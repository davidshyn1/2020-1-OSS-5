import os

from os import path
from wordcloud import WordCloud
from konlpy.tag import Hannanum


# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

#get the path of Korean_fonts otf file
font_path = d + '/word_cloud/examples/fonts/NotoSansKR/NotoSansKR-Black.otf'

def listToString(list1):
    str=" " #distinguish nouns by 'space'
    return (str.join(list1))

def get_string():
    f = open(path, "r", encoding="utf-8")
    sample = f.read()
    f.close()
    h = Hannanum()
    list_nouns = h.nouns(sample) #get list of nouns from sample
    return listToString(list_nouns) #get string of list_nouns

path = d + "텍스트파일.txt"
tags = get_string()  # tags : string of list_nouns

wc = WordCloud(font_path=font_path, background_color="white")
draw_wc = wc.generate(tags)
