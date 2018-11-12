import java.io.*;
class office{
    int empno,salary;
    String empname ;
    public  void getvalue()throws IOException{
      BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
      System.out.println("enter employee no:");
      empno=Integer.parseInt(br.readLine());
      System.out.println("enter employee salary:");
      salary=Integer.parseInt(br.readLine());
      System.out.println("enter employee name:");
      empname=br.readLine();
   }
}
class teaching extends office{
  String designation;
   public  void setvalue()throws IOException{
    BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
      System.out.println("enter designation:");
      designation=br.readLine();
    }
}
class non_teaching extends office{
  String designation;
   public void setvalue()throws IOException{
    BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
      System.out.println("enter designation:");
      designation=br.readLine();
    }
}
class edu_hier{
  public static void main(String args[])throws IOException{
     teaching obj1 = new teaching();
     office obj2 = new office();
     obj1.setvalue();
     obj2.getvalue();
  }
}