import os
from os import path
from konlpy.tag import Hannanum
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

font_path = d + '/word_cloud/examples/fonts/NotoSansKR/NotoSansKR-Black.otf'

def listToString(list1):
    str=" " #distinguish by 'space'
    return (str.join(list1))

def get_string(path):
    f = open(path, "r", encoding="utf-8")
    sample = f.read()
    f.close()
    h = Hannanum()
    list_nouns = h.nouns(sample) #get list of nouns from sample
    return listToString(list_nouns) #get string of list_nouns

path = "text파일.txt"
tags = get_string(path)  # tags : string of list_nouns
wc = WordCloud(font_path=font_path, background_color="white",
               max_font_size=100, random_state=42, width=1000, height=860, margin=2)

#display the generated image
import matplotlib.pyplot as plt
plt.imshow(wc, interpolation ='bilnear')
plt.axis("off")