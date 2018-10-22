class Manager:
    def __init__(self):
        pass

    def paint(self, N, T, L):
        start = max(L)
        end = sum(L)

        while start < end:
            mid = (start + end)//2
            required_num = self.getRequiredPainters(L, mid)
            if required_num <= N:
                end = mid
            else:
                start = mid + 1
        if self.getRequiredPainters(L, start) <= N:
            return 2 * N * start / T
        else:
            return 2 * N * end / T

    def getRequiredPainters(self, l, max_per_painter):
        cur_total = 0
        num_painter = 1
        for i in range(len(l)):
            cur_total += l[i]
            if cur_total > max_per_painter:
                cur_total = l[i]
                num_painter += 1
        return num_painter

if __name__ == '__main__':
  manager = Manager()
  N = 10
  T = 5
  L = [10, 15, 10, 5, 10, 15, 20, 20, 15, 20]

  print(manager.paint(N, T, L))

