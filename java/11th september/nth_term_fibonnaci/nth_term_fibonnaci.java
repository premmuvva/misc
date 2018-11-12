import java.io.*;
/**
 * Write a description of class nth_term_fibonnaci here.
 *WAP to print nth term of the Fibonacci series and also print the 
 *prime numbers present in the Fibonacci series.
 * @author (your name)
 * @version (a version number or a date)
 */
public class nth_term_fibonnaci
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class nth_term_fibonnaci
     */
    public nth_term_fibonnaci()
    {
        // initialise instance variables
        x = 0;
    }
    public static boolean isPrime(int n)
    {
        int i;
        for (i=2;i*i<=n;i++)
            if(n%i==0)
                break;
        if(i*i<=n||n==1)
            return false;
        return true;
    }
    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public static int sampleMethod(int y)
    {
        // put your code here
        if (y==0)
            return 0;
        if(y==1)
            return 1;
        return sampleMethod(y-1)+sampleMethod(y-2);
    }
    public static void main(String []args)throws IOException
    {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        System.out.println("enter a no:");
        int n=Integer.parseInt(br.readLine());
        System.out.println(sampleMethod(n));
        for (int i =1;i<=n;i++)
        {
            int fib=sampleMethod(i);
            if(isPrime(fib))
                System.out.println(fib);
        }
    }
}
