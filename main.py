# 221RDB323
# Danila Sinicins
# 17. grupa

def parallel_processing(n, m, data):
    output = []
    thrds = [0]*n
    for j in range(m):
        timeMin = thrds[0]
        thrdMin = 0
        for i in range(1, n):
            if thrds[i]<timeMin:
                timeMin=thrds[i]
                thrdMin=i
        output.append((thrdMin, timeMin))
        thrds[thrdMin] += data[j]
    return output

def main():
    n = 0
    m = 0
    n, m = map(int, input().split())

    data = []
    data = list(map(int, input().split()))

    result = parallel_processing(n,m,data)
    
    for pair in result:
        print(pair[0],pair[1])

if __name__ == "__main__":
    main()
