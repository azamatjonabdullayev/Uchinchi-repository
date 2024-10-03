for i in range(100, 1000):
    yuzlik = i // 100
    onlik = (i // 10) % 10
    birlik = i % 10

    if (yuzlik==onlik and yuzlik !=birlik) or (yuzlik == birlik and yuzlik != onlik) or (birlik == onlik and birlik != yuzlik):
        print(i, end=" ")
