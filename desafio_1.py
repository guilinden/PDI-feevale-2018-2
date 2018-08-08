import numpy as np
import imageio
import statistics
import matplotlib.pyplot as plt

#matrix = imageio.imread('C:\\Users\\glind\\Pictures\\Figura_Desafio_1.png', as_gray=True)
matrix = imageio.imread('C:\\Users\\glind\\Pictures\\bitcoin.jpg', as_gray=True)

soma = 0

cell_numbers = matrix.shape[1] * matrix.shape[0]

for x in range(matrix.shape[0]):
    for y in range(matrix.shape[1]):
        soma += matrix[x][y]
       
media = soma / cell_numbers

soma = 0

for x in range(matrix.shape[0]):
    for y in range(matrix.shape[1]):
        soma += (matrix[x][y] - media) * (matrix[x][y] - media)

variancia = soma / cell_numbers

matrix_as_array = matrix.flatten()
histograma = [0] * 256

print(cell_numbers)

for x in matrix_as_array.astype(np.int):
    histograma[x] += 1

pixels = [0] * 256

for x in range(256):
    pixels[x] = x

sorted_array = sorted(matrix_as_array)

plt.bar(pixels, histograma)
plt.title('Histograma')
plt.annotate('Media: ' + str("%.2f" % media) + '  Variancia: ' + str("%.2f" % variancia) + '  Moda: ' + str("%.2f" % statistics.mode(sorted_array)) + '  Mediana : ' + str("%.2f" % statistics.median(sorted_array)) , (0,0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top')
plt.show()

                    
