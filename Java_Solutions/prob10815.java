package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class prob10815 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k, m;
        k = Integer.parseInt(br.readLine());
        int[] card = new int[k];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            card[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(card);

        m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < m; i++){
            ans.append(bSearch(card, Integer.parseInt(st.nextToken())) + " ");
        }
        System.out.println(ans);

    }

    static int bSearch(int[] arr, int key){
        int high, low, mid;
        high = arr.length-1;
        low = 0;

        while (low <= high){
            mid = (low+high)/2;
            if (arr[mid] == key){
                return 1;
            } else if (arr[mid] > key){
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return 0;
    }
}
