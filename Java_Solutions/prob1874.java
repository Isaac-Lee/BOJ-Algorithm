package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class prob1874 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(input.readLine());

		int i, temp, max = 0;
		Stack<Integer> s = new Stack<>();
		StringBuilder answer = new StringBuilder();

		while (n-- > 0) {
			temp = Integer.parseInt(input.readLine());

			if (temp > max) {
				for (i = max+1; i < temp+1; i++) {
					s.push(i);
					answer.append("+");
				}
				max = temp;
			} else if (s.peek() != temp) {
				System.out.println("NO");
				return;
			}
			s.pop();
			answer.append("-");
		}
		for (i = 0; i < answer.length(); i++) {
			System.out.println(answer.charAt(i));
		}

	}
}
