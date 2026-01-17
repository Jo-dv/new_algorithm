import java.util.*;

class Solution {
    boolean checkValid(int[] diffs, int[] times, long limit, int level) {
        int size = diffs.length;
        long totalTime = times[0];
        if(totalTime > limit) {
            return false;
        }
        
        for(int i = 1; i < size; i++) {
            long diff = diffs[i];
            long timeCurrent = times[i];
            long timePrev = times[i-1];
            
            if(diff <= level) {
                totalTime += timeCurrent;
            } else {
                long gap = diff - level;
                totalTime += (gap * (timeCurrent + timePrev) + timeCurrent);
            }
            
            if(totalTime > limit) {
                return false;
            }
        }
        
        return true;
    }
    public int solution(int[] diffs, int[] times, long limit) {
        int answer = 0;
        int left = 1;
        int right = Arrays.stream(diffs).max().getAsInt();
        while(left <= right) {
            int mid = (left + right) / 2;
            
            if(checkValid(diffs, times, limit, mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return answer;
    }
}