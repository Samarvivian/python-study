from z3 import *
solver = Solver()#创建一个z3求解器·

x = [BitVec(f'x{i}', 32) for i in range(11)]

solver.add(((x[0]* 0xccffbbbb + 0xdeadc0de) ^ 0xdeadbeef + 0xd3906) == 0xb5073388)
solver.add(((x[1]* 0xccffbbbb + 0xdeadc0de) ^ 0xdeadbeef + 0xd3906) == 0xf58ea46f)
solver.add(((x[2]* 0xccffbbbb + 0xdeadc0de) ^ 0xdeadbeef + 0xd3906) == 0x8cd2d760)
solver.add(((x[3]* 0xccffbbbb + 0xdeadc0de) ^ 0xdeadbeef + 0xd3906) == 0x7fc56cda)
solver.add(((x[4]* 0xccffbbbb + 0xdeadc0de) ^ 0xdeadbeef + 0xd3906) == 0x52bc07da)
solver.add(((x[5]* 0xccffbbbb + 0xdeadc0de) ^ 0xdeadbeef + 0xd3906) == 0x29054b48)
solver.add(((x[6]* 0xccffbbbb + 0xdeadc0de) ^ 0xdeadbeef + 0xd3906) == 0x42d74750)
solver.add(((x[7]* 0xccffbbbb + 0xdeadc0de) ^ 0xdeadbeef + 0xd3906) == 0x11297e95)
solver.add(((x[8]* 0xccffbbbb + 0xdeadc0de) ^ 0xdeadbeef + 0xd3906) == 0x5cf2821b)
solver.add(((x[9]* 0xccffbbbb + 0xdeadc0de) ^ 0xdeadbeef + 0xd3906) == 0x747970da)
solver.add(((x[10]* 0xccffbbbb + 0xdeadc0de) ^ 0xdeadbeef + 0xd3906) == 0x64793c81)

if solver.check() == sat:
    model = solver.model()
    for i in range(11):
        print(f'x{i} = {model[x[i]]}')
else:
    print("方程组无解")

arr=[
1667592045,
1669031540,
875849269,
758264675,
962749027,
875836461,
1700867429,
1663906918,
929130032,
912340835,
2103523170
]
for i in range(11):
    for k in range(4):
        print(chr(arr[i]>>(k*8)&0xff),end='')

