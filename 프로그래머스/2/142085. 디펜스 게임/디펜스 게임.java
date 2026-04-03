import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        int soldier = n;
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int e: enemy) {
            soldier -= e;
            pq.add(e);
            
            if(soldier < 0) {
                if(k > 0) {
                    soldier += pq.poll();
                    k--;
                } else {
                    break;
                }
            }
            
            answer++;
        }
        
        return answer;
    }
}