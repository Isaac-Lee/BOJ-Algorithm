package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class prob11279 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Number> pq = new PriorityQueue<>();

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++){
            int order = Integer.parseInt(br.readLine());
            if (order > 0) {
                pq.offer(new Number(order));
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
class Number implements Comparable{
    int n;

    public Number(int n) {
        this.n = n;
    }

    @Override
    public int compareTo(Object target) {
        Number t = (Number) target;
        if (t.n > this.n) {
            return 1;
        } else if (t.n < this.n) {
            return -1;
        }
        return 0;
    }

    public String toString() {
        return Integer.toString(this.n);
    }
}

