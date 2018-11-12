import java.io.*;
import java.util.*;
/**
 * Write a description of class print_matrix_in_spiral here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class print_matrix_in_spiral
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class print_matrix_in_spiral
     */
    public print_matrix_in_spiral()
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
    public static void main(String[] args) throws IOException
   {
        Scanner ob = new Scanner(System.in);
        System.out.println("Enter the Number of rows and columns");
        int m = ob.nextInt();
        int n = ob.nextInt();
        int i, k = 0, l = 0;
        int a[][]=new int [m][n];
        for (i=0;i<m;i++)
        {
            for (int j=0;j<n;j++)
            {
                a[i][j]=ob.nextInt();
            }
        }
        while (k < m && l < n)
        {
            for (i = l; i < n; ++i)
            {
                System.out.print(a[k][i]+" ");
            }
            k++;
            for (i = k; i < m; ++i)
            {
                System.out.print(a[i][n-1]+" ");
            }
            n--;
            if ( k < m)
            {
                for (i = n-1; i >= l; --i)
                {
                    System.out.print(a[m-1][i]+" ");
                }
                m--;
            }
            if (l < n)
            {
                for (i = m-1; i >= k; --i)
                {
                    System.out.print(a[i][l]+" ");
                }
                l++;    
            }        
        }
    }
}
