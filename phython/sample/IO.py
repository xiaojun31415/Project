#bin/python
#python的简单的输出
#输出的格式化
#表达是语句和print（）函数
#write（）方法，标准输出文件可以用sys.stdout引用
#字符串的输出方式
s="hello world"
print(str(s))
print(repr(s))
for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
#!/usr/bin/python3
str=input("你输入的内容是：")
print("你输入的内容是",str)