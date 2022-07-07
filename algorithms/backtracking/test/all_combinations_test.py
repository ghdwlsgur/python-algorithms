
import sys
from typing import List


# def generate_all_combinations(N: int, M: int) -> List[List[int]]:
#     result: List[List[int]] = []
#     create_all_state(1, N, M, [], result)
#     return result


# def create_all_state(
#     increment: int,
#     total_number: int,
#     level: int,
#     current_list: List[int],
#     total_list: List[List[int]]
# ) -> None:
#     if level == 0:
#         total_list.append(current_list[:])
#         return

#     for i in range(increment, total_number - level + 2):
#         current_list.append(i)
#         create_all_state(
#             i + 1,
#             total_number,
#             level - 1,
#             current_list,
#             total_list
#         )
#         current_list.pop()


# def print_all_state(total_list: List[List[int]]) -> None:
#     for i in total_list:
#         print(*i)

# def generate_all_combinations(N: int, M: int) -> List[List[int]]:
#     result: List[List[int]] = []
#     create_all_state(1, N, M, [], result)
#     return result


# def create_all_state(
#     increment: int,
#     total_number: int,
#     level: int,
#     current_list: List[int],
#     total_list: List[List[int]]
# ) -> None:
#     if level == 0:
#         total_list.append(current_list[:])
#         return

#     for i in range(increment, total_number - level + 2):
#         current_list.append(i)
#         create_all_state(
#             i + 1,
#             total_number,
#             level - 1,
#             current_list,
#             total_list
#         )
#         current_list.pop()


# def print_all_state(total_list: List[List[int]]) -> None:
#     for i in total_list:
#         print(*i)


def generate_all_combinations(N: int, M: int) -> List[List[int]]:
    result: List[List[int]] = []
    create_all_state(1, N, M, [], result)
    return result


def create_all_state(
    increment: int,
    total_number: int,
    level: int,
    current_list: List[int],
    total_list: List[List[int]]
) -> None:
    if level == 0:
        total_list.append(current_list[:])
        return

    for i in range(increment, total_number - level + 2):
        current_list.append(i)
        create_all_state(
            i + 1,
            total_number,
            level - 1,
            current_list,
            total_list
        )
        current_list.pop()


def print_all_state(total_list: List[List[int]]) -> None:
    for i in total_list:
        print(*i)
