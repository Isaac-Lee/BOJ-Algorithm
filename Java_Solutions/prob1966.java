import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class prob1966 {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(reader.readLine());
        LinkedList<Integer> queue = new LinkedList<>();
        StringBuilder builder = new StringBuilder();

        for(int n=0 ; n<T ; n++){
            String[] input = reader.readLine().split(" ");
            String[] priority = reader.readLine().split(" ");
            int N = Integer.parseInt(input[0]);
            int M = Integer.parseInt(input[1]);
            int count = 0;
            queue.clear(); // 큐 초기화

            for(int i=0 ; i<N ; i++)
                queue.add(Integer.parseInt(priority[i])); // 큐에 중요도 데이터 추가

            while(!queue.isEmpty()){
                boolean isPriority = true;

                for(int i=1 ; i<queue.size() ; i++){ // 맨 앞 데이터의 중요도가 가장 높은지 확인
                    if(queue.peek() < queue.get(i)){
                        isPriority = false;
                        break;
                    }
                }

                if(isPriority){ // 가장 높다면 큐에서 제거, 구하려는 값이 아니라면 M값 갱신
                    count++;
                    queue.poll();

                    if(M == 0)
                        break;
                    else
                        M -= 1;
                }
                else { // 중요도가 가장 높은 문서가 아니라면 뒤로 보내고 M값 갱신
                    int temp = queue.poll();
                    queue.add(temp);
                    M = (M==0) ? queue.size()-1 : --M;
                }
            }
            builder.append(count).append("\n");
        }
        System.out.println(builder);
    }
}
