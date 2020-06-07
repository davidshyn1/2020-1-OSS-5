---
layout: post
title: "[한글 문서화] Gallery of Examples"
author: "OSS-5"
---


>word_cloud GitHub Page의 [Gallery of Examples][GoE] 항목을 번역 및 보완한 문서입니다.
<hr>

단일 단어 (Single Word)
===========

반복되는 단어로 Word cloud를 만들기.



![example][example]


    import numpy as np
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud

    text = "square"

    x, y = np.ogrid[:300, :300]

    mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
    mask = 255 * mask.astype(int)


    wc = WordCloud(background_color="white", repeat=True, mask=mask)
    wc.generate(text)

    plt.axis("off")
    plt.imshow(wc, interpolation="bilinear")
    plt.show()



**Script의 총 실행 시간:** ( 0 분  0.532 초)
<hr>


아랍어로 wordcloud 만들기 (Create wordcloud with Arabic)
===========

아랍어 텍스트에서 word cloud 생성


Dependencies : - bidi.algorithm - arabic_reshaper


Dependencies 설치: pip install python-bidi arabic_reshape



Out:

`<wordcloud.wordcloud.WordCloud object at 0x7fa0f73e5fd0>`


    import os
    import codecs
    from wordcloud import WordCloud
    import arabic_reshaper
    from bidi.algorithm import get_display

    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    f = codecs.open(os.path.join(d, 'arabicwords.txt'), 'r', 'utf-8')

    # Make text readable for a non-Arabic library like wordcloud
    text = arabic_reshaper.reshape(f.read())
    text = get_display(text)

    # Generate a word cloud image
    wordcloud = WordCloud(font_path='fonts/NotoNaskhArabic/NotoNaskhArabic-Regular.ttf').generate(text)

    # Export to an image
    wordcloud.to_file("arabic_example.png
    
    
**Script의 총 실행 시간:** ( 0 분  0.929 초)

<hr>


Minimal Example
===========

기본 인수를 사용하여 직각의 미국 헌법 wordcloud 생성

![example1][example1]


![example2][example2]
    
    import os

    from os import path
    from wordcloud import WordCloud

    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    text = open(path.join(d, 'constitution.txt')).read()

    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    # The pil way (if you don't have matplotlib)
    # image = wordcloud.to_image()
    # image.show()


**Script의 총 실행 시간:** ( 0 분  1.024 초)
<hr>


차폐된 Wordcloud (Masked wordcloud)
===========
Mask를 사용하면 임의의 모양으로 word cloud를 생성할 수 있습니다

![example3][example3]


![example4][example4]

    from os import path
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt
    import os

    from wordcloud import WordCloud, STOPWORDS

    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    text = open(path.join(d, 'alice.txt')).read()

    # read the mask image
    # taken from
    # http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
    alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))

    stopwords = set(STOPWORDS)
    stopwords.add("said")

    wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
                   stopwords=stopwords, contour_width=3, contour_color='steelblue')

    # generate word cloud
    wc.generate(text)

    # store to file
    wc.to_file(path.join(d, "alice.png"))

    # show
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.figure()
    plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    plt.show()


**Script의 총 실행 시간:** ( 0 분  5.110 초)
<hr>


사용 빈도 (Using frequency)
===========
단어 빈도 사전을 사용한다

![example5][example5]


    import multidict as multidict

    import numpy as np

    import os
    import re
    from PIL import Image
    from os import path
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt


    def getFrequencyDictForText(sentence):
        fullTermsDict = multidict.MultiDict()
        tmpDict = {}

        # making dict for counting frequencies
        for text in sentence.split(" "):
            if re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|that|be", text):
                continue
            val = tmpDict.get(text, 0)
            tmpDict[text.lower()] = val + 1
        for key in tmpDict:
            fullTermsDict.add(key, tmpDict[key])
        return fullTermsDict


    def makeImage(text):
        alice_mask = np.array(Image.open("alice_mask.png"))

        wc = WordCloud(background_color="white", max_words=1000, mask=alice_mask)
        # generate word cloud
        wc.generate_from_frequencies(text)

        # show
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        plt.show()


    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    text = open(path.join(d, 'alice.txt'), encoding='utf-8')
    text = text.read()
    makeImage(getFrequencyDictForText(text))

**Script의 총 실행 시간:** ( 0 분  4.469 초)
<hr>


이미지 컬러 (Image-colored wordcloud)
===========
ImageColorGenerator에서 구현된 이미지 기반 색상 지정 방법을 사용하여 word cloud를 채색할 수 있습니다. 소스 이미지에서 단어가 차지하는 영역의 평균 색상을 사용합니다. 이것은 masking과 결합할 수 있습니다. 순수한 흰색은 mask로 전달될 때 WordCloud 객체에서 '사용하지 않음'으로 해석됩니다. 법적 색상으로 흰색을 원할 경우 다른 이미지를 "마스크"에 전달하기만 하면 되지만 이미지 모양이 정렬되도록 하십시오.

![example6][example6]

    from os import path
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt
    import os

    from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # Read the whole text.
    text = open(path.join(d, 'alice.txt')).read()

    # read the mask / color image taken from
    # http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
    alice_coloring = np.array(Image.open(path.join(d, "alice_color.png")))
    stopwords = set(STOPWORDS)
    stopwords.add("said")

    wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                   stopwords=stopwords, max_font_size=40, random_state=42)
    # generate word cloud
    wc.generate(text)

    # create coloring from image
    image_colors = ImageColorGenerator(alice_coloring)

    # show
    fig, axes = plt.subplots(1, 3)
    axes[0].imshow(wc, interpolation="bilinear")
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    axes[2].imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
    for ax in axes:
        ax.set_axis_off()
    plt.show()

**Script의 총 실행 시간:** ( 0 분  3.193 초)
<hr>


이모티콘 예시 (Emoji Example)
===========
그림 이모티콘을 포함하는 방법을 보여주는 간단한 예입니다. 이 예제는 OS X에서는 작동하지 않지만 Ubuntu에서는 올바르게 작동합니다.

그림 이모티콘을 포함하기 위해 따라야 할 3가지 중요한 단계가 있습니다. 1) built in open 대신 io.open으로 텍스트 입력을 읽습니다. 이렇게 하면 UTF-8으로 load됩니다. 2) Word cloud가 사용하는 정규식을 재정의하여 텍스트를 단어로 구문 분석합니다. 기본 표현식은 ASCII 단어와만 일치합니다. 3) 기본 글꼴을 그림 이모티콘을 지원하는 것으로 재정의합니다. 포함된 Symbola 글꼴에는 대부분의 이모티콘에 대한 흑백 윤곽선이 포함되어 있습니다. 현재 OS X (https://github.com/python-pillow/Pillow/issues/1774)에서 올바르게 작동하지 못하게 하는 PIL / Pillow 라이브러리에 문제가 있으므로, 문제가 있는 경우 우분투에서 시도하십시오.

![example7][example7]

    import io
    import os
    import string
    from os import path
    from wordcloud import WordCloud

    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # It is important to use io.open to correctly load the file as UTF-8
    text = io.open(path.join(d, 'happy-emoji.txt')).read()

    # the regex used to detect words is a combination of normal words, ascii art, and emojis
    # 2+ consecutive letters (also include apostrophes), e.x It's
    normal_word = r"(?:\w[\w']+)"
    # 2+ consecutive punctuations, e.x. :)
    ascii_art = r"(?:[{punctuation}][{punctuation}]+)".format(punctuation=string.punctuation)
    # a single character that is not alpha_numeric or other ascii printable
    emoji = r"(?:[^\s])(?<![\w{ascii_printable}])".format(ascii_printable=string.printable)
    regexp = r"{normal_word}|{ascii_art}|{emoji}".format(normal_word=normal_word, ascii_art=ascii_art,
                                                         emoji=emoji)

    # Generate a word cloud image
    # The Symbola font includes most emoji
    font_path = path.join(d, 'fonts', 'Symbola', 'Symbola.ttf')
    wc = WordCloud(font_path=font_path, regexp=regexp).generate(text)

    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wc)
    plt.axis("off")
    plt.show()

**Script의 총 실행 시간:** ( 0 분  0.539 초)
<hr>


맞춤 색상 사용 (Using custom colors)
===========
색상 변경 방법 및 사용자 지정 색상 기능 사용

![example8][example8]
![example9][example9]

    import numpy as np
    from PIL import Image
    from os import path
    import matplotlib.pyplot as plt
    import os
    import random

    from wordcloud import WordCloud, STOPWORDS


    def grey_color_func(word, font_size, position, orientation, random_state=None,
                        **kwargs):
        return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


    # get data directory (using getcwd() is needed to support running example in generated IPython notebook)
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

    # read the mask image taken from
    # http://www.stencilry.org/stencils/movies/star%20wars/storm-trooper.gif
    mask = np.array(Image.open(path.join(d, "stormtrooper_mask.png")))

    # movie script of "a new hope"
    # http://www.imsdb.com/scripts/Star-Wars-A-New-Hope.html
    # May the lawyers deem this fair use.
    text = open(path.join(d, 'a_new_hope.txt')).read()

    # pre-processing the text a little bit
    text = text.replace("HAN", "Han")
    text = text.replace("LUKE'S", "Luke")

    # adding movie script specific stopwords
    stopwords = set(STOPWORDS)
    stopwords.add("int")
    stopwords.add("ext")

    wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords, margin=10,
                   random_state=1).generate(text)
    # store default colored image
    default_colors = wc.to_array()
    plt.title("Custom colors")
    plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
               interpolation="bilinear")
    wc.to_file("a_new_hope.png")
    plt.axis("off")
    plt.figure()
    plt.title("Default colors")
    plt.imshow(default_colors, interpolation="bilinear")
    plt.axis("off")
    plt.show()

**Script의 총 실행 시간:** ( 0 분  7.464 초)

[example]: http://amueller.github.io/word_cloud/_images/sphx_glr_single_word_001.png
[example1]: http://amueller.github.io/word_cloud/_images/sphx_glr_simple_001.png
[example2]: http://amueller.github.io/word_cloud/_images/sphx_glr_simple_002.png
[example3]: http://amueller.github.io/word_cloud/_images/sphx_glr_masked_001.png
[example4]: http://amueller.github.io/word_cloud/_images/sphx_glr_masked_002.png
[example5]: http://amueller.github.io/word_cloud/_images/sphx_glr_frequency_001.png
[example6]: http://amueller.github.io/word_cloud/_images/sphx_glr_colored_001.png
[example7]: http://amueller.github.io/word_cloud/_images/sphx_glr_emoji_001.png
[example8]: http://amueller.github.io/word_cloud/_images/sphx_glr_a_new_hope_001.png
[GoE]: http://amueller.github.io/word_cloud/auto_examples/index.html
