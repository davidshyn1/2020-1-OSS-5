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

[example]: http://amueller.github.io/word_cloud/_images/sphx_glr_single_word_001.png
[GoE]: http://amueller.github.io/word_cloud/auto_examples/index.html
