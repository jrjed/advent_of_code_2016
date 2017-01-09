import re


def read_ips(datafile):
    with open(datafile) as f:
        ips = zip(*[line.strip().split() for line in f])
    f.close()
    return list(ips[0])


def tls_test(ip):
    good_abba = re.search(r'([a-z])(?!\1)([a-z])\2\1', ip)
    bad_abba = re.search(r'\[([a-z]*)([a-z])(?!\2)([a-z])\3\2([a-z]*)\]', ip)
    if good_abba and not bad_abba:
        return True
    else:
        return False


def ssl_test(ip):
    for i, letter in enumerate(ip):
        outside = ''.join([s.split(']')[-1] for s in ip.split('[')]).strip()
        chunk = outside[i: i+3]
        aba = re.search(r'([a-z])(?!\1)([a-z])\1', chunk)
        if aba:
            a, b = aba.group(1, 2)
            bab = re.search(r'\[([a-z]*)(' + b + a + b + ')([a-z]*)\]', ip)
            if bab:
                return True
    return False


def main():
    # Part 1
    print(sum(map(tls_test, read_ips('input7.txt'))))
    # Part 2 Guessed 239(too low)
    print(sum(map(ssl_test, read_ips('input7.txt'))))


if __name__ == '__main__':
    main()
