import random
import time


#Name: Adarsh kumar singh
#Roll No: 2501730458
#Course: B.Tech CSE AI/ML
#Section: G




# -----------------------------
# INSERTION SORT
# -----------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr


# -----------------------------
# MERGE SORT
# -----------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])


    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# -----------------------------
# QUICK SORT
# -----------------------------
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# -----------------------------
# TIMING FUNCTION
# -----------------------------
def measure_time(sort_func, arr):
    temp = arr.copy()

    start = time.time()

    if sort_func.__name__ == "quick_sort":
        sort_func(temp, 0, len(temp) - 1)
    else:
        temp = sort_func(temp)

    end = time.time()

    return (end - start) * 1000  # milliseconds


# -----------------------------
# DATASET GENERATOR
# -----------------------------
def generate_datasets(size):
    random.seed(42)

    random_list = [random.randint(1, 100000) for _ in range(size)]
    sorted_list = sorted(random_list)
    reverse_list = sorted_list[::-1]

    return random_list, sorted_list, reverse_list


# -----------------------------
# CORRECTNESS CHECK
# -----------------------------
def check_correctness():
    test = [5, 2, 9, 1, 5, 6]

    print("Correctness Check:")
    print("Original:", test)

    print("Insertion:", insertion_sort(test.copy()))
    print("Merge:", merge_sort(test.copy()))

    temp = test.copy()
    quick_sort(temp, 0, len(temp) - 1)
    print("Quick:", temp)


# -----------------------------
# MAIN RUNNER
# -----------------------------
def run_experiments():
    sizes = [1000, 5000, 10000]

    with open("output.txt", "w") as f:

        for size in sizes:
            rand, sorted_l, rev = generate_datasets(size)

            output = f"\n========== SIZE: {size} ==========\n"
            print(output)
            f.write(output)

            for name, data in [
                ("Random", rand),
                ("Sorted", sorted_l),
                ("Reverse", rev),
            ]:

                output = f"\n{name} Data:\n"
                print(output)
                f.write(output)

                t1 = measure_time(insertion_sort, data)
                t2 = measure_time(merge_sort, data)
                t3 = measure_time(quick_sort, data)

                line1 = f"Insertion Sort: {t1:.2f} ms\n"
                line2 = f"Merge Sort: {t2:.2f} ms\n"
                line3 = f"Quick Sort: {t3:.2f} ms\n"

                print(line1 + line2 + line3)
                f.write(line1 + line2 + line3)


# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    check_correctness()
    run_experiments()