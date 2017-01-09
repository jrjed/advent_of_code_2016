import hashlib


def code_cracker(st, door_number):
    code = [None] * 8
    i = j = 0
    while None in code:
        piece = hashlib.md5(st + str(i)).hexdigest()
        i += 1
        if piece.startswith('00000'):
            if door_number == 1:
                code[j] = piece[5]
                j += 1
            elif door_number == 2:
                if (piece[5].isdigit() and int(piece[5]) < 8 and
                        code[int(piece[5])] is None):
                    code[int(piece[5])] = piece[6]
    return ''.join(code)


def main():
    door_id = 'uqwqemis'
    # Part 1
    print(code_cracker(door_id, 1))
    # Part 2
    print(code_cracker(door_id, 2))


if __name__ == '__main__':
    main()
