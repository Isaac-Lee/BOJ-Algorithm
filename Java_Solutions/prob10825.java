package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class prob10825 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Student[] arr = new Student[n];
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = new Student(st.nextToken(), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }
        Arrays.sort(arr);
        for (int i = 0; i < n; i++) {
            System.out.println(arr[i].name);
        }
    }
}

class Student implements Comparable{
    String name;
    int k, e, m;

    public Student(String name, int k, int e, int m) {
        this.name = name;
        this.k = k;
        this.e = e;
        this.m = m;
    }

    @Override
    public int compareTo(Object o) {
        Student s = (Student) o;
        if (this.k == (s.k)) {
            if (this.e == (s.e)) {
                if (this.m == (s.m)) {
                    if (this.name.compareTo(s.name) > 0) {
                        return 1;
                    } else {
                        return -1;
                    }
                } else if (this.m > s.m) {
                    return -1;
                } else {
                    return 1;
                }
            } else if (this.e > s.e) {
                return 1;
            } else {
                return -1;
            }
        } else if (this.k > s.k) {
            return -1;
        } else {
            return 1;
        }
    }
}
