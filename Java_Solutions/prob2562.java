package BOJ_Solutios_Java;

import java.io.*;

public class prob2562 {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int[] num = new int[9];
        int count = 0;
        int max = 0;
        for(int i=0; i<num.length; i++) {
            num[i] = Integer.valueOf(in.readLine());
            if(num[i] > 99)
                System.exit(0);
        }

        for(int i=0; i<num.length; i++) {
            if(num[i] > max) {
                max = num[i];
                count = i+1;
            }
        }

        System.out.println(max);
        System.out.println(count);

    }
}