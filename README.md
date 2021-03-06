# WordCloud
MF2020に向けての作品リポジトリ.

## セットアップ

* そもそもGithubにSSH鍵の設定してないなら、先に[これ](https://qiita.com/shizuma/items/2b2f873a0034839e47ce)を見て登録してくれ.
* まずはこのリポジトリをForkする.
* 事前にターミナルやGitBashなどでローカルの作業するディレクトリに移動しておく.  

```
① git clone 各自ForkしたWordCloudのリポジトリのurl
② git remote add upstream git@github.com:MF184/WordCloud.git
```
###### ①git clone でリポジトリをローカルにコピー.分からなければ調べて
###### ②git remote で上流のリポジトリを登録

設定は、
```
$ git config --list
```
で確認できる.

## 作業の流れ

```#10 ◯◯の機能を追加する```というissueを割り当てられたとする.
```
① git checkout feature-10  
② git branch
```
###### ①checkout でブランチの切り替えができ、今回は#10なのでfeature-10でブランチを切った.
###### ②どのブランチにいるか確認でき、 -a オプションでリモートのブランチも確認できる

* 作業終了時
```
①git  status
②git add ファイル名
③git  status
④git commit -m 　'' または　""
⑤git push　origin feature-10
```
###### ①③変更箇所や損失箇所が確認できる. 大事なことなので、add前はもちろん、合間合間にする癖を付けておく.
###### ②ファイル名の代わりに -A と入力すると変更済が全てステージングされる(基本的には-Aでおk. ただ馬鹿みたいに全て変更したら周りに危害が被るので、気を付ける)
###### ④'#10 ◯◯の機能を追加する' ''内にコミットメッセージを入力する（更新する内容を記入する. これがないと何をしたか分かりづらい）
###### ⑤リモートに更新

他、分からないことがあれば調べよう.

## リモートの変更内容を取り込む

自分の変更を取り込む前に、他人の変更が入る場合があり、その時は上流の変更を取り込む必要がある.　Slackに通知を来ると思うのでその時に使用する.

```
①git checkout develop
②git pull upstream develop
③git push origin develop
```
###### ①developに切り替え
###### ②上流リポジトリの変更を自分のローカルに落とし込み、ローカルのdevelopに変更点を追加(これは一括した方法で、他にも方法はある)
###### ③自分のリモートリポジトリにも変更を追加

基本はこれで大丈夫だと思います。後分からないことは調べてください(特にstashなどは簡単で覚えると作業が楽)

後作業するときは、必ずbranchを変えてから作業してくれ！！！とてもめんどくさいことになる！！！  
なので自分が今どのbranchにいるかは確認する癖は付けておく！！！    
じゃないと'O S A R U'って呼ぶぞ!!!   

###### 引用が何故か出来ない＆眠い＆反映しなかったので＃＃＃＃＃の方法のこの書き方で説明してすいません...
###### 後日修正します...
