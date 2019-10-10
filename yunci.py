import jieba
from PIL import Image
import numpy as np
from wordcloud import WordCloud,ImageColorGenerator
fn = open('love.txt','r',encoding='utf-8') # 打开文件
jb = fn.read() # 读出整个文件
fn.close() # 关闭文件
jb = jieba.lcut(jb)
jb =' '.join(jb)
maskcover = np.array(Image.open('love.png'))
img_color = ImageColorGenerator(maskcover)
w = WordCloud(
    background_color='white',
    max_words=160,
    random_state=42,
    width=1000,
    height=800,
    margin=1,
    mask=maskcover,
    max_font_size=180,
    font_path='./simhei.ttf',
    ).generate(jb)
import matplotlib.pyplot as plt
plt.imshow(w)
plt.imshow(w.recolor(color_func=img_color))
plt.axis('off')
plt.show()