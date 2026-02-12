import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int[][] games;
    static List<List<Integer>> expectations = new ArrayList<>();
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        games = new int[n][3];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int number = Integer.parseInt(st.nextToken());
            int strike = Integer.parseInt(st.nextToken());
            int ball = Integer.parseInt(st.nextToken());

            games[i][0] = number;
            games[i][1] = strike;
            games[i][2] = ball;
        }

        solve();
    }

    static void search(int cnt, List<Integer> temp, boolean[] check) {
        if (temp.size() == 3) {
            expectations.add(new ArrayList<>(temp));
            return;
        }

        for (int i = 1; i <= 9; i++) {
            if (check[i])
                continue;
            temp.add(i);
            check[i] = true;
            search(cnt + 1, temp, check);
            temp.remove(temp.size() - 1);
            check[i] = false;
        }
    }

    static void solve() {
        search(0, new ArrayList<>(), new boolean[10]);  // 숫자 조합 생성

        Iterator<List<Integer>> iter = expectations.iterator();
        while (iter.hasNext()) {
            List<Integer> expectation = iter.next();
            boolean isValid = true;

            for (int[] game : games) {
                int strike_cnt = 0;
                int ball_cnt = 0;
                String nums = String.valueOf(game[0]);

                for (int i = 0; i < 3; i++) {
                    int expected_num = expectation.get(i);
                    if (expected_num == nums.charAt(i) - '0')
                        strike_cnt++;
                    else if (nums.contains(String.valueOf(expected_num)))  // 위치가 일치하진 않지만 숫자를 포함하는 경우
                        ball_cnt++;
                }

                if (!(strike_cnt == game[1] && ball_cnt == game[2])) {
                    isValid = false;
                    break;
                }
            }

            if (!isValid)
                iter.remove();
        }

        answer = expectations.size();
        System.out.println(answer);
    }
}