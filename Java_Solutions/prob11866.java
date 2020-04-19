package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class prob11866 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Queue<Integer> q = new LinkedList<>();
        StringBuilder sb = new StringBuilder();

        int N , K;
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            q.offer(i+1);
        }
        sb.append("<");
        for (int i = 0; i < N; i++) {
            for (int k = 1; k < K; k++) {
                q.offer(q.poll());
            }
            if (q.size() == 1) {
                sb.append(q.poll()+">");
                break;
            }
            sb.append(q.poll() + ", ");
        }
        System.out.println(sb.toString());
        br.close();
    }
}
