import java.io.*;
/**
 * Write a description of class factorial_of_table here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class factorial_of_table
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class factorial_of_table
     */
    public factorial_of_table()
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
    public static long  sampleMethod(int y)
    {
        // put your code here
        if (y==1)
            return 1;
        return y*sampleMethod(y-1);
    }
    public static void main(String []args)throws IOException
    {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        System.out.println("enter a no:");
        int n=Integer.parseInt(br.readLine());
        for (int i=1;i<=5;i++){
            System.out.println(sampleMethod(i*n));
        }
    }
}
