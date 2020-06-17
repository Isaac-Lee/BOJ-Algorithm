package BOJ_Solutios_Java;

import java.io.*;
class Main{
    public static void main(String[] args)throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] reader=new String[2];
        reader=br.readLine().split(" ");
        int n=Integer.parseInt(reader[0]);
        int k=Integer.parseInt(reader[1]);
        int[] distance=new int[n];
        for(int i=0;i<distance.length;i++){
            distance[i]=Integer.parseInt(br.readLine());
        }
        int l=1;
        int count=0;
        for(int i=0;i<30;i++){
            l*=2;
        }
        int sub=l;
        for(;;){
            count=0;
            for(int i=0;i<distance.length;i++){
                count+=(distance[i]/l);
            }
            sub/=2;
            if(count<k){
                if(sub==0){
                    System.out.println(l-1);
                    break;
                }else{
                    l-=sub;
                }
            }else{
                if(sub==0){
                    System.out.println(l);
                    break;
                }else{
                    l+=sub;
                }
            }
        }



    }
}