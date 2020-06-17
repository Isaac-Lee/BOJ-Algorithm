//package BOJ_Solutios_Java;
//
//import java.io.IOException;
//import java.util.Arrays;
//import java.util.Scanner;
//
//public class prob2512 {
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);​
//        int N = sc.nextInt();
//        int[] region = new int[N];
//        for(int i=0; i<N; i++)
//            region[i] = sc.nextInt();
//
//        Arrays.sort(region);
//
//        int budget = sc.nextInt();
//        int limit = 0;
//        for(int i=0; i<N; i++){
//            if(region[i] * (N-i) < budget){
//                budget -= region[i];
//            }else{
//                limit = budget/(N-i);
//                break;
//            }
//        }
//
//        if(limit == 0)
//            limit = region[N-1];
//
//        System.out.println(limit);
//
//
//    }
//}
