import java.io.*; 
  
interface in1 
{ 
    final int a = 10; 
    void display(); 
} 
  
class test implements in1 
{ 
    public void display() 
    { 
        System.out.println("Geek"); 
    } 
  
    public static void main (String[] args) 
    { 
        testClass t = new testClass(); 
        t.display(); 
        System.out.println(a); 
    } 
} 