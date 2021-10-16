

def binary_search(my_list, element):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        print(my_list[mid])
        if my_list[mid] == element:
            return True
        else:
            if my_list[mid] > element:
                high = mid - 1
            else:
                low = mid + 1
    return False


def main():
    my_list = [-29, -14, -12, -8, -7, 3, 7, 11, 19, 25, 35, 48, 54, 58, 60]
    print(my_list)
    print(binary_search(my_list, 19))


if __name__ == '__main__':
    main()
