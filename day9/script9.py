import re

def read_text(datafile):
    with open(datafile, 'r') as f:
        text = ''.join([line for line in f]).strip()
    f.close()
    return text


def decompress(text):
    result = ''
    regex = re.compile(r'\((\d+)x(\d+)\)')
    i = 0
    while i < len(text):
        match = regex.match(text, i)
        if match:
            start  = int(match.end())
            end = start + int(match.group(1))
            n = int(match.group(2))
            chunk = text[start: end]
            result += chunk * n
            i = start + len(chunk)
        else:
            result += text[i]
            i += 1
    return len(result)

print decompress(read_text('input9.txt'))
