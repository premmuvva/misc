import java.io.*;
class multi
{
	public static void main(String args[])throws IOException
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int a[][]=new int [3][3];
		int b[][]=new int [3][3];
		int c[][]=new int [3][3];
		for (int i=0;i<3;i++)
		{
			for (int j=0;j<3;j++)
			{
				System.out.println("enter a element for a matrix");
				a[i][j]=Integer.parseInt(br.readLine());
				System.out.println("enter a element for b matrix");
				b[i][j]=Integer.parseInt(br.readLine());
			}
		}
		for (int k=0;k<3;k++)
		{
			for (int l=0;l<3;l++)
			{
				for (int m=0;m<3;m++)
				{
					c[k][l]+=a[k][m]*b[m][l];
				}
			}
		}
		for (int x=0;x<3;x++)
		{
			for (int y=0;y<3;y++)
			{
				System.out.print(c[x][y]+" ");
			}
			System.out.println();
		}
	}
}