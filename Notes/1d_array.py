import numpy as np

# Vectors, 1D Arrays

def basics():

    print('BASICS')

    # Vector initialization

    a = np.array([1.,2.,3.]) # [1. 2. 3.]

    print(a)

    print(a.dtype) # np.float64
    print(a.shape) # (3,)

    b = np.zeros(3, int)

    print(b) # [0 0 0]

    c = np.zeros_like(a) # [0. 0. 0.]

    print(c)

    np.zeros(3)

    print(np.zeros(3)) # [0. 0. 0.]

    np.ones(3)

    print(np.ones(3)) # [1. 1. 1.]

    np.empty(3)

    print(np.empty(3)) # [_ _ _]

    np.full(3, 7.)

    print(np.full(3, 7.)) # [7. 7. 7.]

    np.array([1, 2, 3])

    print(np.array([1,2,3])) # [1 2 3]

    print()


def array_init():

    print('Array Init')

    # Array Initialization

    # np.arange(start, stop, step)

    np.arange(6) # stop

    print(np.arange(6)) # [0 1 2 3 4 5]

    np.arange(2, 6) # start, stop

    print(np.arange(2, 6)) # [2 3 4 5]

    np.arange(1, 6, 2) # start, stop, step

    print(np.arange(1, 6, 2)) # [1 3 5]

    # np.linespace(start, stop, num)

    np.linspace(0, 0.5, 6)

    print(np.linspace(0, 0.5, 6)) # [0.  0.1 0.2 0.3 0.4 0.5]

    print()


def vector_indexing():

    print('Vector indexing')

    a = np.arange(1, 6)

    print(a)

    #    [1 2 3 4 5]
    # id  0 1 2 3 4

    print(a[1]) # 2

    print(a[2:4]) # [3 4]

    print(a[-2:]) # [4 5]

    print(a[::2])  # [1 3 5]

    # fancy indexing

    print(a[[1,3,4]]) # [2 4 5]

    a[2:4] = 0

    print(a) # [1 2 0 0 5]

    # Note:
    # In numpy c = a[:] does not copy
    # to copy, use a.copy()

    print()


def test():

    print('Test')

    a = np.arange(5, 15)
    print(a)
    result = a[::3]

    print(result)

    a = np.arange(1, 5)
    print(a)
    result = a[::-1]
    print(result)






if __name__ == '__main__':

    basics()

    array_init()

    vector_indexing()

    test()



