#bin/opt/python

#数字
#数字的简单的定义

var1=1
var2=3
#删除定义的变量
del var2 

#删除的变量的语法
#del var[,var2]
#Python支持的3中数值类型 int float complex（负数 a+bi）
#Python支持数字类型转换

#Python的数字运算（有丰富的函数库支持）

#Python的字符串
#访问字符串的值 可以按照元素访问var[i] 输出第i个元素 var[i:j] 输出i到j的字符元素
var1 = 'Hello World!'
var2 = "Runoob"
 
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

#Python支持字符转义
#字符串的简单操作方法
#in 判断字符串是否存在该字符 not in
#r/R 不转义

a = "Hello"
b = "Python"
 
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
 
if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")
 
if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")
 
print (r'\n')
print (R'\n')

#Python字符串格式化

#Python的列表-对应数组 
#del list[2]删除元素
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

#python的元组-无法修改元素，但是可以进行相关运算
tup1 = ('Google', 'Runoob', 1997, 2000);
tup3 = "a", "b", "c", "d";
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup1[1:3])

#python的字典
#ley：value
#键唯一，但是值可以不唯一
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
print ("dict['Name']: ", dict1['Name'])
print ("dict['Age']: ", dict1['Age'])

dict3 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#修改字典中键对应的值 
dict3['Age'] = 8;               # 更新 Age
dict3['School'] = "菜鸟教程"  # 添加信息
#del dict['Name'] # 删除键 'Name'
#dict.clear()     # 清空字典
#del dict         # 删除字典
 
print ("dict['Age']: ", dict3['Age'])
print ("dict['School']: ", dict3['School'])


#python的集合
'''
parame = {value01,value02,...}
或者
set(value)
'''

>>>basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # 这里演示的是去重功能
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # 快速判断元素是否在集合内
True
>>> 'crabgrass' in basket
False
 
>>> # 下面展示两个集合间的运算.
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # 集合a中包含而集合b中不包含的元素
{'r', 'd', 'b'}
>>> a | b                              # 集合a或b中包含的所有元素
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # 集合a和b中都包含了的元素
{'a', 'c'}
>>> a ^ b                              # 不同时包含于a和b的元素
{'r', 'd', 'b', 'm', 'z', 'l'}
