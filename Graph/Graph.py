import MeCab as mc
from collections import Counter
import seaborn as sns
import numpy as np #wordcloudのマスクに必要
from matplotlib import pyplot as plt
#これがないとグラフが日本語表示されない
import japanize_matplotlib


#Mecabを使いさらに分けている(完成2.pyのMecabでやると単語が一つ一つに別れてしまったので、とりあえず作った)
#完成2.pyの形態素解析とここの形態素解析を二回通した場合、一様動いたので助長になるけどしんどいのでそれでいきたい。
def mecab_analysis(text):
    #パーサーの設定
    t = mc.Tagger("-Ochasen")
    #t.parseでUnicodeDecodeErrorを避けることが出来るらしい
    t.parse('')
    #surface(単語)feature(品詞情報)。node.surface/node.featureでそれぞれにアクセス出来る。
    node = t.parseToNode(text) 
    output = []
    while node:
        if node.surface != "":  # ヘッダとフッタを除外
            word_type = node.feature.split(",")[0]
            if word_type in ["名詞"]:
                output.append(node.surface)
        node = node.next
        if node is None:
            break
    return output

def count_csv():
    text= str(open("/Users/nakano_shougo/Documents/MF184/グラフ化/sample.txt","r",encoding="utf-8").read())
    words = mecab_analysis(text)



# 2.集計
    counter = Counter(words)
# 3.数字が正しいか確認用
    print(counter.most_common())


#グラフのパラメータ  
    plt.title("TOP 10",fontsize=36)
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
    plt.show()


#動作させる為　
def main():
    count_csv()

#これを記入するとターミナルやコンソールから直接動かないようになるらしい
if __name__ == '__main__':
   main()