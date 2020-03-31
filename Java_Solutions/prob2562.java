import java.io.*;

class prob2562 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] num = new int[9];
        for (int i = 0; i < 9; i++){
            num[i] = Integer.parseInt(br.readLine());
        }
        int max = Integer.MIN_VALUE;
        int index = 0;
        for (int i = 0; i < 9; i++) {
            if (num[i] > max){
                max = num[i];
                index = i;
            }
        }
        System.out.println(max);
        System.out.println(index+1);
        bw.close();
    }
}