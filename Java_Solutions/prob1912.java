package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class prob1912 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(binarySearch(arr, 0, arr.length-1));
        System.out.println(dp(arr));
    }

    public static int binarySearch(int[] arr, int left, int right){
        if (left == right) {
            return arr[left];
        }

        int middle = (left + right) / 2;
        int leftsum = Integer.MIN_VALUE;
        int rightsum = Integer.MIN_VALUE;

        int sum = 0;
        for (int i = middle; i >= left; i--) {
            sum += arr[i];
            leftsum = Math.max(leftsum, sum);
        }
        for (int i = middle+1; i < right; i++) {
            sum += arr[i];
            rightsum = Math.max(rightsum, sum);
        }
        int single = Math.max(binarySearch(arr, left, middle), binarySearch(arr, middle+1, right));
        return Math.max(leftsum + rightsum, single);
    }

    public static int dp(int[] arr) {
        int n = arr.length;
        int sum = Integer.MIN_VALUE;
        int patialSum = 0;

        for (int i = 0; i < n; i++) {
            patialSum = Math.max(0, patialSum) + arr[i];
            sum = Math.max(sum, patialSum);
        }
        return sum;
    }
}
