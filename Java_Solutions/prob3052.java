package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class prob3052 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        
		int[] left = new int[42];
		int c = 0;
		for (int i = 0; i < 10; i ++) {
			left[Integer.parseInt(in.readLine())%42] += 1;
		}
		
		for (int i = 0; i < 42; i ++) {
			
			if (left[i] == 0) {
				continue;
			} else {
				c++;
			}
		}
		System.out.println(c);
	}
}
