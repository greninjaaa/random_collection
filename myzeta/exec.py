from datetime import datetime, timedelta
from multiprocessing.sharedctypes import Value
from myzeta import * 

q = input("goal for 2m? ")

try:
    int(q)
except ValueError:
    exit("not an integer")

d = datetime.now()
z = zetafloat()
for i in range(0, int(q)):
    op = z.operation()
    nums = z.gen_nums(op)
    ans = z.ans(op, nums)
    user = -1
    while True:
        try:
            print(ans[0])
            if float(input()) == ans[1]:
                break
        except ValueError:
            pass

d2 = datetime.now()
comp = timedelta(minutes=2)
if (d2 - d) > comp:
    print("too slow")
else:
    print("nice job")

print("total time taken", d2 - d)