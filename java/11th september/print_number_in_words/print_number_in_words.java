import java.io.*;
/**
 * Write a description of class print_number_in_words here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class print_number_in_words
{
    // instance variables - replace the example below with your own
    private int x;
    String number[];
    /**
     * Constructor for objects of class print_number_in_words
     */
    public print_number_in_words()
    {
        // initialise instance variables
        x = 0;
        number=new String [] {"zero ","one ","two ","three ","four ","five ","six ","seven ","eight ", "nine "};
    }

    /**
     * printing 54 as "five four"
     */
    public static  void sampleMethod(int y)
    {
        // put your code here
        if (y==0)
            return;
        sampleMethod(y/10);
        print_number_in_words temp=new print_number_in_words();
        System.out.print(temp.number[y%10]);
    }
    public static void main(String []args) throws IOException
    {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        System.out.println("enter a no:");
        int n=Integer.parseInt(br.readLine());
        sampleMethod(n);
    }
        
}
