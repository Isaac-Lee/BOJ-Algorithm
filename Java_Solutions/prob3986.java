package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class prob3986 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		
		int answer = 0;
		int n = Integer.parseInt(input.readLine());
		for (int i = 0; i < n; i++) {
			String str = input.readLine();
			Stack<Character> s = new Stack<Character>();
			
			for (int j = 0; j < str.length(); j++) {
				if (!s.empty() && s.peek() == str.charAt(j)) {
					s.pop();
				} else {
					s.push(str.charAt(j));
				}
			}
			if (s.size() == 0) {
				answer ++;
			}
		}
		System.out.println(answer);
	}
}
