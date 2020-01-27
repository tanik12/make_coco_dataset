import glob
import os
import sys
import re

import xml.etree.ElementTree as et

def read():
    # 拡張子.jpgのファイルを取得する
    xml_path = './annotations/Annotations/*.xml'
    img_path = './images/train9999/*.jpg'
    # image pathを取得する
    file_lists = glob.glob(xml_path)
    img_lists = glob.glob(img_path)
    return file_lists, img_lists

def rename(file_lists, img_lists):
    i = 1
    prefix_name = "COCO_train9999_"

    #重複しない接頭文字を格納する
    prefixes = set() 
    for img_path in img_lists:
        img_name = os.path.basename(img_path)
        #print(img_name)
        sp_str = img_name.split("_")
        pre_str = img_name.replace(sp_str[-1], "")
        #print(sp_str)
        prefixes.add(pre_str)
    print(prefixes)
    for file_name in file_lists:
        tree = et.ElementTree(file=file_name)
        root = tree.getroot()

        img_name = ""

        for item in root:
            #xmlやimageの名前、xmlの中身の一部(filename, path)のリネーム処理をする。
            if item.tag == "filename":
                item.text = prefix_name + "%09.f.jpg" % i #xmlの中のfilenameタグの中をリネーム
            elif item.tag == "path":
                basename = os.path.basename(item.text) #get file name
                
                for tmp in prefixes:
                    #取得したファイル名の中に接頭文字(tmp)があるか確認。あった場合その接頭文字を消して数字だけを取得する。
                    if tmp in basename: 
                         #数字を取得
                         number = re.sub(r'\D', '', basename.replace(tmp, ""))
                
                for prefix in prefixes:
                    #print('./images/train9999/' + prefix + number + ".jpg")
                    #print(os.path.isfile('./images/train9999/' + prefix + number + ".jpg"))
                    if os.path.isfile('./images/train9999/' + prefix + number + ".jpg"):
                        print("Yes. exist file name")
                        os.rename('./images/train9999/' + prefix + number + ".jpg", './images/train9999/' + prefix_name + "%09.f.jpg" % i) #image名の変更
                        item.text = "./images/train9999/" + prefix_name + "%09.f.jpg" % i #xmlの中のpathタグの中をリネーム
                        tree.write('./annotations/Annotations/' + "%09.f.xml" % i)               #xmlファイル名を修正
                        os.remove(file_name)
                        print("=========================")
                        break
                    else:
                        print("No. file name")
                        continue

        i += 1

def main():
    file_lists, img_lists = read()
    rename(file_lists, img_lists)
    
if __name__ == "__main__":
    main()