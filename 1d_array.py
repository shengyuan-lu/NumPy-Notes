import numpy as np

# Vectors, 1D Arrays

if __name__ == '__main__':

    a = np.array([1.,2.,3.])

    print(a)

    print(a.dtype) # np.float64
    print(a.shape) # (3,)

    b = np.zeros(3, int)

    c = np.zeros_like(a)



