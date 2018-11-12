import java.io.*;
/**
 * Write a description of class swap_without_third_variable here.
 *WAP to swap two numbers with using and without using third variable.
 * @author (REDDY)
 * @version (a version number or a date)
 */
public class swap_without_third_variable
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class swap_without_third_variable
     */
    public swap_without_third_variable()
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
    public int sampleMethod(int y)
    {
        // put your code here
        return x + y;
    }
    public static void main(String args[])throws IOException
    {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        System.out.println("enter a no:");
        int n1=Integer.parseInt(br.readLine());
        int n2=Integer.parseInt(br.readLine());
        System.out.println("n1="+n1+" n2="+n2);
        n1^=n2;
        n2^=n1;
        n1^=n2;
        System.out.println("n1="+n1+" n2="+n2);
    }
}
