class countobj
{
	static int c=0;
	public countobj()
	{
		c++;
	}
	public countobj(int a)
	{
		c++;
	}
	public countobj(float a)
	{
		c++;
	}
	public static void main(String args[])
	{
		countobj obj=new countobj();
		countobj obj1=new countobj(5);
		countobj obj2=new countobj(2.5f);
		System.out.println(c);
	}
}	