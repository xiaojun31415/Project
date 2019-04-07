#循环
#while的斐波那契数
a,b=0,1
while b<10:
	print(b)
	a,b=b,b+a
	
while b<10:
	#print(b，end=',')#end 的关键字无法使用
	a,b=b,b+a
#条件语句
'''
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
'''
#循环语句
'''
while 判断条件：
    语句
while 循环使用 else 语句
在 while … else 在条件语句为 false 时执行 else 的语句块：
'''
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
   
'''
for 语句
Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

for循环的一般格式如下：
for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''

language=["C","C++","python"]
for x in language:
	print(x)
	
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")