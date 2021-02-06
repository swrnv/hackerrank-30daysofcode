actual = list(map(int, input().split()))
da, ma, ya = actual

expected = list(map(int, input().split()))
de, me, ye = expected

fine = 0

if ya>ye:
    fine = 10000
elif ya == ye:
    if ma>me:
        fine=(ma-me)*500
    elif ma==me and da>de:
        fine = (da-de)*15
print(fine)