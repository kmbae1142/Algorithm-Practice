import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int num = Integer.parseInt(br.readLine());
		String s = "";
		
		for (int i = 0; i < num; i++) {
			String temp = br.readLine();
			if (temp.contains("S")) {
				s = temp;
				break;
			}
		}
		
		bw.write(s + "\n");
		
		bw.close();
		br.close();
	}
	
}