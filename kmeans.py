from math import sqrt, inf

def dist(a, b):
    return sqrt(sum([((a[i] - b[i]) ** 2) for i in range(len(list(a)))]))

def form(c):
    return tuple(map(lambda p: float(format(p, "0.3f")), list(c)))

def kmeans(points, centroids, label_offset=1):
    print()
    print("\t", end='\t')
    for i in range(len(centroids)):
        print(f"dist(C{i + label_offset})", end='\t')
    print("Cluster")

    clusters = [[] for _ in centroids]
    for p in points:
        print(form(p), end='\t')
        min_dist = inf
        index = 0
        for i, c in enumerate(centroids):
            d = float(format(dist(c, p), ".3f"))
            print(f"{d}", end='\t\t')
            if d < min_dist:
                min_dist = d
                index = i
        print(index + label_offset)
        clusters[index].append(p)
    print()

    updated_centroids = []
    for c in clusters:
        x = 0
        y = 0
        for a, b in c:
            x += a
            y += b
        cp = float(format(x / len(c), ".3f")), float(format(y / len(c), ".3f"))
        updated_centroids.append(cp)

    return updated_centroids, clusters

def read_h(file='kmeans.txt'):
    lines = open(file, "r").read().split('\n')
    points = []
    for line in lines:
        points.append(tuple(map(lambda x: float(x), line.split(' '))))
    return points

def read_v(file='kmeans.txt'):
    lines = open(file, "r").read().split('\n')
    dims = []
    for line in lines:
        dims.append(list(map(lambda x: float(x), line.split(' '))))
    n = len(dims[0])
    points = []
    for i in range(n):
        p = []
        for d in dims:
            p.append(d[i])
        points.append(tuple(p))

    return points

points = read_v()
centroids = [(0.06, 0.37), (1.75, 1.35)]
print("Points:", points)
print("Centroids:", centroids)

centroids, clusters = kmeans(points, centroids, label_offset=1)
print("Updated Centroids:", str(centroids).replace("[", "").replace("]", ""))

