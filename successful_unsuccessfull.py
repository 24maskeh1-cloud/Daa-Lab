def obst_successful_unsuccessful(P, Q):
    n = len(P)
    C = [[0 for _ in range(n+2)] for _ in range(n+2)] 
    W = [[0 for _ in range(n+2)] for _ in range(n+2)] 
    R = [[0 for _ in range(n+2)] for _ in range(n+2)] 

   
    for i in range(1, n+2):
        C[i][i-1] = Q[i-1]
        W[i][i-1] = Q[i-1]

    for l in range(1, n+1): 
        for i in range(1, n-l+2):
            j = i + l - 1
            C[i][j] = float('inf')
            W[i][j] = W[i][j-1] + P[j-1] + Q[j]
            for r in range(i, j+1):
                t = C[i][r-1] + C[r+1][j] + W[i][j]
                if t < C[i][j]:
                    C[i][j] = t
                    R[i][j] = r
    print("Minimum OBST Cost:", round(C[1][n], 4))
    print("Cost Matrix (C):")
    for row in C[1:n+1]:
        print([round(x, 4) for x in row[1:n+1]])
    print("Root Matrix (R):")
    for row in R[1:n+1]:
        print(row[1:n+1])

P = [0.1, 0.2, 0.4, 0.3]
Q = [0.05, 0.1, 0.05, 0.05, 0.1]
obst_successful_unsuccessful(P, Q)