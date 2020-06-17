package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class prob3020 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n, h;
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        Map<Integer, Integer> height = new HashMap<>();
        for (int j = 0; j < h; j++) {
            height.put(j, 0);
        }
        for (int i = 0; i < n; i++) {
            int k = Integer.parseInt(br.readLine());
            if (i %2 == 0) {
                for (int j = 0; j < k; j++) {
                    height.put(j, height.get(j)+1);
                }
            } else {
                for (int j = h-1; j > h-(k+1); j--) {
                    height.put(j, height.get(j)+1);
                }
            }
        }

        Iterator it = sortByValue(height).iterator();

        int min = height.get((Integer) it.next());
        int cnt = 1;

        while(it.hasNext()) {
            Integer temp = (Integer) it.next();
            if (height.get(temp) > min) {
                break;
            }
            cnt++;
        }
        System.out.println(min+" "+cnt);
    }

    public static List sortByValue(final Map map) {
        List<String> list = new ArrayList();
        list.addAll(map.keySet());

        Collections.sort(list, new Comparator() {
            public int compare(Object o1,Object o2) {
                Object v1 = map.get(o1);
                Object v2 = map.get(o2);

                return ((Comparable) v2).compareTo(v1);
            }
        });

        Collections.reverse(list);
        return list;
    }
}
