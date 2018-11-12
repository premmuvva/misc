import java.io.*;
import java.util.Arrays;
/**
 * Write a description of class transpose_of_a_matrix here.
 *WAP to find transpose of a matrix.
 * @author (your name)
 * @version (a version number or a date)
 */
public class transpose_of_a_matrix
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class transpose_of_a_matrix
     */
    public transpose_of_a_matrix()
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
    public static int[][] sampleMethod(int[][] y,int r ,int c)
    {
        // put your code here
        int ar[][]=new int [c][r];
        for (int i =0;i<c;i++)
        {
            for (int j=0;j<r;j++)
            {
                ar[i][j]=y[j][i];
            }
        }
        return ar;
    }
    public static void main(String args[])throws IOException
    {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        System.out.println("enter a row and column size:");
        int r=Integer.parseInt(br.readLine());
        int c=Integer.parseInt(br.readLine());
        int matrix[][]=new int [r][c];
        System.out.println("enter elements row wise");
        for (int i =0;i<r;i++)
        {
            for (int j=0;j<c;j++)
            {
                matrix[i][j]=Integer.parseInt(br.readLine());
            }
        }
        //System.out.println(Arrays.toString(sampleMethod(matrix,r,c)));
        System.out.println("orginal_matrix:");
        for (int i =0;i<r;i++)
        {
            for (int j=0;j<c;j++)
            {
                System.out.print(matrix[i][j]+" " );
            }
            System.out.println();
        }
        System.out.println("inverse_matrix:");
        int inverse_matrix[][]=sampleMethod(matrix,r,c);
        for (int i =0;i<c;i++)
        {
            for (int j=0;j<r;j++)
            {
                System.out.print(inverse_matrix[i][j]+" " );
            }
            System.out.println();
        }
    }
}
