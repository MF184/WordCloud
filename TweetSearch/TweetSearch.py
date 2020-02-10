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
#import tweepy
#--------この下に関数を書く--------

#twitterAPI KEY
CONSUMER_KEY =#GIthubにKEYを書いたままで上げて良いのかわからないのでとりあえずKEYなしで
CONSUMER_SECRET =#GIthubにKEYを書いたままで上げて良いのかわからないのでとりあえずKEYなしで
ACCESS_TOKEN =#GIthubにKEYを書いたままで上げて良いのかわからないのでとりあえずKEYなしで
ACCESS_TOKEN_SECRET =#GIthubにKEYを書いたままで上げて良いのかわからないのでとりあえずKEYなしで
#
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)





#TextBoxの文字を削除する(btn2)
def DeleteEntryValue(event):
  #TextBoxの中身を削除
    textBox.delete(0,tk.END)


#キーワードを元にWordCloudを作成(スクレイピング関連もここに記入する)

   

def tweetsearch(Event):
    keyword=textBox.get()
    q=keyword
    count=100
    tweet_list=[]

    tweets = api.search(q=q, locale="ja", count=count,tweet_mode='extended')
    for tweet in tweets:
       tweet_list.append([tweet.id, tweet.user.screen_name, tweet.created_at, tweet.full_text.replace('\n',''), 
       tweet.favorite_count, tweet.retweet_count, tweet.user.followers_count, tweet.user.friends_count])
 
    with open(keyword+'.csv', 'w',newline='',encoding='utf-8') as f:
       writer = csv.writer(f, lineterminator='\n')
       writer.writerow(["id","user","created_at","text","fav","RT","follower","follows"])
       writer.writerows(tweet_list)
   

pass



#メインウィンドウ作成
root = tk.Tk()
    #ウィンドウタイトルを指定
root.title("WordCloud")
    #ウィンドウサイズを指定
root.geometry("1700x1600")
    #ウィンドウサイズ固定
#root.resizable(0,0)
    #ウィンドウの背景色
root.configure(bg="white")


#キーワードを入力する為のTextBox
textBox = tk.Entry()
textBox.configure(state='normal',width=26)
textBox.place(x=20,y=20)
#座標を指定して設置する
textBox.insert(tk.END,"#を付けてキーワードを入力する")
#フォームを開いた際にtxtBoxに文字を表示する(薄くしたい)


#txtBoxに入力されたキーワードからTwitterでスクレイピングをし、detaとして落とし込む(WordCloudで読み込むために)
btn = tk.Button(root,text='表示',width=10)
btn.place(x=270, y=23)
btn.bind("<Button-1>",tweetsearch)

#btn２はtxtBoxの文字をクリアするボタン(作業を楽にする為に付けたやつなので、助長なら消しても良い by中野)
btn2=tk.Button(root,text='クリア',width=10)
btn2.place(x=370,y=23)
btn2.bind("<Button-1>",DeleteEntryValue) 
#メモ　<Button-1>はクリック、<Button-2>はホイールクリック、<Button-3>は右クリック(他もpython bindで調べると出てくる)


#コンボボックス(WordCloudのbackgroundの色を変える)

frame = ttk.Frame(root,padding=10)
frame.grid()

root.mainloop()