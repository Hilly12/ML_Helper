from math import exp, sqrt, pi

def mean(xs):
    return sum(xs) / len(xs)

def stdev(xs):
    m = mean(xs)
    return sqrt(sum([((x - m) ** 2) for x in xs]) / len(xs))

def normal(x, mean, stdev):
    return exp(-(((x - mean) ** 2) / (2 * (stdev ** 2)))) / (stdev * sqrt(2 * pi))

# a = sum([normal(3.13, xi, 1) for xi in [7.42, 2.28, 3.45, 7.17, 1.75]]) / 5

# xs = [7.42, 2.28, 3.45, 7.17, 1.75]
# m = mean(xs)
# s = stdev(xs)
# print(normal(3.13, m, s))

# sm = 0
# for xi in xs:
#     n = normal(3.13, xi, 1)
#     s += n
#     print(f"+ {n} ")
# sm /= len(xs)

# print(sm)

# GME

print("Expectation")
xs = [5.92, 2.28, 3.85, 5.17, 1.75]
pik = [0.5, 0.5]
means = [3.34, 6.12]
stds = [1, 1]
rik = [[0] * len(pik) for i in xs]
for i, xi in enumerate(xs):
    pkxi = []
    for k in range(len(pik)):
        p = float(format(normal(xi, means[k], stds[k]), ".6f"))
        print(f"p{k + 1}(x{i + 1}) = {p}")
        pkxi.append(p)
    
    sm = float(format(sum([pik[j] * pkxi[j] for j in range(len(pkxi))]), ".6f"))
    print(f"Σ πk pjx{i + 1} = {sm}")
    
    for k in range(len(pik)):
        r = float(format((pik[k] * pkxi[k]) / sm, ".4f"))
        rik[i][k] = r
        print(f"r{i + 1}{k + 1} = {r}")

print("\nMaximisation")

for k in range(len(pik)):
    n = sum([rik[i][k] for i in range(len(xs))])
    print(f"pi{k + 1} = {format(n, '0.4f')} / {len(xs)} = {format(n / len(xs), '0.4f')}")

nmeans = []
for k in range(len(pik)):
    den = sum([rik[i][k] for i in range(len(xs))])
    print(f"mean {k + 1} = 1/{format(den, '0.4f')}", end=' ')
    num = 0
    for i, x in enumerate(xs):
        num += rik[i][k] * x
    res = float(format(num / den, "0.4f"))
    print(f"({format(num, '0.6f')}) = {res}")
    nmeans.append(res)

for k in range(len(pik)):
    den = sum([rik[i][k] for i in range(len(xs))])
    print(f"std {k + 1} = 1/{format(den, '0.4f')}", end=' ')
    num = 0
    for i, x in enumerate(xs):
        num += rik[i][k] * ((x - nmeans[k]) ** 2)
    res = float(format(num / den, "0.4f"))
    print(f"({format(num, '0.6f')}) = {res}")

print()

a = normal(1.75, 6.12, 1)
print(a)