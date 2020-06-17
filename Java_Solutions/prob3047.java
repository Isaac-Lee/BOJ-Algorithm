package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class prob3047 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[3];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 3; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        String order = br.readLine();
        for (int i = 0; i < 3; i++) {
            char c = order.charAt(i);
            if (c == 'A') {
                System.out.print(arr[0]+" ");
            } else if (c == 'B') {
                System.out.print(arr[1]+" ");
            } else if (c == 'C') {
                System.out.print(arr[2]+" ");
            }
        }
    }
}
