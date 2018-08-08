matriz = [[0 for x in range(3)] for y in range(3)]

matriz[0][0] = 200
matriz[0][1] = 0
matriz[0][2] = 200
matriz[1][0] = 180
matriz[1][1] = 0
matriz[1][2] = 200
matriz[2][0] = 120
matriz[2][1] = 0
matriz[2][2] = 255

soma = 0

media = 128.33

for x in range(3):
    for y in range(3):
        soma = soma + (matriz[x][y] - media) * (matriz[x][y] - media)

print(soma / 9)
