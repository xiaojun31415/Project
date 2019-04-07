echo "this is first linxu script"
#linux的简答注释方法
#方法1 使用"#"注释
#方法2 使用":<<EOF 注释内容 <<EOF
#求两个数之和 使用函数"awk" or "expr"
val=`expr 2 + 2`;
echo "the two number is summary: ${val}";
a=20;
b=30;
val=`expr $a - $b`;
echo "a - b : $val";

val=`expr $a \* $b`;
echo "a * b : $val";
#乘号(*)前边必须加反斜杠(\)才能实现乘法运算；

val=`expr $b / $a`;
echo "b / a : $val";

val=`expr $b % $a`;
echo "b % a : $val";
#如果未定地的变量使用，其结果返回的只是算数运算符

a=20
b=40
c=20
if [ $a == $c ]
then
echo "a=c"
fi

if [ $a != $b ]
then
echo "a!=b"
fi

#关系运算符
#关系运算符有 -eq -ne -gt -lt -ge -le

a=20
b=20
 if [ $a -eq $b ]
then
echo "a=b"
else
echo "a !=b "
fi

c=30
if [ $a -eq $c ]
then 
echo "a=c"
else
echo "a ！=c"
fi

#布尔运算符
#说明 ！ 非 -o 或 -a 与

echo "-----------------布尔运算——————————"
a=20
b=30
c=40

if [ ! $a -ne $b ]
then
echo "a 不等于b"
else
echo "a 等于 b"
fi

#逻辑运算符
:<<I
&& 表示and || 或者OR
I
a=30
b=40
c=60

if [[ $b -gt $a && $b -ne $c ]]
then
echo " b 大于a b不等于c "
fi
:<<ror
文件测试运算符
文件测试运算符用于检测 Unix 文件的各种属性。

属性检测描述如下：

操作符	说明	举例
-b file	检测文件是否是块设备文件，如果是，则返回 true。	[ -b $file ] 返回 false。
-c file	检测文件是否是字符设备文件，如果是，则返回 true。	[ -c $file ] 返回 false。
-d file	检测文件是否是目录，如果是，则返回 true。	[ -d $file ] 返回 false。
-f file	检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。	[ -f $file ] 返回 true。
-g file	检测文件是否设置了 SGID 位，如果是，则返回 true。	[ -g $file ] 返回 false。
-k file	检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。	[ -k $file ] 返回 false。
-p file	检测文件是否是有名管道，如果是，则返回 true。	[ -p $file ] 返回 false。
-u file	检测文件是否设置了 SUID 位，如果是，则返回 true。	[ -u $file ] 返回 false。
-r file	检测文件是否可读，如果是，则返回 true。	[ -r $file ] 返回 true。
-w file	检测文件是否可写，如果是，则返回 true。	[ -w $file ] 返回 true。
-x file	检测文件是否可执行，如果是，则返回 true。	[ -x $file ] 返回 true。
-s file	检测文件是否为空（文件大小是否大于0），不为空返回 true。	[ -s $file ] 返回 true。
-e file	检测文件（包括目录）是否存在，如果是，则返回 true。	[ -e $file ] 返回 true。
ror
echo "文件的简单测试"
file=`pwd`
file1="$file/test.sh"
echo "文件的路径为 $file1"
if [ -x $file1 ]
then
echo "$file1 文件有执行的权限"
fi

