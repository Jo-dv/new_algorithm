import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static int n;
	static int answer;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		answer = 0;
		
		solve();
	}
	
	static void solve() {
		int[][] dp = new int[n + 1][10];
		
		for(int i = 0; i < 10; i++) {
			dp[1][i] = 1;
		}
		
		for(int i = 2; i < n + 1; i++) {  // 길이
			for(int j = 0; j < 10; j++) {  // 숫자
				for(int k = 0; k < j + 1; k++) {  // 이전 숫자들(작거나 같은)
					dp[i][j] += dp[i - 1][k];
				}
				dp[i][j] %= 10007;
			}
		}
		
		for(int i: dp[n]) {
			answer += i;
		}
		
		System.out.println(answer % 10007);
	}
}
