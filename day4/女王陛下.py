
'''姐就是女王:
随机选择人物： 1、普通没有技能
2、稀有英雄初始值为30。3、传奇英雄不会减少只会增加
需求：
初始值为：10
随机生成三个数字
随机选择一个数字
选择的数字和初始值进行计算（随机加减）
计算过后大于100则任务成功
计算过后小于或等于0则任务失败'''


#随机选择人物："稀有","传奇"
import  random                         #随机数
list=["普通"]         #列表
name=[list[random.randint(0,len(list)-1)]]    #判断名称角标
print(name)                #输出
num=50                      #初始值
if name=="普通":            #判断 ==普通
    while True:              #真假
        i=0                     #从零开始
        list1=[]               #空的列表
        while i<3:              #判断i是否小于三，小于三运行小面 的代码
            i=i+1                 #每次循环都加1
            a=random.randint(5,20)   #随机数
            list1.append(a)            #添加一个数
            print(list1)             #输出
            num1=list1[random.randint(0,len(list1)-1)]  #这是2边随机取出来的num
            print(num1)
            lisat2=[1,2]  #1加号 2减号
            name2=list[random.randint(0,len(list)-1)]  #随机加减
            if name2==1:
                num=num1+num
                print(num)
            elif name2==2:
                num=num1-num
                print(num)
                if num>100:
                    print("任务成功你的分数为",num)
                    break
                elif num<=0:
                    print("任务失败你的分数为",num)
                    break

list16=["稀有"]
name=list16[random.randint(0,len(list16)-1)]
    print(name)
    num6 = 30
    if name=="稀有":
        while True:
            i=0
            list5=[]
            while i<3:
                i=i+1
                a5=random.randint(10,20)
                list5.append(a5)
                print(list5)

            num5 = list5[random.randint(0, len(list5) - 1)]  # 这是两边随机取出来的数字num1
            print(num5)
            list6= [1, 2]  # 1 ==加号  2 等于减号
            name6 = list6[random.randint(0, len(list6) - 1)]  # 随机的加减
            if name6 == 1:  # 随机的加减如果等于1 进行加法运算
                num = num6 + num
                print(num)  # 初始num 加上一个随机取出来的数字
            elif name6 == 2:  # 随机的加减如果等于1 进行减法运算
                num = num6 - num
                print(num)  # 初始num 加上一个随机取出来的数字
            if num > 100:
                print("任务成功你的分数为", num)
                break
            elif num <= 0:
                print("任务失败你的分数为", num)
                break


list10=["传奇"]
name=list10[random.randint(0,len(list10)-1)]
print(name)
    if name=="传奇":
        while True:
            i=0
            list11=[]
            while i<3:
                i=i+1
                b=random.randint(15,30)
                list11.append(b)
                print(list11)

                num11=list12[random.randint(0,len(list11)-1)]
                print(num11)
                list12=[1,2]
                name2 = list12[random.randint(0, len(list12) - 1)]
                if name==1:
                    num=num+num
                    print(num)
                elif name2==2:
                    num=num-num
                    print(num)
                    if num>100:
                        print("任务成功分数为",num)
                        break
                    elif num<=0:
                        print("任务失败",num)
                        break





