//75. WAP to check whether a given number is binary or not?
import java.io.*;
import java.util.*;
class 75_binary_or_not{
    public static void main(String args[])throws IOException{
        Scanner input = new Scanner (System.in);
        System.out.println("Enter the binary number that is to be checked : ");
        String n = input.nextLine();
        int i ;
        for(i=0;i<n.length();i++)
            if (n[i]!='0'&&n[i]!='1')
            break;
        if (i<n.length())
        System.out.println("it is not a binary number ");
        else
        System.out.println("it is not a binary number ");
    }
}