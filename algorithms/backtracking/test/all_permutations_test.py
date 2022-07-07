import sys


# def generate_all_permutations(sequence, M) -> None:
#     create_state_space_tree(
#         sequence, [], M, [0 for i in range(len(sequence))])


# def create_state_space_tree(
#     sequence,
#     current_sequence,
#     index,
#     index_used
# ) -> None:
#     if index == len(sequence):
#         print(current_sequence)
#         return
#     for i in range(len(sequence)):
#         if not index_used[i]:
#             current_sequence.append(sequence[i])
#             index_used[i] = True
#             create_state_space_tree(
#                 sequence,
#                 current_sequence,
#                 index + 1,
#                 index_used
#             )
#             current_sequence.pop()
#             index_used[i] = False


# def generate_all_permutations(sequence, M) -> None:
#     create_state_space_tree(
#         sequence,
#         [],
#         M,
#         [0 for i in range(len(sequence))]
#     )

# def create_state_space_tree(
#     sequence,
#     current_sequence,
#     index,
#     index_used
# ) -> None:
#     if index == len(sequence):
#         print(current_sequence)
#         return
#     for i in range(len(sequence)):
#         if not index_used[i]:
#             current_sequence.append(sequence[i])
#             index_used[i] = True
#             create_state_space_tree(
#                 sequence,
#                 current_sequence,
#                 index + 1,
#                 index_used
#             )
#             current_sequence.pop()
#             index_used[i] = False


# def generate_all_permutations(sequence, M) -> None:
#     create_state_space_tree(
#         sequence,
#         [],
#         M,
#         [0 for i in range(len(sequence))]
#     )


# def create_state_space_tree(
#     sequence,
#     current_sequence,
#     index,
#     index_used
# ) -> None:
#     if index == len(sequence):
#         print(current_sequence)
#         return
#     for i in range(len(sequence)):
#         if not index_used[i]:
#             current_sequence.append(sequence[i])
#             index_used[i] = True
#             create_state_space_tree(
#                 sequence,
#                 current_sequence,
#                 index + 1,
#                 index_used
#             )
#             current_sequence.pop()
#             index_used[i] = False

# def generate_all_permutations(sequence, M) -> None:
#     create_state_space_tree(
#         sequence,
#         [],
#         M,
#         [0 for i in range(len(sequence))]
#     )

# def create_state_space_tree(
#     sequence,
#     current_sequence,
#     index,
#     index_used
# ) -> None:
#     if index == len(sequence):
#         print(current_sequence)
#         return
#     for i in range(len(sequence)):
#         if not index_used[i]:
#             current_sequence.append(sequence[i])
#             index_used[i] = True
#             create_state_space_tree(
#                 sequence,
#                 current_sequence,
#                 index + 1
#             )
#             current_sequence.pop()
#             index_used[i] = False


def generate_all_permutations(sequence, M) -> None:
    create_state_space_tree(
        sequence,
        [],
        M,
        [0 for i in range(len(sequence))]
    )


def create_state_space_tree(
    sequence,
    current_sequence,
    index,
    index_used,
) -> None:
    if index == len(sequence):
        print(current_sequence)
        return
    for i in range(len(sequence)):
        if not index_used[i]:
            current_sequence.append(sequence[i])
            index_used[i] = True
            create_state_space_tree(
                sequence,
                current_sequence,
                index + 1,
                index_used
            )
            current_sequence.pop()
            index_used[i] = False


N, M = map(int, sys.stdin.readline().split())

generate_all_permutations([i for i in range(1, N + 1)], abs(M-N))
