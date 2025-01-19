import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
		int d = 0;
		
		while (x > 0) {
			if (x % 2 == 0) {
				d -= 2;
			}
			else {
				d += 3;
			}
			x--;
		}
		
		System.out.println(d);
		sc.close();
		
	}
}