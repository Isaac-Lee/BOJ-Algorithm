package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.EmptyStackException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class prob18258 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        Queue<Integer> q = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String oper = st.nextToken();

            if (oper.equals("push")) {
                int k = Integer.parseInt(st.nextToken());
                q.offer(k);
            } else if (oper.equals("pop")) {
                System.out.println(q.poll());
            } else if (oper.equals("size")) {
                System.out.println(q.size());
            } else if (oper.equals("empty")) {
                int Empty = 0;
                if (q.isEmpty()) {
                    Empty = 1;
                }
                System.out.println(Empty);
            } else if (oper.equals("front")) {
                if (q.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(q.peek());

                }
            } else if (oper.equals("back")) {
                if (q.isEmpty()) {
                    System.out.println(-1);
                } else {
                    System.out.println(q);
                }
            }
        }
    }


}
