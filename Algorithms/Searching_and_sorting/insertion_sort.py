import random


def generate_random_list(n):
    # n is the length of the list
    my_list = []
    for i in range(n):
        my_list.append(random.randint(0, 4*n))
    return my_list


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        for j in range(i, 0, -1):
            if my_list[j] < my_list[j-1]:
                my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
            else:
                break


def main():
    my_list = generate_random_list(20)
    print(my_list)
    insertion_sort(my_list)
    print(my_list)


if __name__ == '__main__':
    main()
