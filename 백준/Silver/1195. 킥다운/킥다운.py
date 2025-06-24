class Main:
    def __init__(self):
        self.part1 = input()
        self.part2 = input()

    def solve(self):
        if len(self.part1) < len(self.part2):
            slider = self.part1
            standard = self.part2
        else:
            slider = self.part2
            standard = self.part1

        len_slider = len(slider)
        len_standard = len(standard)
        min_width = len_slider + len_standard

        for shift in range(-len_slider, len_standard + 1):
            overlap_ok = True
            for i in range(len_slider):
                pos_in_standard = shift + i
                if 0 <= pos_in_standard < len_standard:
                    if slider[i] == '2' and standard[pos_in_standard] == '2':
                        overlap_ok = False
                        break
            if overlap_ok:
                left = min(0, shift)
                right = max(len_standard, shift + len_slider)
                width = right - left
                min_width = min(min_width, width)

        print(min_width)


problem = Main()
problem.solve()
