#n = list(input().split())
n = (int(i) for i in input().split())
a = 10
print(a)
def max(n):
    maxx = 0
    for i in range(0, len(n)):
        if n[i] > maxx:
            maxx = n[i]
        elif maxx == n[i]:
            return i
    return maxx

def pow(n):
    return max([12,198])+n

print(pow(12))