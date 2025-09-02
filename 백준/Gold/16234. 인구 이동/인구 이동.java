import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int[][] direction = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
	static int n, l, r;
	static int[][] maps;
	static int min_population;
	static boolean[][] visit;
	static Queue<Country> q;
	static int answer;

	// 1. 국경선을 공유하는 두 나라의 인구수 차이가 l 이상 r이하
	// 2. 각 칸의 인구수 = 연합의 인구수 / 연합을 이루고 있는 칸의 개수
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		l = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		maps = new int[n][n];
		min_population = Integer.MAX_VALUE;
		answer = 0;

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				maps[i][j] = Integer.parseInt(st.nextToken());
				min_population = Math.min(maps[i][j], min_population);
			}
		}
		
		while(true) {
			visit = new boolean[n][n];
			int move = 0;
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					if(!visit[i][j])
						move += bfs(new Country(i, j, maps[i][j]));
			
			if(move == 0)
				break;
			answer++;
		}

		System.out.println(answer);
	}

	static int bfs(Country node) {
		List<Country> union = new ArrayList<>();
		q = new ArrayDeque<>();
		int y = node.y, x = node.x, total_population = node.population;
		union.add(node);
		q.add(node);
		visit[y][x] = true;

		while (!q.isEmpty()) {
			Country i = q.poll();
			for (int[] d : direction) {
				int my = i.y + d[0];
				int mx = i.x + d[1];
				if (0 <= my && my < n && 0 <= mx && mx < n && !visit[my][mx]) {
					int diff = Math.abs(maps[i.y][i.x] - maps[my][mx]);
					if (l <= diff && diff <= r) {
						Country next = new Country(my, mx, maps[my][mx]);
						visit[my][mx] = true;
						union.add(next);
						q.add(next);
						total_population += next.population;
					}
				}
			}
		}

		if (union.size() > 1) {
			for (Country i: union)
				maps[i.y][i.x] = total_population / union.size();
			
			return 1;
		}
		
		return 0;
	}

	static class Country {
		int y, x, population;

		Country(int y, int x, int population) {
			this.y = y;
			this.x = x;
			this.population = population;
		}
	}

}