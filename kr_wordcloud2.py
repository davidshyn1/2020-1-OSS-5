from konlpy.tag import Hannaum

def listToString(list1):
    str=""
    return (str.join(list1))

def get_string():
    f = open("파일명.txt", "r", encoding="utf-8") 
    sample = f.read()
    f.close()
    h = Hannaum()
    list_nouns = h.nouns(sample) #get list of nouns from sample
    return listToString(list_nouns) #get string of list_nouns

tags = get_string()  # tags : string of list_nouns
