 #filename:test.py
#author by :xiaojun

#导入日历模块
import calendar

#输入指定的年月
yy=int(input("你输入的年份是："))
mm=int(input("你输入的月份是："))

#显示日历
print(calendar.month(yy,mm))
