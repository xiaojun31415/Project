#bin/python

#简单数字求和

#file name :xiaojun
#输入用户求和的数字
num1=input("请输入第一个数字：")
num2=input("请输入第二个数字：")

#求和
sum =float(num1)+float(num2)

#显示计算结果
print('数字{0}和{1}相加的结果为:{2}'.format(num1,num2,sum))

#精简化后的代码
print('两数之和为 %.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))