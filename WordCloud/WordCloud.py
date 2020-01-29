from wordcloud import WordCloud
from matplotlib import pyplot as plt

with open('/Users/nakano_shougo/Documents/プログラミング/python/wordcloud.txt', mode='rt', encoding='utf-8') as fo:
    cloud_text = fo.read()

word_cloud = WordCloud().generate(cloud_text)



plt.imshow(word_cloud)
plt.axis('off')
plt.show()
