P1, P2, P3, P4 = map(int, input().split())

problems = [P1, P2, P3, P4]

count = sum(1 for p in problems if p >= 10)

print(count)
