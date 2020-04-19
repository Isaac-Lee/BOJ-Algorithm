package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class prob2178 {
    public static int rows = 0;    // 행수
    public static int cols = 0;    // 열수
    public static int[][] map = null;    // 맵정보
    public static int shortestDist = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(in.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());

        map = new int[rows][cols];

        for (int j = 0; j < rows; j++) {
            String row = in.readLine();
            for (int k = 0; k < cols; k++) {
                map[j][k] = Integer.parseInt(String.valueOf(row.charAt(k)));
            }
        }

        shortestDist = Integer.MAX_VALUE;

        int curRow = 0;        // 현재 row
        int curCol = 0;        // 현재 col
        int curDist = 1;    // 현재 이동한 거리

        dfs(new Coord(curRow, curCol, curDist));

        System.out.println(shortestDist);
    }

    static void dfs(Coord coord) {
        int curRow = coord.row;        // 현재 row
        int curCol = coord.col;        // 현재 col
        int curDist = coord.dist;    // 현재 이동한 거리

        map[curRow][curCol] = 0;
        if(curRow == rows - 1 && curCol == cols - 1) {
            if(curDist < shortestDist) {
                shortestDist = curDist;
            }
        }
        // 위로 갈수 있으면
        if(curRow-1 >= 0 && map[curRow-1][curCol] == 1) {
            dfs(new Coord(curRow-1, curCol, curDist+1));
        }
        // 아래로 갈수 있으면
        if(curRow+1 < rows && map[curRow+1][curCol] == 1) {
            dfs(new Coord(curRow+1, curCol, curDist+1));
        }
        // 왼쪽으로 갈수 있으면
        if(curCol-1 >= 0 && map[curRow][curCol-1] == 1) {
            dfs(new Coord(curRow, curCol-1, curDist+1));
        }
        // 오른쪽으로 갈수 있으면
        if(curCol+1 < cols && map[curRow][curCol+1] == 1) {
            dfs(new Coord(curRow, curCol+1, curDist+1));
        }

        // 지나간 자리를 다시 지나갈수 있도록 복구함.
        map[curRow][curCol] = 1;
    }

    static class Coord {
        int row, col, dist;

        public Coord(int row, int col, int dist) {
            this.row = row;
            this.col = col;
            this.dist = dist;
        }
    }
}
