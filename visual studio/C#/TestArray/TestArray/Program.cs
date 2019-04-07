using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Test;
namespace TestArray
{
    class Program
    {
        static void Main(string[] args)
        {
            testA a = new testA();
            a.myArray = new int [3]{ 1, 3, 4 };
            a.fun(a.myArray);
            TestB c = new TestB();
            c.fun();

        }
    }
 
}
namespace Test
{
    class testA
    {
        public int[] myArray;


       public void fun(int[] myArray)
        {
            foreach(int val in myArray)
            {
                Console.WriteLine(val);
            }
        }
        
        


    }
}
