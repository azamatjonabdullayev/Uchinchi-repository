son = int(input("Son kiriting: "))

ikkinchi_son = 0

while son>0:
    a = son%10
    ikkinchi_son = (ikkinchi_son*10)+a
    son//=10

while ikkinchi_son>0:
    b = ikkinchi_son%10
    print(b, end=" ")
    ikkinchi_son//=10