def buble_sort(array):
    while True:
        corrected = False
        for i in range(0, len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                corrected = True
        if not corrected:
            return array


def insert_sort():
    pass

def fast_sort():
    pass


def main():
    array = [8, 0, 1, 2, 3, 4, 9, 7]
    print(array)

    new_array = buble_sort(array)
    print(new_array)



main()