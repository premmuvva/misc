import java.util.Scanner;
class diagonal
{
	public static void main(String[]args)
	{
		Scanner in=new Scanner(System.in);
		int m,n;
		System.out.println("enter the no of rows and columns");
		m=in.nextInt();
		n=in.nextInt();
		int[][] a=new int[m][n];
		
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			{
				a[i][j]=in.nextInt();
			}
		}
		System.out.println("The Primary Diagonal is:");
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(i==j)
				{
				System.out.println(a[i][j]);
				}
				
			}
		}
		System.out.println("The Secondary Diagonal is:");
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			{
				int k=n-i-1;
				if(k==j)
				{
				System.out.println(a[i][j]);
				}
				System.out.println(" ");
			}
		}
		
		
		
		
	}
}	
		
		
		
		
		