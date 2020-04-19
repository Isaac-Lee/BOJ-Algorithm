package BOJ_Solutios_Java;

import java.io.*;
import java.util.*;

public class prob10818 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            int tmp = Integer.parseInt(st.nextToken());
            min = Math.min(min, tmp);
            max = Math.max(max, tmp);
        }
        bw.write(min + " " + max + "\n");
        bw.close();
    }
}