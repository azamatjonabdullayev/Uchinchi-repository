for i in range(10, 100):
    tub = 0

    for j in range(1, i+1):
        if i % j == 0:
            tub+=1


    if tub == 2:
        print(i, end=" ")
