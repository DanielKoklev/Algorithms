import random

def generate_random_list(n):
    # n is the length of the list
    my_list = []
    for i in range(n):
        my_list.append(random.randint(0, 4*n))
    return my_list

def bubble_sort(my_list):
    for i in range(len(my_list), 1, -1):
        for x in range(1, len(my_list)):
            if my_list[x-1] > my_list[x]:
                my_list[x-1], my_list[x] = my_list[x], my_list[x-1]


def main():
    # my_list = [2, 5, 6, 8, 10, 7, 3, 1, 9, 4]
    my_list = generate_random_list(10)
    print(my_list)
    bubble_sort(my_list)
    print(my_list)


if __name__ == '__main__':
    main()
