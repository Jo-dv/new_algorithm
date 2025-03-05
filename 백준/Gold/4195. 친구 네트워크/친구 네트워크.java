import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int t;
	static int f;
	static HashMap<String, String> parents;
	static HashMap<String, Integer> child;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
		t = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < t; i++) {
			f = Integer.parseInt(br.readLine());
			parents = new HashMap<>();
			child = new HashMap<>();
			
			for(int j = 0; j < f; j++) {
				st = new StringTokenizer(br.readLine());
				String friend1 = st.nextToken();
				String friend2 = st.nextToken();
				
				if(!parents.containsKey(friend1)) {
					parents.put(friend1, friend1);
					child.put(friend1, 1);
				}
				
				if(!parents.containsKey(friend2)) {
					parents.put(friend2, friend2);
					child.put(friend2, 1);
				}
				sb.append(union(friend1, friend2)).append("\n");
			}
		}
		System.out.println(sb);
	}
	
	static String find(String x) {
		if(parents.get(x).equals(x))
			return x;
		parents.put(x, find(parents.get(x)));
		return parents.get(x);
	}
	
	static int union(String x, String y) {
		x = find(x);
		y = find(y);
		
		if(x.equals(y))
			return child.get(y);
		
		parents.put(y, x);
		child.put(x, child.get(x) + child.get(y));
		return child.get(x);
	}
}