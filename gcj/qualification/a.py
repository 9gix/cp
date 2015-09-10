testcase = []
with open('a.in', 'r') as f:
    t = f.readline()
    for i in range(int(t)):
        case = f.readline().split()[1]
        case = list(map(lambda x: int(x), list(case)))
        testcase.append(case)

result = []
for case in testcase:
    extra_clapper = 0
    total_clapper = 0
    for shyness_level, n_people in enumerate(case):
        if n_people > 0:
            if total_clapper < shyness_level:
                deficit = shyness_level - total_clapper
                extra_clapper += deficit
                total_clapper += deficit
            total_clapper += n_people
    result.append(extra_clapper)


with open('a.out', 'w') as f:
    for i, friend in enumerate(result):
        print("Case #{}: {}".format(i+1, friend), file=f)



    


