import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m, r;
	static int u, v;
	static HashMap<Integer, ArrayList<Integer>> graph = new HashMap<>();
	static StringBuilder sb = new StringBuilder();
	static int[] visited;
	static int num = 1;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		
		for(int i = 1; i <= n; i++) {
			graph.put(i, new ArrayList<>());
		}
		
		for(int i = 1; i <= m; i++) {
			st = new StringTokenizer(br.readLine());
			u = Integer.parseInt(st.nextToken());
			v = Integer.parseInt(st.nextToken());
			graph.get(u).add(v);
			graph.get(v).add(u);
		}
		
		visited = new int[n + 1];
		
		solve();
		System.out.println(sb);
	}
	
	static void search(int current) {
		visited[current] = num;
		Collections.sort(graph.get(current));
		
		for(int next: graph.get(current)) {
			if(visited[next] == 0) {
				num++;
				search(next);
			}
		}
	}
	
	static void solve() {
		search(r);
		
		for(int i = 1; i <= n; i++) {
			sb.append(visited[i]).append("\n");
		}
	}
}