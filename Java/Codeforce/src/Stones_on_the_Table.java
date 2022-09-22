import java.util.Scanner;
public class Stones_on_the_Table {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        String s = input.next();
        int x = 0;
        for(int i= 0; i<n-1;i++){
            if (s.charAt(i) == s.charAt(i+1)){
                x += 1;
            }
        }
        System.out.println(x);



    }
}
