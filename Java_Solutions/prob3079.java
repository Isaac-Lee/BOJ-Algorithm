package BOJ_Solutios_Java;

import java.io.*;
import java.util.*;

public class prob3079 {

    static long n, m;
    static long[] time;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Long.parseLong(st.nextToken());
        m = Long.parseLong(st.nextToken());

        time = new long[(int) n];

        for (int i = 0; i < n; i++) {
            time[i] = Long.parseLong(br.readLine());
        }
        binarySearch();
    }

    private static void binarySearch() {
        long left = 1;
        long right = 1000000000000000000L;
        long result = right;
        long mid = 0;

        while (left <= right) {
            mid = (left + right) / 2;

            if (isPossible(mid)) {
                result = Math.min(result, mid);
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        System.out.println(result);
    }

    private static boolean isPossible(long t) {
        long temp = 0;
        for (int i = 0; i < n; i++) {
            temp += t / time[i];
        }
        return temp >= m;
    }
}