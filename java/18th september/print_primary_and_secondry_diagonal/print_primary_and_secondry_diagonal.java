import java.util.*;
import java.io.*;
/**
 * Write a description of class print_primary_and_secondry_diagonal here.
 *WAP to print primary and secondry diagonal of a square matrix.�
 * @author (your name)
 * @version (a version number or a date)
 */
public class print_primary_and_secondry_diagonal
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class print_primary_and_secondry_diagonal
     */
    public print_primary_and_secondry_diagonal()
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
        System.out.println("enter order of square matrix:");
        int r=Integer.parseInt(br.readLine());
        int matrix[][]=new int [r][r];
        System.out.println("enter elements of square matrix:");
        for (int i =0;i<r;i++)
        {
            for (int j=0;j<r;j++)
            {
                matrix[i][j]=Integer.parseInt(br.readLine());
            }
        }
        //System.out.println(Arrays.toString(sampleMethod(matrix,r,c)));
        int sum=sampleMethod(matrix,r,c);
        
    }
}
