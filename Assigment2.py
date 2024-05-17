"""
Name: Rahul Reddaveni
Student ID: C0930162
"""
import random


def main():
    """
    1. Create list that contain10 random numbers between 10 – 100
    Then do the following
    ➢ Print the list
    ➢ Calculate and display the sum of all elements
    ➢ Reverse a list and display it
    """
    random_number_list = [random.randint(10, 100) for x in range(10)]
    print(random_number_list)
    sum_of_elements = sum(random_number_list)
    print(f"Sum of elements in {random_number_list} is {sum_of_elements}")
    random_number_list.reverse()
    print(random_number_list)

    """
    2. Write a program to add two lists index-wise Given a two Python list.
    Write a program to iterate both lists simultaneously and display items from list1 in original order
    and items from list2 in reverse order.
    """
    list1 = [1, 2, 3, 4]
    list2 = [9, 10, 11, 19]
    list_length = len(list1)
    print(f"list1 - {list1}")
    print(f"list2 - {list2}")
    for idx in range(list_length):
        print(f"List 1 element - {list1[idx]} List 2 element - {list2[list_length - 1 - idx]}")

    """
    3.You have given a Python list. Write a program to find value 20 in the list, and if it is present,
    replace it with 200
    """
    list1 = [10, 32, 323, 43, 20]
    print(list1)
    list1 = [200 if x == 20 else x for x in list1]
    print(f"Modified list - {list1}")

    """
    4. Write program that store users info , username and email , in a dictionary ( use email as key
    name as value) Allow user to enter info about 5 users ( use loop
    """
    user_info_dict = {}
    for idx in range(5):
        email = input(f"enter email of user {idx + 1}: ")
        user_name = input(f"enter user name of user {idx + 1}: ")
        user_info_dict[email] = user_name
    print(f"Registered user details {user_info_dict}")


if __name__ == '__main__':
    main()
