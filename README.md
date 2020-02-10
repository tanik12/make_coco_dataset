## このリポジトリについて
VOC形式のデータセットと自作のデータセット(VOC形式)を1つのデータセットにするためのリポジトリです。<br>
COCO形式からVOC形式に変換したデータセットでも動作確認はできています。<br><br>
本リポジトリでは、COCO形式からVOC形式に変換したデータセットと自作データセットを1つにします。<br>

## 使い方の前準備として
1. mkdir mydataset && cd coco && mkdir annotations && mkdir images
2. mkdir -p annotations/Annotations
3. mkdir -p images/train9999 (train9999は暫定版なので後で変更する)

　各ディレクトリについて<br>
　mydatasetには自作データを入れること。<br>
　annotations/Annotationsにアノテーションデータを入れること。<br>
　images/train9999に画像データを入れること。<br>

## 使い方
**1. cocoデータセットの移動**<br>
　cocoアノテーションのファイル群をannotations/Annotationsに入れる<br>
　cocoの画像群をimages/train9999に入れる。<br><br>
**2. 自作データセットの準備**<br>
　　datasetディレクトリに自分のデータセットを置く。(一時保管用)<br>
　　※注意<br>
　　・自作データは○○○_00001.xmlのようなprefixをつけること。<br>
　　・以降説明に書かれているmain.pyを実行するとrenameされるので元データは保管すること。<br>
 
　　自分のデータセットを置いたら下記を行う。<br>
　　・自作データのアノテーションをannotationsフォルダに入れる。<br>
　　・自作データの画像をimagesに入れる。<br><br>

**3. コマンドの実行**<br>
※2の自作データセットの準備でも伝えたようにmain.pyを実行するとrenameされるので元データは保管すること。<br>
python main.py<br>
