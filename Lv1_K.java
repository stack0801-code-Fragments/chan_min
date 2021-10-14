import java.util.Arrays;
public class Lv1_K {
    class Solution {
        public int[] solution(int[] array, int[][] commands) {
            int size = commands.length;
            int[] answer = new int[size]; 
            
            for(int i = 0; i < size; i++){
                int cnt = 0;                
                int temp[] = new int[commands[i][1] - commands[i][0] + 1];
                for(int j = commands[i][0] -1 ; j <= commands[i][1] - 1; j++)
                {
                    temp[cnt] = array[j];
                    cnt++;
                }
                Arrays.sort(temp);
                answer[i] = temp[commands[i][2] - 1];
            }
            return answer;
        }
    }
}

/* 다른 사람 풀이
import java.util.Arrays;
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for(int i=0; i<commands.length; i++){
            int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            Arrays.sort(temp);
            answer[i] = temp[commands[i][2]-1];
        }

        return answer;
    }
}
*/
