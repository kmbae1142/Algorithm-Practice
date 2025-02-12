import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[][] pos = new long[N + 1][2];
		long sum = 0;
		
		for (int i = 0; i < N; i++) {
			pos[i][0] = sc.nextLong();
			pos[i][1] = sc.nextLong();
		}
		
		pos[N][0] = pos[0][0];
		pos[N][1] = pos[0][1];
		
		for (int i = 0; i < N; i++) {
			sum += pos[i][0] * pos[i + 1][1] - pos[i + 1][0] * pos[i][1];
		}
		
		System.out.printf("%.1f", Math.abs(sum) * 0.5);
		sc.close();
		
	}
}