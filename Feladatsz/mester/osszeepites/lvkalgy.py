n = int(input())
megold = float("inf")
van = False
for i in range(n):
    be = int(input())
    if be > 120 and be < megold:
        van = True
        megold = be
if van:
    print(n, megold)
else: 
    print("-1")