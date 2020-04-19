package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class prob8958 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		int cases = Integer.parseInt(in.readLine());
		for (int i = 0; i < cases; i++) {
			int score = 0, total = 0;
			String answer = in.readLine();
			for (int j = 0; j < answer.length(); j++) {
				if (answer.charAt(j) == 'O') {
					score += 1;
					total += score;
				} else if (answer.charAt(j) == 'X'){
					score = 0;
				}
			}
			System.out.println(total);
		}
	}
}
