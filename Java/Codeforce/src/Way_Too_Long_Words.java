import java.util.Scanner;
public class Way_Too_Long_Words {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);


        int n = input.nextInt();
        for (int i = 0; i<n ; i++){
            String s = input.next();
            if(s.length() >= 11){
                System.out.println(s.charAt(0)+""+(s.length()-2)+""+s.charAt(s.length()-1));
            }else {
                System.out.println(s);
            }
            }
//abcdefghikkk
//a9k




    }
}
