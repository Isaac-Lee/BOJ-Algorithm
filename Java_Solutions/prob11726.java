package BOJ_Solutios_Java;

import java.util.Scanner;

public class prob11726 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // int N = sc.nextInt();

        for (int N = 1; N < 1001; N++) {
            int tmp1 = 1;
            int tmp2 = 2;
            int answer = 0;

            if (N == 1) {
                System.out.println(1);
            } else if (N == 2) {
                System.out.println(2);
            } else {
                for (int i = 3; i < N+1; i++) {
                    answer = tmp1 + tmp2;
                    tmp1 = tmp2;
                    tmp2 = answer;
                }

                // for Test
                if (answer < 0) {
                    System.out.println(String.format("n = %d, answer = %d", N, answer%10007));
                }

                // System.out.println(answer - (answer/10007));
            }
        }
    }
}
