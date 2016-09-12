import random


sample = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'

def genCode(length):
    if len(sample) >= length * 10:
        return random.sample(sample * 10, length)
    else:
        return random.sample(sample * (length//len(sample) + 1) * 10, length)



def genCodes(number, length):
    sets = set()
    while len(sets) < number:
        aa = ''.join(genCode(length))
        if aa not in sets:
            sets.add(aa)
    print(sets)


if __name__ == "__main__":
    main()
            


