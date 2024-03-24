import math

def compare_insertion_with_merge_sort():
    n: int = 2
    insert_less_than_merge = True
    while(insert_less_than_merge):
        insert_sort_steps = calc_insert_sort(n)
        merge_sort_steps = calc_merge_sort(n)

        insert_less_than_merge = insert_sort_steps < merge_sort_steps
        n+=1

    print(f"Insert Sort takes {insert_sort_steps} many steps to execute on {n} many inputs.")
    print(f"Merge Sort takes {merge_sort_steps} many steps to execute {n} many inputs.")
def calc_insert_sort(n:int) -> float:
    return 8 * n**2

def calc_merge_sort(n:int) -> float:
    return 64 * n * math.log2(n)

if __name__ == '__main__':
    compare_insertion_with_merge_sort()
