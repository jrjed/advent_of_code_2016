import re
def read_ip(datafile):
    with open(datafile) as f:
        ips = zip(*[line.split() for line in f])
    f.close()
    return list(ips[0])

def tls_search():
    pass

def parse_ip(ip):
    exterior_abba = re.search(r'(.*)(\w+)(\w+)\2\1(.*)', ip)
    interior_abba = re.search(r'(.*)\[(\w+)(\w+)\2\1\](.*)', ip)
    if exterior_abba is not None and interior_abba is None:
        return True
    else:
        return False

for ip in read_ip('test.txt'):
    print parse_ip(ip)

