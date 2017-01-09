import re
import string
from collections import Counter


def read_data(datafile):
    data = []
    info = {}
    f = open(datafile, 'r+')
    for line in f:
        data.append(parse(line))
    data = zip(*data)
    info['name'] = data[0]
    info['id'] = map(int, data[1])
    info['checksum'] = data[2]
    f.close()
    return info


def parse(line):
    return re.match('(.+)-(.+)\[(.+)\]', line).groups()


def real_info(info):
    real_index = []
    for i, (name, checksum) in enumerate(zip(info['name'], info['checksum'])):
        if valid(name, checksum):
            real_index.append(i)
    for key in info.keys():
        info[key] = [info[key][i] for i in real_index]
    return info


def top_counts(name):
    counts = Counter(name.replace('-', ''))
    counts = sorted(counts.items(), key=lambda x: x[0])
    counts.sort(key=lambda x: x[1], reverse=True)
    top = [k[0] for k in counts][:5]
    return top


def valid(name, checksum, min_match=5):
    results = [n in top_counts(name) for n in checksum]
    if sum(results) == min_match:
        return True
    else:
        return False


def decrypt(info):
    decrypted_names = []
    alphabet = string.ascii_lowercase * 2
    dash = '-'
    for name, sector in zip(info['name'], info['id']):
        decrypted_name = ''
        shift = sector % 26
        for letter in name:
            if letter is not dash:
                decrypted_name += alphabet[alphabet.index(letter) + shift]
            else:
                decrypted_name += ' '
        decrypted_names.append(decrypted_name)
    info['decrypted_name'] = decrypted_names
    return info


def find_northpole(info):
    for name, sector in zip(info['decrypted_name'], info['id']):
        searched_name = re.search(r'(.*)(north)(.*)(pole)(.*)', name.lower())
        if searched_name is not None:
            print(searched_name.string, sector)
            break


def main():
    # Part 1 Returns 158835
    unfiltered_info = read_data('input4.txt')
    info = real_info(unfiltered_info)
    print(sum(info['id']))
    # Part 2
    decrypted_info = decrypt(info)
    find_northpole(decrypted_info)


if __name__ == '__main__':
    main()
