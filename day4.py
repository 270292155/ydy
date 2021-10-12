dict={"地球":{"中国":{"北京":{"昌平":{"沙河":{"七马路":"北科院"}}}}}}
print(dict["地球"]["中国"])
num1=input("请输入一个地址")
if num1 in dict:
    num2=input("请输入第二个地址")
    if num2 in dict["地球"]:
        num3=input("请输入第三个地址")
        if num3 in dict["地球"]["中国"]:
            print(dict[num1][num2][num3])

