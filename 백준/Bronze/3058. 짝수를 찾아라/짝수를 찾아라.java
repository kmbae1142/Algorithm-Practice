import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for (int i = 0; i < T; i++) {
			int min = 101;
			int sum = 0;
			for (int j = 0; j < 7; j++) {
				int num = sc.nextInt();
				if (num % 2 == 0) {
					sum += num;
					if (min > num) {
						min = num;
					}
				}
			}
			System.out.printf("%d %d\n", sum, min);
		}
		
		sc.close();
		
	}
}