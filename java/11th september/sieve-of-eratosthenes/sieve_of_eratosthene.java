import java.io.*;
/**
 * Write a description of class sieve_of_eratosthene here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class sieve_of_eratosthene
{
    // instance variables - replace the example below with your own
    private int x;
    /**
     * Constructor for objects of class sieve_of_eratosthene
     */
    public sieve_of_eratosthene()
    {
        // initialise instance variables
        x = 0;
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public static void sampleMethod(int y)//seive of eratosthenes
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
        for (int i=0;i<y;i++){
            if (check[i]==true)
                System.out.println(i);
        }
    }
    public static void main(String []args)throws IOException
    {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        System.out.println("enter a no:");
        int n=Integer.parseInt(br.readLine());
        sampleMethod(n);
    }
}
