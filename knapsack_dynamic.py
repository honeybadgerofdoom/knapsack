import pprint, sys

DEBUG = False

def knapSack(W, weights, values, n):
    print()

    M = [[0 for x in range(W + 1)] for x in range(n + 1)] 

    for i in range(n + 1):
        if DEBUG: print(f'i: {i}')
        for w in range(W + 1):
            if DEBUG: print(f'w: {w}')
            if i == 0 or w == 0: 
                M[i][w] = 0
            elif weights[i-1] <= w:
                value_to_store = max(values[i-1] + M[i-1][w-weights[i-1]], M[i-1][w])
                if DEBUG: print(f'Storing {value_to_store}')
                M[i][w] = value_to_store 
            else: 
                M[i][w] = M[i-1][w]
    print(f'Result: {M[n][W]}')
    return M


def printKnapsack(knapsack):
    print()
    print("Knapsack Table")
    rows = len(knapsack)-1
    columns = len(knapsack[0])-1
    pad_length = len(str(knapsack[rows][columns]))
    for row in range(len(knapsack)):
        for column in range(len(knapsack[row])):
            knapsack[row][column] = str(knapsack[row][column]).zfill(pad_length)
    # pprint.pprint(knapsack)
    for row in knapsack:
        print(row)


def solutionSet(n, W, M, weights, values):
    print()
    print("Solution Set")
    S = []
    j = W
    for i in reversed(range(1, n+1)):
        if DEBUG: print(f'i: {i}')
        if DEBUG: print(f'j: {j}')
        if M[i][j] > M[i-1][j]:
            value_in_set = values[i-1]
            if DEBUG: print(f'Found keeper: {value_in_set}')
            S.append(value_in_set)
            j -= weights[i-1]

    pprint.pprint(S)
    print()

   
def main():
    values = [4,13,11,6] 
    weights = [2,7,5,4] 
    W = 10
    n = len(values)
    knapsack = knapSack(W, weights, values, n)
    printKnapsack(knapsack)
    solutionSet(n, W, knapsack, weights, values)


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1: DEBUG = args[1]
    main()

