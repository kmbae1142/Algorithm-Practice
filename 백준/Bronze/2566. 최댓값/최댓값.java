import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] arr = new int[9][9];
		int max = -1, i, j;
		
		for (i = 0; i < 9; i++) {
			for (j = 0; j < 9; j++) {
				arr[i][j] = sc.nextInt();
				if (arr[i][j] > max) {
					max = arr[i][j];
					Index.i = i + 1;
					Index.j = j + 1;
				}
			}
		}
		
		System.out.printf("%d\n%d %d", max, Index.i, Index.j);
	}
}

class Index {
	static int i;
	static int j;
}