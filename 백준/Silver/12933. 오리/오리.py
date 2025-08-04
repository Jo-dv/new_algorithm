class Main:
    def __init__(self):
        self.sounds = input()
        self.answer = 0

    def solve(self):
        order = "quack"
        duck_states = []
        max_ducks = 0

        for ch in self.sounds:
            found = False
            for i in range(len(duck_states)):
                expected_char = order[duck_states[i]]
                if ch == expected_char:
                    duck_states[i] += 1
                    if duck_states[i] == 5:
                        duck_states[i] = 0
                    found = True
                    break
            if not found:
                if ch == 'q':
                    duck_states.append(1)
                    max_ducks = max(max_ducks, len(duck_states))
                else:
                    print(-1)
                    return

        if any(state != 0 for state in duck_states):
            print(-1)
            return

        print(max_ducks)


problem = Main()
problem.solve()
