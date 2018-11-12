import java.util.*;
/**
 * Write a description of class determinant_of_matrix here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class invertibility_of_matrix
{
    // instance variables - replace the example below with your own
    private int x;

    /**
     * Constructor for objects of class determinant_of_matrix
     */
    public invertibility_of_matrix()
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
    public static double determinant(double A[][],int N)
    {
        double det=0;
        if(N == 1)
        {
            det = A[0][0];
        }
        else if (N == 2)
        {
            det = A[0][0]*A[1][1] - A[1][0]*A[0][1];
        }
        else
        {
            det=0;
            for(int j1=0;j1<N;j1++)
            {
                double[][] m = new double[N-1][];
                for(int k=0;k<(N-1);k++)
                {
                    m[k] = new double[N-1];
                }
                for(int i=1;i<N;i++)
                {
                    int j2=0;
                    for(int j=0;j<N;j++)
                    {
                        if(j == j1)
                            continue;
                        m[i-1][j2] = A[i][j];
                        j2++;
                    }
                }
                det += Math.pow(-1.0,1.0+j1+1.0)* A[0][j1] * determinant(m,N-1);
            }
        }
        return det;
    }
 
    public static void main(String args[])
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the order of the square matrix");
        int n = input.nextInt();
 
        System.out.println("Enter the elements of the square matrix");
        double[][] mat = new double[n][n];
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
            {
                mat[i][j] = input.nextDouble();
            }
        } 
        if(determinant(mat, n) == 0)
        {
            System.out.println("Matrix is not Invertible, as the determinant is : "+determinant(mat, n));
        }
        else
        {
            System.out.println("Matrix is Invertible, as the determinant is : "+determinant(mat, n));
        }
	}
}
