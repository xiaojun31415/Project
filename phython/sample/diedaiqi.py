"""
Python3 迭代器与生成器
"""
'''
迭代器
迭代是Python最强大的功能之一，是访问集合元素的一种方式。

迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter() 和 next()。

字符串，列表或元组对象都可用于创建迭代器：
'''
list=[1,2,3,4]
it=iter(list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" , ")

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    x = self.a
    self.a += 1
    return x
 
myclass = MyNumbers()
myiter = iter(myclass)
 
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

'''
生成器
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
'''

'''
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
'''

def hello():
	print("hello")

def area(width,height):
	return width * height
def print_welcome(name):
	print("Welcome",name)


d
