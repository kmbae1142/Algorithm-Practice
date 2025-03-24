import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		int[][] arr = new int[100][100];
		int sum = 0;
		
		int num = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < num; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			arrFill(arr, A, B);
		}
		
		for (int i = 0; i < 100; i++) {
			for (int j = 0; j < 100; j++) {
				if (arr[i][j] == 1)
					sum += 1;
			}
		}
		
		bw.write(sum + "\n");
		bw.close();
		br.close();
	}
	
	private static void arrFill(int[][] arr, int A, int B) {
		for (int i = A; i < A + 10; i++) {
			for (int j = B; j < B + 10; j++) {
				arr[i][j] = 1;
			}
		}
	}
}