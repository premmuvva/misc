import java.io.*;
class op{
	public static int area(int a){
		return a*a;
	}
	public static int area(int a , int b){
		return a*b;
	}
	public static double area (float a){
		return 3.14*a*a;
	}
	public static void main(String args[])throws IOException{
		int a,b,o;
		float c;
		BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
		System.out.println("enter 1 for finding area of square 2for rectangle and 3 for circle");
		o=Integer.parseInt(br.readLine());
		switch(o){
			case 1:
			a=Integer.parseInt(br.readLine());
			System.out.println(area(a));
			break;
			case 2:
			a=Integer.parseInt(br.readLine());
			b=Integer.parseInt(br.readLine());
			System.out.println(area(a,b));
			break;
			case 3:
			c=Float.parseFloat(br.readLine);
			System.out.println(area(c));
			break;
			default:
			System.out.println ("wrong choice !!!");
		}
	}
}