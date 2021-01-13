def find_max_ones(n):
    if not n:
        return 0
    bin_num = bin(n)[2:]
    return len(max(bin_num.replace('0', ' ').split(), key=len))


if __name__ == '__main__':
    n = int(input())
    max_ones = find_max_ones(n)
    print(max_ones)
