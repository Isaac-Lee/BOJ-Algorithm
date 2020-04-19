package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class prob9012 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(input.readLine());
		for (int i = 0; i < n; i++) {
			boolean isPal = true;
			int cnt = 0;
			String str = input.readLine();
			for (int j = 0; j < str.length(); j++) {
				if (str.charAt(j) == '(') {
					cnt ++;
				} else if (str.charAt(j) == ')') {
					cnt --;
					if (cnt < 0) {
						isPal = false;
						break;
					}
				}
			}
			
			if (isPal) {
				if (cnt > 0) {
					System.out.println("NO");
				} else {
					System.out.println("YES");
				}
			} else {
				System.out.println("NO");
			}
			
		}
	}
}
