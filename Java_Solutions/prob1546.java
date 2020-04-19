package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class prob1546 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(in.readLine());
		
		StringTokenizer st = new StringTokenizer(in.readLine());
		
		double[] score = new double[n];
		double max = 0;
		double total = 0;
		for (int i = 0; i < n; i++) {
			score[i] = Integer.parseInt(st.nextToken());
			max = Math.max(score[i], max);
			
		}
		for (int i = 0; i < n; i++) {
			score[i] = (score[i]/max)*100;
			total += score[i];
			
		}
		
		System.out.println(total/n);
		
	}

}
