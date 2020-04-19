package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.Stack;

public class prob1935 {

    static int N;
    static int[] arr;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws NumberFormatException, IOException {

        N = Integer.parseInt(br.readLine());
        String str = br.readLine();
        arr = new int[N];

        for (int i = 0; i < N; i++)
            arr[i] = Integer.parseInt(br.readLine());

        System.out.printf("%.2f", calPostfix(str));

    }

    public static double calPostfix(String input) {

        Stack<Double> stack = new Stack<>();
        int len = input.length();

        for (int i = 0; i < len; i++) {

            char op = input.charAt(i);

            if (op >= 'A' && op <= 'Z') {
                stack.push((double) arr[op - 'A']);
            } else {

                double op2 = stack.pop();
                double op1 = stack.pop();
                switch (op) {

                    case '+':
                        stack.push(op1 + op2);
                        break;
                    case '-':
                        stack.push(op1 - op2);
                        break;
                    case '*':
                        stack.push(op1 * op2);
                        break;
                    case '/':
                        stack.push(op1 / op2);
                        break;
                }
            }
        }
        return stack.pop();
    }
}