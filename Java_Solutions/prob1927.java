package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class prob1927 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++){
            int order = Integer.parseInt(br.readLine());
            if (order > 0) {
                pq.offer(order);
            } else {
                if (pq.size() == 0) {
                    System.out.println(0);
                } else {
                    System.out.println(pq.poll());
                }

            }
        }
    }
}
