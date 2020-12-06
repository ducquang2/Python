import random
ngua1=0
ngua2=0
ngua3=0
ngua4=0
ngua5=0
while True:
    if (ngua1<6)and(ngua2<6)and(ngua3<6)and(ngua4<6)and(ngua5<6):
        print("----------------------------------------")
        ngua1+=random.randrange(0, 2)
        print("Giá trị con ngựa thứ 1 ",ngua1)
        ngua2+=random.randrange(0, 2)
        print("Giá trị con ngựa thứ 2 ",ngua2)
        ngua3+=random.randrange(0, 2)
        print("Giá trị con ngựa thứ 3 ",ngua3)
        ngua4+=random.randrange(0, 2)
        print("Giá trị con ngựa thứ 4 ",ngua4)
        ngua5+=random.randrange(0, 2)
        print("Giá trị con ngựa thứ 5 ",ngua5)
        print("----------------------------------------")
    else:
        break

if ngua1==6:
    print("Ngựa 1")
elif ngua2==6:
    print("Ngựa 2")
elif ngua3==6:
    print("Ngựa 3")
elif ngua4==6:
    print("Ngựa 4")
else :
    print("Ngựa 5")