def quick_sort(data):
    def quick_sort_recursive(arr, left, right):
        i, j = left, right
        pivot = arr[(left + right) // 2]
        while i <= j:
            while arr[i] < pivot and i < right:
                i += 1
            while pivot < arr[j] and j > left:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i, j = i + 1, j - 1
        if left < j:
            quick_sort_recursive(arr, left, j)
        if i < right:
            quick_sort_recursive(arr, i, right)
    quick_sort_recursive(data, 0, len(data) - 1)
    
data = [-45, -91, -81, 65, 39, -37, 90, -94, -12, -24, 53, 59, -63, -2, -11, 29, 42, 51, -45, 36, 31, -68, -77, 0, 92, -32, 17, -56, 51, -49, 1, 40, 79, 92, 9, -73, -70, -49, 68, -9, 5.1573, 5.1437, 8.1421, 3.1625, 12.3187, 2.8465, 78.0454, -32.6666, -51.9204, -31.9391, -30.6136, -12.1411, -4.7172, -6.1189, 15.1574, 10.8995, 21.0344, 49.7912, -56.6149, -27.4997, 17.1503, -1.5368, -31.3245, -17.5386, 6.9865, -27.8045, 27.2986, -17.9399, 50.6482, -30.2363, 5.5773, -42.5887, -20.2617, -16.6110, 11.2374, 26.3797, 8.4136, -10.4460, 22.8337, 22.3688, 3.3657, 15.9949, 11.5583, -27.6349, 21.2679, -18.4016, -16.9097, 4.9545, -8.6101, -3.6910]
quick_sort(data)
print(data)