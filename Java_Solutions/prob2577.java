package BOJ_Solutios_Java;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class prob2577 {
    public static void main(String[] args) throws Exception {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int a,b,c;
        a = Integer.valueOf(in.readLine());
        b = Integer.valueOf(in.readLine());
        c = Integer.valueOf(in.readLine());

        String number = Integer.toString(a*b*c);
        char[] nums = number.toCharArray();

        int[] num = new int[10];
        for (int i = 0; i < nums.length; i++){
        	int index = nums[i] - '0';
        	num[index] += 1;
        }
        for (int n : num){
            System.out.println(n);
        }
    }
}