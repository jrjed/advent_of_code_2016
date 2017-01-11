import re


def read_text(datafile):
    with open(datafile, 'r') as f:
        text = ''.join([line for line in f]).strip()
    f.close()
    return text


def find_marker(text, index='all'):
    regex = re.compile(r'\((\d+)x(\d+)\)')
    if index is not 'all':
        return regex.match(text, index)
    else:
        return re.search(regex.pattern, text)


def decompress(text):
    result = ''
    i = 0
    while i < len(text):
        match = find_marker(text, i)
        if match:
            start = int(match.end())
            end = start + int(match.group(1))
            n = int(match.group(2))
            chunk = text[start: end]
            result += chunk * n
            i = start + len(chunk)
        else:
            result += text[i]
            i += 1
    return result


def full_decompress(text):
    '''
    It works for resonably sized strings (e.g. the test cases).
    It would too long to run on test input so implemented Peter Norvigs
    strategy (not shown here) simply to get an answer, but again, this works
    ... you just need a super computer.
    '''
    markers = find_marker(text)
    result = text
    while markers:
        result = decompress(result)
        markers = find_marker(result)
    return result


def norvig(text):
    length = 0
    i = 0
    while i < len(text):
        match = find_marker(text, i)
        if match:
            interval, n = map(int, match.groups())
            i = int(match.end())
            length += n * norvig(text[i: i + interval])
            i += interval
        else:
            length += 1
            i += 1
    return length


def main():
    # Part 1
    print(len(decompress(read_text('input9.txt'))))
    # Part 2
    #print(len(full_decompress(read_text('input9.txt'))))
    print(norvig(read_text('input9.txt')))


if __name__ == '__main__':
    main()
