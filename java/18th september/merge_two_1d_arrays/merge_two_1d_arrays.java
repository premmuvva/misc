import java.io.*;
/**
 * Write a description of class merge_two_1d_arrays here.
 *WAP a program to merge two single dimensional array 
 *of size m and p respectively�
 * @author (your name)
 * @version (a version number or a date)
 */
public class merge_two_1d_arrays
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class merge_two_1d_arrays
     */
    public merge_two_1d_arrays()
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
    public static int[] sampleMethod(int x[],int y[],int m,int p)
    {
        // put your code here
        int z[]=new int [m+p];
        for (int i =0;i<m;i++)
        {
            z[i]=x[i];
        }
        for (int i =0;i<p;i++)
        {
            z[i+m]=y[i];
        }
        return z;
    }
    public static void main(String args[])throws IOException
    {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        System.out.println("enter sizes m and p of two arrays:");
        int m=Integer.parseInt(br.readLine());
        int p=Integer.parseInt(br.readLine());
        int matrix1[]=new int [m];
        int matrix2[]=new int [p];
        System.out.println("enter elements of matrix1");
        for (int i =0;i<m;i++)
        {
            matrix1[i]=Integer.parseInt(br.readLine());
        }
        System.out.println("enter elements of matrix2");
        for (int i =0;i<p;i++)
        {
            matrix2[i]=Integer.parseInt(br.readLine());
        }
        int merged_matrix[]=sampleMethod(matrix1,matrix2,m,p);
        for (int i =0;i<m+p;i++)
        {
            System.out.print(merged_matrix[i]+" ");
        }
    }
}
