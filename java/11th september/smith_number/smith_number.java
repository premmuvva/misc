import java.io.*;
/**
 * Write a description of class Primorial_of_number here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class smith_number
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class Primorial_of_number
     */
    public smith_number()
    {
        // initialise instance variables
        x = 0;
    }

    /**
     * WAP to check whether an input number is smith or not?
Where smith number is a composite number, the sum of whose digits is the sum of the prime
factors obtained as a result of prime factorization (excluding 1). The first few numbers are
4,22, 27,58…
Example: a. 666 Prime factors are 2,3,3 and 37 Sum of the digits are (6+6+6) = 18. Sum of
the digits of the factors (2 + 3 + 3 + (3 + 7)) = 18. So 666 is the Smith Number.
     */
    public static boolean sampleMethod(int y)
    {
        // put your code here
        boolean check[]=new boolean [y+1];
        for (int i=2;i<y;i++)
            check[i]=true;
        for (int i =2 ;i<(y+1)/2;i++){
            if (check[i]==true)
                for (int j=2;i*j<y+1;j++)
                    check[i*j]=false;
        }
        int sum=0,sum1=0;
        for (int i=0;i<y;i++){
            if (check[i]==true){
                int temp1=y;
                while(temp1%i==0){
                    int temp=i;
                    while(temp>0){
                        sum+=temp%10;
                        temp/=10;
                    }
                    temp1/=i;
                }
            }
        }
        int temp=y;
        while(temp>0){
            sum1+=temp%10;
            temp/=10;
        }
        return sum==sum1?  true : false ;
    }
    public static void main(String []args)throws IOException
    {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        System.out.println("enter a no:");
        int n=Integer.parseInt(br.readLine());
        System.out.println(sampleMethod(n));
    }
}
