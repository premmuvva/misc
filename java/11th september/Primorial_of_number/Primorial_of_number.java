import java.io.*;
/**
 * Write a description of class Primorial_of_number here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Primorial_of_number
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class Primorial_of_number
     */
    public Primorial_of_number()
    {
        // initialise instance variables
        x = 0;
    }

    /**
     * WAP to find Primorial of a number.
Primorial is defined as the product of prime numbers less than or equal to that number. e.g.
Primorial of 6 will be 2*3*5 = 30.

     */
    public static long sampleMethod(int y)
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
        long primodal=1;
        for (int i=0;i<y;i++){
            if (check[i]==true)
                primodal*=i;
        }
        return primodal;
    }
    public static void main(String []args)throws IOException
    {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        System.out.println("enter a no:");
        int n=Integer.parseInt(br.readLine());
        System.out.println(sampleMethod(n));
    }
}
