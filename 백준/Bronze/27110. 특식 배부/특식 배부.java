import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[3];
		int n = sc.nextInt();
		int sum = 0;
		
		for (int i = 0; i < 3; i++) {
			arr[i] = sc.nextInt();
			if (arr[i] <= n) {
				sum += arr[i];
			}
			else {
				sum += n;
			}
		}
		
		System.out.println(sum);
		sc.close();
		
	}
}