public class Pyramid{
    public static void printStars(int n){
        int i, j;
        for(i=0; i<n; i++){
            for(j=0; j<=5-i; j++)
                System.out.print("  ");
            for(j=0; j<=2*i; j++)
                System.out.print("* ");
            System.out.println();
        }
   }
    public static void main(String args[]){
        int n = 5;
        printStars(n);
    }
}