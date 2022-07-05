
matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]

result_1 = sum(matriz[0])
result_2 = sum(matriz[1])
result_3 = sum(matriz[2])
result_4 = sum(matriz[3])

matriz[0].append(result_1)
matriz[1].append(result_2)
matriz[2].append(result_3)
matriz[3].append(result_4)

print(matriz)

