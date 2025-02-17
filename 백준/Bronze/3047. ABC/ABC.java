import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[3];
		
		for (int i = 0; i < 3; i++) {
			arr[i] = sc.nextInt();
		}
		sc.nextLine();
		
		String[] str = sc.nextLine().trim().split("");
		
		Arrays.sort(arr);
		
		for (String s : str) {
			if (s.equals("A")) {
				System.out.printf("%s ", arr[0]);
			}
			else if (s.equals("B")) {
				System.out.printf("%s ", arr[1]);
			}
			else if (s.equals("C")) {
				System.out.printf("%s ", arr[2]);
			}
		}
		
		sc.close();
	}
}