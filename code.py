# LCM-and-GCD

# LCM- Least Common Multiple
# GCD(HCF) - Gretest Common Diffrence aka Highest Common Multiple.
# product = lcm * gcd

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b%a,a)


def lcm(a,b):
    prod = a*b
    hcf = gcd(a,b)
    return prod // hcf


t = int(input())
while t:
    x,y = map(int,input().split())
    print('GCD = {} lcm = {}'.format(gcd(x,y),lcm(x,y)))
    t = t-1
