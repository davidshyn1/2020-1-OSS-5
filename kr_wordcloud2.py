from konlpy.tag import Hannaum


def listToString(list1):
    str=""
    return (str.join(list1))

def get_string():
    f = open("파일명.txt", "r", encoding="utf-8") 
    sample = f.read()
    f.close()
