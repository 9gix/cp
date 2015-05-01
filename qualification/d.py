
def read_testcase(fname):
    testcase = [] 
    with open('{}.in'.format(fname), 'r') as f:
        t = f.readline()
        for i in range(int(t)):
            case = tuple(int(x) for x in f.readline().split())
            testcase.append(case)
    return testcase


def execute(case):
    
    x, r, c = case

    grid_area = r * c
    quotient, remainder = divmod(grid_area, x)

    ldim = min(r, c)
    hdim = max(r, c)

    if ((remainder != 0) or (ldim < x and hdim < x) or (ldim <= x - 2) or (x > 6)):
        return 'RICHARD'
    else:
        return 'GABRIEL'
    

def save(result, fname):
    with open('{}.out'.format(fname), 'w') as fname:
        for i, out in enumerate(result):
            print("Case #{}: {}".format(i+1, out), file=fname)

    
def main():
    fname = "d"
    testcase = read_testcase(fname)
    result = [execute(case) for case in testcase]
    save(result, fname)

if __name__ == '__main__':
    main()


