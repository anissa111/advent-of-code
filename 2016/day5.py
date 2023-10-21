import hashlib

raw = 'ffykfhsq'


def get_password_1(raw):
    i = 0
    password = ''
    while len(password) < 8:
        md5hash = hashlib.md5((raw + str(i)).encode()).hexdigest()
        if md5hash[:5] == '00000':
            password = password + md5hash[5]

        i += 1

    return password


def get_password_2(raw):
    i = 0
    found = [False, False, False, False, False, False, False, False]
    password = [0, 0, 0, 0, 0, 0, 0, 0]
    while not all(found):
        md5hash = hashlib.md5((raw + str(i)).encode()).hexdigest()
        if md5hash[:5] == '00000' and md5hash[5].isdigit():
            if int(md5hash[5]) < 8 and not found[int(md5hash[5])]:
                password[int(md5hash[5])] = md5hash[6]
                found[int(md5hash[5])] = True
        i += 1

    return ''.join(password)


print(f'Part 1: {get_password_1(raw)}')
print(f'Part 2: {get_password_2(raw)}')
