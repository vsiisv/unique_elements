def unique_elements_in_list(list_of_elements):
    return len(set(list_of_elements))


list_of_random_numbers = [4, 8, 15, 16, 23, 42, 4, 8, 15, 16, 23, 42]
list_of_random_elements = [1, "sdf", 2, "sdf", 3, "sdf", 1, "sdf", 2, "sdf", 3, "sdf"]


print(
    f"Количество уникальных элементов в списке = {unique_elements_in_list(list_of_random_elements)}"
)
print(
    f"Количество уникальных чисел в списке = {unique_elements_in_list(list_of_random_numbers)}"
)
