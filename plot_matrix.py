# TODO: import ...
import numpy as np
import matplotlib.image as plt
def generate_random_matrix(m, n):
    image_array = np.random.randint(0, 2, (m, n))
    return image_array


def save_matrix(matrix, file_name):
    plt.imsave(file_name, matrix)
    
if __name__ == "__main__":
    matrix = generate_random_matrix(10, 10)
    save_matrix(matrix, "example.jpg")
