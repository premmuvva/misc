import java.io.*;
/**
 * Write a description of class sum_of_largest_and_smallest_number_in_array
 * here.
 *WAP to find sum of the digits of the largest and smallest number 
 *present in the array of size m x n.�
 * @author (your name)
 * @version (a version number or a date)
 */
public class sum_of_largest_and_smallest_number_in_array
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class sum_of_largest_and_smallest_number_in_array
     */
    public sum_of_largest_and_smallest_number_in_array()
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
    public static int sampleMethod(int[][] y,int r ,int c)
    {
        // put your code here
        int smallest=y[0][0],largest=y[0][0];
        for (int i =0;i<r;i++)
        {
            for (int j=0;j<c;j++)
            {
                if(y[i][j]<smallest)
                    smallest=y[i][j];
                if (y[i][j]>largest)
                    largest=y[i][j];
            }
        }
        return smallest+largest;
    }
    public static void main(String args[])throws IOException
    {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        System.out.println("enter a row and coloumn:");
        int r=Integer.parseInt(br.readLine());
        int c=Integer.parseInt(br.readLine());
        int matrix[][]=new int [r][c];
        System.out.println("enter elements row wise:");
        for (int i =0;i<r;i++)
        {
            for (int j=0;j<c;j++)
            {
                matrix[i][j]=Integer.parseInt(br.readLine());
            }
        }
        //System.out.println(Arrays.toString(sampleMethod(matrix,r,c)));
        int sum=sampleMethod(matrix,r,c);
        System.out.print("sum=" +sum);
    }
}
