#!bin/user/bin/python

print('hello')
a=20
b=20
print(a*b)
print("this is sun day!")
#this is a test statement;
a,b=0,1
while b<1000:
    print(b,end=',')
    a,b=b,a+b
'''
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
'''
var1 = 100
if var1:
    print ("1 - if 表达式条件为 true")
    print (var1)
 
var2 = 0
if var2:
    print ("2 - if 表达式条件为 true")
    print (var2)
print ("Good bye!")

count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

for letter in 'Runoob':     # 第一个实例
   if letter == 'b':
      break
   print ('当前字母为 :', letter)

def area(width, height):
    return width * height
 
def print_welcome(name):
    print("Welcome", name)
 
print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

dd=area(w,h)
print(dd)

