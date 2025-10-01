class Solution {
    public String solution(String myString) {
        String answer = "";
        for(int i = 0; i < myString.length(); i++) {
            if(myString.charAt(i) - 97 < 0) {
                answer += myString.charAt(i);
            } else {
               answer += (char)(myString.charAt(i) - 32);
            }
        }
        return answer;
    }
}