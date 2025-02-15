import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		long[] arr = new long[N];
		long LCMnum = 0, sum = 0;
		
		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextLong();
		}
		
		LCMnum = arr[0];
		for (int i = 1; i < N; i++) {
			LCMnum = LCM(LCMnum, arr[i]);
		}
		
		
		for (long num : arr) {
			sum += LCMnum / num;
		}
		
		long rGCD = GCD(LCMnum, sum);
		System.out.printf("%d/%d", LCMnum / rGCD, sum / rGCD);
		sc.close();
		
	}
	
	public static long GCD(long a, long b) {
		while (b != 0) {
			long temp = a % b;
			a = b;
			b = temp;
		}
		
		return a;
	}
	
	public static long LCM(long a, long b) {
		return a * b / GCD(a, b);
	}
	
}