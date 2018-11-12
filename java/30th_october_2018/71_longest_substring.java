//71. WAP to find longest substring without repeating characters
import java.io.*;
import java.util.*;
String longest_substring_without_repeating(String str,int n){
    if(n==str.len())
    return str;
    if(str.indexOf(str[n],n+1)<0)
    return longest_substring_without_repeating(str,n+1);
    if(len(longest_substring_without_repeating(str.subSeqence(0,str.indexOf()),n+1)))
}
class 71_longest_substring{
    public static void main(String args[])throws IOException{
        Scanner input = new Scanner (System.in);
        System.out.println("Enter the string : ");
        String n = input.nextLine();
        System.out.println(longest_substring_without_repeating(n,0));
        }
    }
}