table = {
    '1': {
        '1': '1',
        'i': 'i',
        'j': 'j',
        'k': 'k',
    },
    'i': {
        '1': 'i',
        'i': '-1',
        'j': 'k',
        'k': '-j',
    },
    'j': {
        '1': 'j',
        'i': '-k',
        'j': '-1',
        'k': '1',
    },
    'k': {
        '1': 'k',
        'i': 'j',
        'j': '-i',
        'k': '-1',
    },
}


def read_testcase(fname):
    testcase = [] 
    with open('{}.in'.format(fname), 'r') as f:
        t = f.readline()
        for i in range(int(t)):
            repeat = int(f.readline().split()[1])
            case = f.readline().strip() * repeat
            testcase.append(case)
    return testcase

memo_join = {}
def join(a, b):
    if (a,b) in memo_join:
        return memo_join[(a,b)]
    negate = a.startswith('-') != b.startswith('-')
    a, b = [i.lstrip('-') for i in [a, b]]
    result = table[a][b]
    if negate:
        if result.startswith('-'):
            result = result.lstrip('-')
        else:
            result = '-{}'.format(result)
    memo_join[(a,b)] = result
    return result

memo_reduce = {}
def _reduce(s):
    if s in memo_reduce:
        return memo_reduce[s]
    x = s[0]
    for i in range(1, len(s)):
        segment = s[0:i]
        if (segment in memo_reduce):
            x = memo_reduce[segment]
        else:
            x = join(x, s[i])
            memo_reduce[segment] = x
    memo_reduce[s] = x
    return x



def execute(s):
    if len(s) < 3:
        return "NO"
    
    pi = 1
    pj = 2
    found_i = False
    found_j = False

    si, sj, sk = s[:pi], s[pi:pj], s[pj:]
    for i in range(1, len(s) - 1):
        if _reduce(s[0:i]) == 'i':
            pi = i
            found_i = True
            break
    print("Found I")

    if not found_i: return "NO"

    for j in range(pi + 1, len(s)):
        if _reduce(s[pi:j]) == 'j':
            pj = j
            found_j = True
            break

    print("Found J")
    if not found_j: return "NO"
    for k in range(pj + 1, len(s)+1):
        if _reduce(s[pj:]) == 'k':
            return "YES"


    return "NO"


def save(result, fname):
    with open('{}.out'.format(fname), 'w') as fname:
        for i, out in enumerate(result):
            print("Case #{}: {}".format(i+1, out), file=fname)

    
def main():
    fname = "c"
    testcase = read_testcase(fname)
    result = [execute(case) for case in testcase]
    save(result, fname)

if __name__ == '__main__':
    main()


