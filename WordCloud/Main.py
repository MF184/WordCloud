import tkinter as tk
import tkinter.ttk as ttk
import requests                 #
from bs4 import BeautifulSoup   #
import csv
import time

from datetime import datetime
#この下に関数を書く

#TextBoxの文字を削除する(btn2)
def DeleteEntryValue(event):
  #TextBoxの中身を削除
    textBox.delete(0,tk.END)

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
textBox.configure(state='normal',width=20)
textBox.place(x=20,y=20)
#座標を指定して設置する
textBox.insert(tk.END,"#を付けてキーワードを入力する")
#フォームを開いた際にtxtBoxに文字を表示する


#txtBoxに入力されたキーワードからTwitterでスクレイピングをし、detaとして落とし込む(WordCloudで読み込むために)
btn = tk.Button(root,text='表示',width=10)
btn.place(x=220, y=23)


#btn２はtxtBoxの文字をクリアするボタン(作業を楽にする為に付けたやつなので、助長なら消しても良い by中野)
btn2=tk.Button(root,text='クリア',width=10)
btn2.place(x=320,y=23)
btn2.bind("<Button-1>",DeleteEntryValue) 
#メモ　<Button-1>はクリック、<Button-2>はホイールクリック、<Button-3>は右クリック(他もpython bindで調べると出てくる)



frame = ttk.Frame(root,padding=10)
frame.grid()

root.mainloop()