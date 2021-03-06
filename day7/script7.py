import re


def read_lines(datafile):
    with open(datafile) as f:
        lines = list(f.readlines())
    f.close()
    return lines


def tls_test(ip):
    good_abba = re.search(r'([a-z])(?!\1)([a-z])\2\1', ip)
    bad_abba = re.search(r'\[([a-z]*)([a-z])(?!\2)([a-z])\3\2([a-z]*)\]', ip)
    if good_abba and not bad_abba:
        return True
    else:
        return False


def ssl_test(ip):
    outside = ''.join([s.split(']')[-1] for s in ip.split('[')]).strip()
    aba = re.findall(r'(?=([a-z])(?!\1)([a-z])\1)', outside)
    if aba:
        for match in aba:
            a, b = match
            bab = re.search(r'\[([a-z]*)(' + b + a + b + ')([a-z]*)\]', ip)
            if bab:
                return True
    return False


def main():
    # Part 1
    print(sum(map(tls_test, read_lines('input7.txt'))))
    # Part 2 Guessed 239(too low)
    print(sum(map(ssl_test, read_lines('input7.txt'))))


if __name__ == '__main__':
    main()
