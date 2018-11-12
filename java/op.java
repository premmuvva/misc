import java.io.*;
class op{
	public static void main(String args[]){
		int a,b=135;
		BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
		a=Integer.parseInt(br.readLine());
		System.out.printf("sum : %d",a+b);
		System.out.printf("difference : %d",a-b);
		System.out.printf("product : %d",a*b);
		System.out.printf("divide : %d",a/b);
	}
}