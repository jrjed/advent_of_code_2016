def read_ips(datafile):
    with open(datafile) as f:
        ips = zip(*[line.split() for line in f])
    f.close()
    return list(ips[0])


def splitter(ip, chunksize=6):
    ip = ' ' + ip + ' '
    chunks = [ip[i: i+chunksize] for i in range(len(ip))]
    return [chunk for chunk in chunks if len(chunk) == chunksize]


def abba_test(ip):
    candidates = []
    for chunk in splitter(ip):
        a, b, c, d , e, f = chunk
        if b == e and c == d and b != c:
            candidates.append(chunk)
    if len(candidates) == 0:
        return False
    else:
        for candidate in candidates:
            if candidate[0] == '[' and candidate[-1] == ']':
                return False
            else:
                return True


def tls_check(ips):
    results = []
    for ip in ips:
        results.append(abba_test(ip))
    for res in results:
        print res
    return sum(results)
    

def main():
    print(tls_check(read_ips('input7.txt')))

main()
