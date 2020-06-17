package BOJ_Solutios_Java;

import java.io.IOException;
import java.util.Scanner;

public class prob1300 {
    private static int n = 0;
    private static int k = 0;
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        k = scanner.nextInt();

        long left = 1;
        long right = k;

        System.out.println(bSearch(left, right));
    }

    private static long result = 0 ;
    private static long bSearch(long left, long right) {
        int cnt = 0;
        long mid = (left + right) / 2;
        if(left > right) return result;
        for(int i = 1; i <= n; i++) {
            cnt += Math.min(mid/i, n);
        }

        if(k <= cnt) {
            result = mid;
            return bSearch(left, mid -1);
        }else{
            return bSearch(mid + 1, right);
        }
    }
}