from insertion_sort import *


def contains(my_list, element):
    for e in my_list:
        if e == element:
            return True
        elif e > element:
            return False
    return False


def main():
    my_list = [2, 5, 7, 1, 22, 44, 55, 67, 89]
    insertion_sort(my_list)
    print(my_list)
    print(contains(my_list, 4))


if __name__ == '__main__':
    main()
