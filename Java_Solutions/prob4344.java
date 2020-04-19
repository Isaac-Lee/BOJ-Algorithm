package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class prob4344 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		int cases = Integer.parseInt(in.readLine());
		for (int i = 0; i < cases; i++) {
			StringTokenizer st = new StringTokenizer(in.readLine());
			int n = Integer.parseInt(st.nextToken());
			int[] scores = new int[n];
			int total = 0;
			double m = 0, c = 0;
			for (int j = 0; j < n; j++) {
				scores[j] = Integer.parseInt(st.nextToken());
				total += scores[j];
			}
			m = total/n;
			for (int j = 0; j < n; j++) {
				if (scores[j] > m) {
					c += 1;
				} else {
					continue;
				}
			}
			System.out.println(String.format("%.3f%%", (c/n)*100));
		}
	}
}
