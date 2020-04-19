package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class prob10828 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		
		Stack<Integer> s = new Stack<Integer>();
		
		int n = Integer.parseInt(input.readLine());
		for(int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(input.readLine());
			
			String order = st.nextToken();
			if (order.equals("push")) {
				s.push(Integer.parseInt(st.nextToken()));
			} else if (order.equals("top")) {
				if (s.empty()) {
					System.out.println(-1);
				} else {
					System.out.println(s.peek());
				}
			} else if (order.equals("pop")) {
				if (s.empty()) {
					System.out.println(-1);
				} else {
					System.out.println(s.pop());
				}
			} else if (order.equals("size")) {
				System.out.println(s.size());
			} else if (order.equals("empty")) {
				if (s.empty()) {
					System.out.println(1);
				} else {
					System.out.println(0);
				}
			}
		}
	}
}
