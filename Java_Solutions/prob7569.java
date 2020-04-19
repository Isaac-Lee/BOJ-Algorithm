package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class prob7569 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int m, n, H;
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        Queue<int[]> q = new LinkedList<>();

        // 농장 입력부
        int[][][] map = new int[H][n][m];

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < m; k++) {
                    map[i][j][k] = Integer.parseInt(st.nextToken());
                }
            }
        }
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    if (map[i][j][k] == 1) {
                        int[] point = {k, j, i};
                        q.offer(point);
                    }
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
                int h = startPoint[2];

                if (h > 0 && map[h-1][y][x] == 0) {
                    map[h-1][y][x] = 1;
                    int[] tmp = {x, y, h-1};
                    q.offer(tmp);
                    changed = true;
                }
                if (y > 0 && map[h][y-1][x] == 0) {
                    map[h][y-1][x] = 1;
                    int[] tmp = {x, y-1, h};
                    q.offer(tmp);
                    changed = true;
                }
                if (x > 0 && map[h][y][x-1] == 0) {
                    map[h][y][x-1] = 1;
                    int[] tmp = {x-1, y, h};
                    q.offer(tmp);
                    changed = true;
                }
                if (h < h-1 && map[h+1][y][x] == 0) {
                    map[h+1][y][x] = 1;
                    int[] tmp = {x, y, h+1};
                    q.offer(tmp);
                    changed = true;
                }
                if (y < n-1 && map[h][y+1][x] == 0) {
                    map[h][y+1][x] = 1;
                    int[] tmp = {x, y+1, h};
                    q.offer(tmp);
                    changed = true;
                }
                if (x < m-1 && map[h][y][x+1] == 0) {
                    map[h][y][x + 1] = 1;
                    int[] tmp = {x + 1, y, h};
                    q.offer(tmp);
                    changed = true;
                }
            }
            answer++;
        }
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    if (map[i][j][k] == 0) {
                        System.out.println(-1);
                        return;
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
