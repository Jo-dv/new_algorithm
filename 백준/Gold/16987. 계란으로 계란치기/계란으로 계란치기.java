import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n;
	static int s, w;
	static Egg[] eggs;
	static int answer = 0;
	
	static class Egg {
		int s, w;
		
		Egg(int s, int w) {
			this.s = s;
			this.w = w;
		}
	}
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		eggs = new Egg[n];
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken());
			w = Integer.parseInt(st.nextToken());
			eggs[i] = new Egg(s, w);
		}
		
		solve();
		System.out.println(answer);
	}

	static void dfs(int idx) {
		if (idx == n) {
			int broken = 0;
			for (int i = 0; i < n; i++) {
				if (eggs[i].s <= 0) broken++;
			}
			answer = Math.max(answer, broken);
			return;
		}

		if (eggs[idx].s <= 0) {  // 현재 계란이 이미 깨졌으면 다음 계란으로
			dfs(idx + 1);
			return;
		}

		boolean hit = false;

		for (int i = 0; i < n; i++) {
			if (i == idx || eggs[i].s <= 0) {
				continue;
			}

			eggs[idx].s -= eggs[i].w;  // 계란 idx로 i를 친다
			eggs[i].s -= eggs[idx].w;
			hit = true;

			dfs(idx + 1);

			eggs[idx].s += eggs[i].w;  // 상태 복구
			eggs[i].s += eggs[idx].w;
		}

		
		if (!hit) {  // 칠 수 있는 계란이 없을 경우 그냥 넘긴다
			dfs(idx + 1);
		}
	}
	
	static void solve() {
		dfs(0);
	}
}