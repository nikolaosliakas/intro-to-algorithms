import math


def compare_insertion_with_merge_sort():
    n: int = 2
    insert_less_than_merge = True
    while insert_less_than_merge:
        insert_sort_steps = calc_insert_sort(n)
        merge_sort_steps = calc_merge_sort(n)

        insert_less_than_merge = insert_sort_steps < merge_sort_steps
        n += 1

    print(f"Insert Sort takes {insert_sort_steps} many steps to execute on {n} many inputs.")
    print(f"Merge Sort takes {merge_sort_steps} many steps to execute {n} many inputs.")


def calc_insert_sort(n: int) -> float:
    return 8 * n ** 2


def calc_merge_sort(n: int) -> float:
    return 64 * n * math.log2(n)


def smallest_value_n():
    n_sq_less_than_two_n: bool = True
    n: int = 1
    # n_sq_runtime = 0.0
    # two_power_n_runtime = 0.0
    while n_sq_less_than_two_n:
        # n_sq_runtime = 100 * n ** 2
        # two_power_n_runtime = 2 ** n
        if 100 * n ** 2 < 2 ** n: break
        n += 1
    # print(n_sq_runtime)
    # print(two_power_n_runtime)
    print(f"The smallest n where nSquared runtime is faster than 2PowerN is: {n}")



if __name__ == '__main__':
    compare_insertion_with_merge_sort()
    smallest_value_n()
