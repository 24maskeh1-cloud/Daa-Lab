def obst_successful_only(P):
    n = len(P)
    C = [[0 for _ in range(n+2)] for _ in range(n+2)] 
    R = [[0 for _ in range(n+2)] for _ in range(n+2)] 

 
    for i in range(1, n+1):
        C[i][i] = P[i-1]
        R[i][i] = i
        C[i][i-1] = 0 

    for d in range(1, n): 
        for i in range(1, n-d+1):
            j = i + d
            C[i][j] = float('inf')
            for k in range(i, j+1): 
                left = C[i][k-1]
                right = C[k+1][j] if k+1 <= n else 0
                subcost = left + right
                sumP = sum(P[i-1:j])
                total = subcost + sumP
                if total < C[i][j]:
                    C[i][j] = total
                    R[i][j] = k

    print("Minimum OBST Cost:", round(C[1][n], 4))
    print("Cost Matrix (C):")
    for row in C[1:n+1]:
        print([round(x, 4) for x in row[1:n+1]])
    print("Root Matrix (R):")
    for row in R[1:n+1]:
        print(row[1:n+1])

P = [0.1, 0.2, 0.4, 0.3]
obst_successful_only(P)