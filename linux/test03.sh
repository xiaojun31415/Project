#bin/bash
#this is a sample test
#read hh
#echo "the input : $hh"

echo -e "OK! \n" 
# -e 开启转义
echo "It is a test"
echo -e "OK! \c" # -e 开启转义 \c 不换行
echo "It is a test" > input.txt

printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg  
printf "%-10s %-8s %-4.2f\n" 郭靖 男 66.1234 
printf "%-10s %-8s %-4.2f\n" 杨过 男 48.6543 
printf "%-10s %-8s %-4.2f\n" 郭芙 女 47.9876 

for loop in 1 2 3 4
do
echo "this is sample circult: $loop"
done

#循环的关键字有3个 for while until
#注意for的特殊格式for (( ; ; ))

#注意case语句的格式
:<<com
case 值 in
模式1)
    command1
    command2
    ...
    commandN
    ;;
模式2）
    command1
    command2
    ...
    commandN
    ;;
esac
com
echo '输入 1 到 4 之间的数字:'
echo '你输入的数字为:'
read aNum
case $aNum in
    1)  echo '你选择了 1'
    ;;
    2)  echo '你选择了 2'
    ;;
    3)  echo '你选择了 3'
    ;;
    4)  echo '你选择了 4'
    ;;
    *)  echo '你没有输入 1 到 4 之间的数字'
    ;;
esac
function hello(){
echo "函数开始执行"
ss=1
sd=2
return $(( $ss +$sd))
}

hello
echo "最后的结果$?"
