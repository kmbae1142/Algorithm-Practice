import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String A = sc.next();
		String B = sc.next();
		
		if (A.equals("null")) {
			A = null;
		}
        
        if (B.equals("null")) {
			B = null;
		}
		
		try {
			System.out.println(A.equals(B));
		}
		catch (NullPointerException e){
			System.out.println("NullPointerException");
		}
		
		try {
			System.out.println(A.equalsIgnoreCase(B));
		}
		catch (NullPointerException e){
			System.out.println("NullPointerException");
		}
		
	}
}