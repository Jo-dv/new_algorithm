import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n, m;
	static int u, v, cost;
	static ArrayList<Node>[] graph;
	static int[][] grid;
	static StringBuilder answer = new StringBuilder();
	
	static class Node {
		int v, cost;
		Node(int v, int cost) {
			this.v = v;
			this.cost = cost;
		}
	}
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		graph = new ArrayList[n + 1];
		for(int i = 0; i < n + 1; i++) {
			graph[i] = new ArrayList<>();
		}
		for(int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			u = Integer.parseInt(st.nextToken());
			v = Integer.parseInt(st.nextToken());
			cost = Integer.parseInt(st.nextToken());
			graph[u].add(new Node(v, cost));
			graph[v].add(new Node(u, cost));
		}
		
		grid = new int[n + 1][n + 1];
		for(int i = 1; i <= n; i++) {
			solve(i);
		}
		
		for(int i = 1; i <= n; i++) {
			for(int j = 1; j <= n; j++) {
				answer.append(grid[i][j] > 0 ? grid[i][j] : "-").append(" ");
			}
			answer.append("\n");
		}
		
		System.out.println(answer);
	}
	
	static void solve(int start) {
		int[] cost = new int[n + 1];
		int[] trace = new int[n + 1];
		Arrays.fill(cost, Integer.MAX_VALUE);
		cost[start] = 0;
		
		PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.cost - o2.cost);
		pq.add(new Node(start, 0));
				
		while(!pq.isEmpty()) {
			Node current = pq.poll();
			if(cost[current.v] < current.cost) {
				continue;
			}
			
			for(Node next: graph[current.v]) {
				if(current.cost + next.cost < cost[next.v]) {
					pq.add(new Node(next.v, current.cost + next.cost));
					cost[next.v] = current.cost + next.cost;
					
					trace[next.v] = current.v == start ? next.v : trace[current.v];
				}
			}
		}
		
		for (int i = 1; i <= n; i++) {
	        if (i == start) {
	        	continue;
	        }
	        grid[start][i] = trace[i];
	    }
	}
}
