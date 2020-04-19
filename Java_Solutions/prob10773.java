package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class prob10773 {
    public static void main(String[] args) throws IOException {
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        int n, answer = 0,  k = Integer.parseInt(input.readLine());
        Stack<Integer> s = new Stack<>();

        for (int i = 0; i < k; i++) {
            n = Integer.parseInt(input.readLine());
            if (n > 0) {
                s.push(n);
            } else {
                s.pop();
            }
        }
        for (int i : s){
            answer += i;
        }
        System.out.println(answer);
    }
}
