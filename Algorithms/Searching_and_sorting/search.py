def contains(my_list, element):
    for e in my_list:
        if e == element:
            return True
    return False


def main():
    my_list = [2, 5, 7, 1, 22, 44, 55, 67, 89]
    print(my_list)
    print(contains(my_list, 89))


if __name__ == '__main__':
    main()
