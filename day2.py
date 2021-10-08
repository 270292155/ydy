import  random
randit=random.randint(10,100)#从10到100之前随机取一个数字
while True:
    num1=int(input("请输入一个数"))
    print(num1)
    if num1==randit:
        print("猜对了")
        break
    elif num1>randit:
        print("猜大了")
    else:print("猜小了")


