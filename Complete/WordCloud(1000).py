import tkinter as tk
import tkinter.ttk as ttk
#ComboBoxに必要
import requests                 #
import numpy as np #wordcloudのマスクに必要
from bs4 import BeautifulSoup   #
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import csv
import time
from datetime import datetime
from PIL import Image, ImageTk
import os
import tweepy
import MeCab
from collections import Counter
import seaborn as sns
#これがないとグラフが日本語表示されない
import japanize_matplotlib

#--------この下に関数を書く--------

#twitterAPI KEY
CONSUMER_KEY =
CONSUMER_SECRET =
ACCESS_TOKEN =
ACCESS_TOKEN_SECRET =

#
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)




#グラフ用
def mecab_analysis(word):
    #パーサーの設定
    t = MeCab.Tagger('-Ochasen')
    #-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd
    #t.parseでUnicodeDecodeErrorを避けることが出来るらしい？
    t.parse('')
    #surface(単語)feature(品詞情報)。node.surface/node.featureでそれぞれにアクセス出来る。
    node = t.parseToNode(word) 
    output = []
    while node:
        if node.surface != "":  # ヘッダとフッタを除外
            word_type = node.feature.split(",")
            if word_type[0] == "名詞"and word_type[1] == "一般":
                output.append(node.surface)
        node = node.next
        if node is None:
            break
    return output




#TextBoxの文字を削除する(btn2)
def DeleteEntryValue(event):
  #TextBoxの中身を削除
    textBox.delete(0,tk.END)


# ラベルの色を変更する 各オプションには[オプション]でアクセスする　colorは16進数表記
def changeColor(targetbtn,color):
    targetbtn["foreground"]=color


#キーワードを元に棒グラフを作成
def TweetGraph(event):
    text= str(open(keyword+'.txt',"r").read())
    #グラフ用の解析を呼び出し
    words = mecab_analysis(text) 
    #集計　   
    counter = Counter(words)
    #グラフのパラメータ  
    plt.figure(figsize=(15,8),dpi=100)
    plt.title("#"+keyword+" TOP 10",fontsize=36)
    plt.xlabel('出現頻度が多い10単語')
    plt.ylabel('出現頻度数')

    #Xの値(項目名)
    #counter.most_common()[0][0]の場合、文字の間にある''*'が最大になるので、[1][0]から始める　
    left = np.array([counter.most_common()[1][0],counter.most_common()[2][0],counter.most_common()[3][0],counter.most_common()[4][0],counter.most_common()[5][0]
    ,counter.most_common()[6][0],counter.most_common()[7][0],counter.most_common()[8][0],counter.most_common()[9][0],counter.most_common()[10][0]])

    #Yの値(数字)　グラフの最大値はheightの最大値に合わせられる
    height = np.array([counter.most_common()[1][1],counter.most_common()[2][1],counter.most_common()[3][1],counter.most_common()[4][1],counter.most_common()[5][1]
    ,counter.most_common()[6][1],counter.most_common()[7][1],counter.most_common()[8][1],counter.most_common()[9][1],counter.most_common()[10][1]])
    plt.bar(left, height,color="#FF82B2")
    ##99FFFF
    plt.savefig(keyword)
    global img
    filePath = keyword+'.png'
    canvas = tk.Canvas(bg="white", width=1400, height=900)
    canvas.place(x=250, y=100)
    img = Image.open(filePath)
    img = ImageTk.PhotoImage(img)  # 表示するイメージを用意
    canvas.create_image(0, 0, image=img, anchor=tk.NW)
    os.remove(keyword+'.png')
    os.remove(keyword+'.txt')













#キーワードを元にWordCloudを作成
def TweetWordCloud(Event):
    global keyword
    keyword=textBox.get()
    q='#'+keyword
    count=100
    tweet_list=[]

    tweets = api.search(q=q+"exclude:retweets", locale="ja", count=count,tweet_mode='extended')
    for tweet in tweets:
       tweet_list.append([tweet.id, tweet.user.screen_name, tweet.created_at, tweet.full_text.replace('\n',''), 
       tweet.favorite_count, tweet.retweet_count, tweet.user.followers_count, tweet.user.friends_count])
    next_max_id = tweets[-1].id
    for i in range(2,11):
        tweets = api.search(q=q+"exclude:retweets", locale="ja", count=count,tweet_mode='extended',max_id = next_max_id-1)
        next_max_id = tweets[-1].id
        for tweet in tweets:
            tweet_list.append([tweet.id, tweet.user.screen_name, tweet.created_at, tweet.full_text.replace('\n',''), 
            tweet.favorite_count, tweet.retweet_count, tweet.user.followers_count, tweet.user.friends_count])
    with open(keyword+'.csv', 'w',newline='',encoding='utf-8') as f:
       writer = csv.writer(f, lineterminator='\n')
       writer.writerow(["id","user","created_at","text","fav","RT","follower","follows"])
       writer.writerows(tweet_list)

    f = open(keyword+'.csv',encoding="utf-8")
    tango =f.read()
    text = tango.replace('\n','').replace('\t','')
    f.close()
    m = MeCab.Tagger ('-Ochasen')
 #-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd
    word=""
    node = m.parseToNode(text)
    while node:
        meisi = node.feature.split(",")
        if meisi[0] == "名詞"and meisi[1] == "一般":
            origin = node.feature.split(",")[6]
            if origin not in ['てる', 'いる', 'なる', 'れる', 'する', 'ある', 'こと', 'これ', 'さん', 'して', 
             'くれる', 'やる', 'くださる', 'そう', 'せる', 'した',  '思う',  
             'それ', 'ここ', 'ちゃん', 'くん', '', 'て','に','を','は','の', 'が', 'と', 'た', 'し', 'で', 
             'ない', 'も', 'な', 'い', 'か', 'ので', 'よう', '', 'れ','さ','なっ']:
                word = word + " " + origin
        node = node.next
    fpath ="C:/Users/mf/Desktop/MF184/NotoSansCJKjp-Regular.otf"
    #fpath ="/Library/Fonts/ヒラギノ角ゴシック W3.ttc"
    wordcloud = WordCloud(background_color="white",width=1400,font_path=fpath,height=900,min_font_size=15,collocations = False)
    wordcloud.generate(word)
    changeColor(btn3,"#F0F")
    wordcloud.to_file(keyword+'.png')
    with open(keyword+".txt",'w')as f:
        print(word,file=f)
    
    global img
    filePath = keyword+'.png'
    canvas = tk.Canvas(bg="white", width=1400, height=900)
    canvas.place(x=250, y=100)
    img = Image.open(filePath)
    img = ImageTk.PhotoImage(img)  # 表示するイメージを用意
    canvas.create_image(0, 0, image=img, anchor=tk.NW)
    os.remove(keyword+'.png')
    os.remove(keyword+'.csv')

pass

#メインウィンドウ作成
root = tk.Tk()
    #ウィンドウタイトルを指定
root.title("WordCloud")
    #ウィンドウサイズを指定
root.geometry("1920x1080")
    #ウィンドウサイズ固定
#root.resizable(0,0)
    #ウィンドウの背景色
root.configure(bg="#CCFFCC")


#キーワードを入力する為のTextBox
textBox = tk.Entry()
textBox.configure(state='normal',width=26)
textBox.place(x=20,y=26)
#座標を指定して設置する
textBox.insert(tk.END,"キーワードを入力する")
#フォームを開いた際にtxtBoxに文字を表示する(薄くしたい)


#btnはtxtBoxに入力されたキーワードからTwitterでスクレイピングをし、WordCloudで表示する
btn = tk.Button(root,text='表示',width=10)
btn.place(x=270, y=23)
btn.bind("<Button-1>",TweetWordCloud)


#btn２はtxtBoxの文字をクリアするボタン(作業を楽にする為に付けたやつなので、助長なら消しても良い by中野)
btn2=tk.Button(root,text='クリア',width=10)
btn2.place(x=470,y=23)
btn2.bind("<Button-1>",DeleteEntryValue) 
#メモ　<Button-1>はクリック、<Button-2>はホイールクリック、<Button-3>は右クリック(他もpython bindで調べると出てくる)


#btn3はtxtBoxに入力されたキーワードからTwitterでスクレイピングをし、棒グラフで表示する
btn3=tk.Button  (root,text='グラフで表示',fg="#EEEEEE",bg="#EEEEEE",width=10,command=lambda:changeColor(btn3,"#EEEEEE"))
btn3.place(x=370,y=23)
btn3.bind("<Button-1>",TweetGraph)



frame = ttk.Frame(root,padding=10)
frame.grid()

root.mainloop()