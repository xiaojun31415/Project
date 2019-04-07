using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
/*
 * project :Calculator 
 * function :  calculator sample operation 
 * 
 *
 */
namespace calc
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                CCount count = new CCount();
                Console.Write("please input first number:\n");
                int a = Convert.ToInt32(Console.ReadLine());
                Console.Write("请输入运算法则：\n");
                string type = Console.ReadLine();
                Console.Write("please input second number:\n");
                int b = Convert.ToInt32(Console.ReadLine());
                int c = count.Result(a, b, type);
                Console.WriteLine("the result is : " + c);

                Console.Clear();
                
               
            }
        }

    }

    public class CCount{
        public int Result(int a,int b,string type)
        {
            switch (type)
            {
                case "+":
                    return a + b; break;
                case "-":
                    return a - b;break;
                case "*":
                    return a * b; break;
                case "/":
                    return a / b; break;
                default:
                    return 0; break;
            }

        }
    }
}
