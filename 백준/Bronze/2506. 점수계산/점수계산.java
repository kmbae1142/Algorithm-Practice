import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int count = 0, sum = 0, prob;
		
		for (int i = 0; i < N; i++) {
			prob = sc.nextInt();
			if (prob == 1) {
				count++;
				sum += count;
			}
			else {
				count = 0;
			}
		}
		
		System.out.println(sum);
		sc.close();
		
	}
}