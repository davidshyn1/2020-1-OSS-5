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

[example]: http://amueller.github.io/word_cloud/_images/sphx_glr_single_word_001.png
[example1]: http://amueller.github.io/word_cloud/_images/sphx_glr_simple_001.png
[example2]: http://amueller.github.io/word_cloud/_images/sphx_glr_simple_002.png
[GoE]: http://amueller.github.io/word_cloud/auto_examples/index.html
