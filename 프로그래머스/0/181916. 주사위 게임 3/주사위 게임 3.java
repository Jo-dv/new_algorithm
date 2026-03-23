import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int[] nums = {a, b, c, d};
        Arrays.sort(nums);

        // 1. 네 숫자가 모두 같은 경우
        if (nums[0] == nums[3]) {
            return 1111 * nums[0];
        } 
        // 2. 세 숫자가 같은 경우
        else if (nums[0] == nums[2]) { // 앞의 3개가 같음
            return (int) Math.pow(10 * nums[0] + nums[3], 2);
        } else if (nums[1] == nums[3]) { // 뒤의 3개가 같음
            return (int) Math.pow(10 * nums[1] + nums[0], 2);
        } 
        // 3. 두 개씩 같은 경우
        else if (nums[0] == nums[1] && nums[2] == nums[3]) {
            return (nums[0] + nums[2]) * Math.abs(nums[0] - nums[2]);
        } 
        // 4. 두 개만 같고 나머지 두 개는 각각 다른 경우
        else if (nums[0] == nums[1]) { // [p, p, q, r]
            return nums[2] * nums[3];
        } else if (nums[1] == nums[2]) { // [q, p, p, r]
            return nums[0] * nums[3];
        } else if (nums[2] == nums[3]) { // [q, r, p, p]
            return nums[0] * nums[1];
        } 
        else {
            return nums[0];
        }
    }
}