import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(x, y):
    g = gcd(x, y)
    return x // g, y // g

def process_queries(n, m, q, X, Y, queries):
    results = []
    fractions = sorted((simplify_fraction(x, y) for x in X for y in Y), key=lambda frac: frac[0] / frac[1])

    for query in queries:
        if query[0] == 1:
            k = query[1] - 1
            if 0 <= k < len(fractions):
                results.append(fractions[k])
        elif query[0] == 2:
            i, v = query[1] - 1, query[2]
            X[i] = v
            fractions = sorted((simplify_fraction(x, y) for x in X for y in Y), key=lambda frac: frac[0] / frac[1])
        elif query[0] == 3:
            i, v = query[1] - 1, query[2]
            Y[i] = v
            fractions = sorted((simplify_fraction(x, y) for x in X for y in Y), key=lambda frac: frac[0] / frac[1])

    return results

n, m, q = map(int, input("Введите n, m и q (через пробел): ").split())
X = list(map(int, input(f"Введите {n} элементов массива X (через пробел): ").split()))
Y = list(map(int, input(f"Введите {m} элементов массива Y (через пробел): ").split()))

queries = []
for _ in range(q):
    query = list(map(int, input("Введите запрос: ").split()))
    queries.append(query)

results = process_queries(n, m, q, X, Y, queries)
print("Результаты запросов:")
for x, y in results:
    print(x, y)