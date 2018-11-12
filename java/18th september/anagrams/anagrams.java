import java.io.*;
import java.util.*;
/**
 * Write a description of class anagrams here.
 *Write a Program in Java to input a word and print its anagrams.
Note: Anagrams are words made up of all the characters present in 
the original word by re-arranging the characters. 
Example: Anagrams of the word TOP are: TOP, TPO, OPT, OTP, PTO and POT.�
 * @author (your name)
 * @version (a version number or a date)
 */
public class anagrams
{
    // instance variables - replace the example below with your own
    private int x;
    /**
     * Constructor for objects of class anagrams
     */
    public anagrams()
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
    public static void sampleMethod(String str)
    {
        // put your code here
        for (int i =0;i<=str.length();i++)
        {
            
        }
    }
    public static void main(String []args)throws IOException
    {
        Scanner sc =new Scanner (System.in);
        System.out.println("enter a string :");
        String str=(sc.nextLine());
        System.out.println();
        sampleMethod(str);
    }
}
