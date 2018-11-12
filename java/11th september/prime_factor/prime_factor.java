import java.io.*;
/**
 * Write a description of class Primorial_of_number here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class prime_factor
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class Primorial_of_number
     */
    public prime_factor()
    {
        // initialise instance variables
        x = 0;
    }

    /**
     * WAP to print prime factors of a number.
    */
    public static void sampleMethod(int y)
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
        int sum=0;
        for (int i=0;i<y;i++){
            if (check[i]==true){
                int temp1=y;
                while(temp1%i==0){
                    System.out.println(i);
                    temp1/=i;
                }
            }
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
