package BOJ_Solutios_Java;

import java.util.*;

public class prob1918 {
    static int precedence(char ch) {
        if (ch == '(') return 0;
        if (ch == '+' || ch == '-') return 1;
        else return 2;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        StringBuilder ans = new StringBuilder();
        Stack<Character> ops = new Stack<>();
        for (char ch : s.toCharArray()) {
            if ('A' <= ch && ch <= 'Z') {
                ans.append(ch);
            } else if (ch == '(') {
                ops.push(ch);
            } else if (ch == ')') {
                while (!ops.isEmpty()) {
                    char op = ops.pop();
                    if (op == '(') break;
                    ans.append(op);
                }
            } else {
                while (!ops.isEmpty() && precedence(ops.peek()) >= precedence(ch)) {
                    ans.append(ops.pop());
                }
                ops.push(ch);
            }
        }
        while (!ops.isEmpty()) {
            ans.append(ops.pop());
        }
        System.out.println(ans);
    }
}