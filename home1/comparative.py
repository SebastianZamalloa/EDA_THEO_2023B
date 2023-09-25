import random
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def compare_sorting_algorithms(arr_lengths):
    insertion_sort_times = []
    merge_sort_times = []

    for n in arr_lengths:
        arr = [random.randint(1, 1000) for _ in range(n)]

        start_time = time.time()
        insertion_sort(arr.copy())
        insertion_sort_times.append(time.time() - start_time)

        start_time = time.time()
        merge_sort(arr.copy())
        merge_sort_times.append(time.time() - start_time)

    return insertion_sort_times, merge_sort_times

arr_lengths = [50,100,200,500,1000,2000,5000]
insertion_sort_times, merge_sort_times = compare_sorting_algorithms(arr_lengths)

plt.plot(arr_lengths, insertion_sort_times, label="Insertion Sort")
plt.plot(arr_lengths, merge_sort_times, label="Merge Sort")
plt.xlabel("Tamaño del arreglo")
plt.ylabel("Tiempo de ejecución (segundos)")
plt.legend()
plt.title("Comparación de Insertion Sort y Merge Sort")
plt.show()
