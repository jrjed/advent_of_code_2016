import re


def read_ips(datafile):
    with open(datafile) as f:
        ips = zip(*[line.strip().split() for line in f])
    f.close()
    return list(ips[0])


def tls_test(ip):
    good_abba = re.search(r'([a-z])(?!\1)([a-z])\2\1', ip) 
    bad_abba = re.search(r'\[([a-z]*)([a-z])(?!\2)([a-z])\3\2([a-z]*)\]', ip)
    if good_abba is not None and bad_abba is None:
        return True
    else:
        return False


def ssl_test(ip):
    pass


def main():
    print(sum(map(tls_test, read_ips('input7.txt'))))
        

if __name__ == '__main__':
    main()
