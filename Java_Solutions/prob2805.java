package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class prob2805 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int m = Integer.parseInt(br.readLine());

        List<Integer> tree = new ArrayList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            tree.add(Integer.parseInt(st.nextToken()));
        }

        tree.sort(Comparator.naturalOrder());

        int first = binarySearch(tree, m);
        System.out.println(first);
        for (int i = 0; i < tree.size(); i++) {
            if (tree.get(i) > first) {
                tree.add(i, tree.get(i) - (tree.get(i)-first));
            }
        }
        int second = binarySearch(tree, m);
        System.out.println(second);
    }
    public static int binarySearch(List<Integer> arr, int key) {
        int low = 0;
        int high = arr.get(arr.size()-1);
        int mid;
        int s;

        while (low <= high){
            s = 0;
            mid = (low+high)/2;
            for (int i = 0; i < arr.size(); i++) {
                if (arr.get(i) > mid) {
                    s += arr.get(i) - mid;
                }
            }
            if (s >= key){
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return high;
    }
}
