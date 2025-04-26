import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static String code;
	
	public static void main(String[] args) throws IOException {
		code = br.readLine();
		
		solve();
	}
	
	static void solve() {
		int[] dp = new int[code.length() + 1];
		dp[0] = 1;
		dp[1] = 1;
		
		if(code.charAt(0) == '0') {
			System.out.println(0);
			return;
		}
		
		for(int i = 2; i <= code.length(); i++) {
			if(code.charAt(i - 1) != '0') {
				dp[i] += dp[i - 1];
			}
			int num = Integer.parseInt(code.substring(i - 2, i));
			if(10 <= num && num <= 26) {
				dp[i] += dp[i - 2];
			}
			dp[i] %= 1000000;
		}
		
		System.out.println(dp[code.length()]);
	}
}