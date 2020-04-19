package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class prob7576 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int m, n;
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        Queue<int[]> q = new LinkedList<>();

        // 농장 입력부
        int[][] map = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 1) {
                    int[] point = {j, i};
                    q.offer(point);
                }
            }
        }

        int answer = 0;
        boolean changed = true;

        while (changed) {
            changed = false;
            int ripeCont = q.size();

            for (int i = 0; i < ripeCont; ++i) {
                int[] startPoint = q.poll();
                int x = startPoint[0];
                int y = startPoint[1];

                if (y > 0 && map[y-1][x] == 0) {
                    map[y-1][x] = 1;
                    int[] tmp = {x, y-1};
                    q.offer(tmp);
                    changed = true;
                }
                if (x > 0 && map[y][x-1] == 0) {
                    map[y][x-1] = 1;
                    int[] tmp = {x-1, y};
                    q.offer(tmp);
                    changed = true;
                }
                if (y < n-1 && map[y+1][x] == 0) {
                    map[y+1][x] = 1;
                    int[] tmp = {x, y+1};
                    q.offer(tmp);
                    changed = true;
                }
                if (x < m-1 && map[y][x+1] == 0) {
                    map[y][x + 1] = 1;
                    int[] tmp = {x + 1, y};
                    q.offer(tmp);
                    changed = true;
                }
            }
            if (changed == false) {
                break;
            } else {
                answer++;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 0) {
                    System.out.println(-1);
                    return;
                }
            }
        }
        System.out.println(answer);
    }
}
