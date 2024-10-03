import random as r

urinish = int(input("Necha marta urunasiz?\n>>>>>>>>>> "))
a = urinish

rand_son = r.randint(1, 1000)

son = int(input("Son kiriting: "))

while urinish > 0:

    if son == rand_son:
        if a == 1:
            print("Tabriklaymiz!!!\nSiz 1 000 000 so'm yutib oldingiz!")
            break
        elif a == 2:
            print("Tabriklaymiz!!!\nSiz 500 000 so'm yutib oldingiz!")
            break
        elif a == 3:
            print("Tabriklaymiz!!!\nSiz 100 000 so'm yutib oldingiz!")
            break
        else:
            print("Tabriklaymiz!!!\nSiz 10 000 so'm yutib oldingiz!")
            break
    else:
        urinish -= 1
        if urinish == 0:
            print("Afsus, siz yutqazdingiz!")
        else:
            if son > rand_son:
                son = int(input("Kichikroq son kiriting: "))
            else:
                son = int(input("Kattaroq son kiriting: "))