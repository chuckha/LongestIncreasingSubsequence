import random

def generate_random_sequence(length=50):
    x = range(length)
    random.shuffle(x)
    return x

def lis(sequence):
    list_of_sequences = [[sequence[0]]]
    for item in sequence:
        # case 1: item is larger than all sequence ends
        if item > list_of_sequences[-1][-1]:
            new_s = list(list_of_sequences[-1])
            new_s.append(item)
            list_of_sequences.append(new_s)
        # case 2: item is smaller than all sequence ends
        elif item < list_of_sequences[0][0]:
            list_of_sequences[0][0] = item
        # case 3: item is somewhere in the middle
        else:
            list_of_sequences = clone_extend_remove(item, list_of_sequences)

    return list_of_sequences[-1]


def clone_extend_remove(item, list_of_sequences):
    for seq in list_of_sequences[::-1]:
        if item > seq[-1]:
            new_s = list(seq)
            new_s.append(item)
            index = list_of_sequences.index(seq)
            list_of_sequences = remove_lists_of_same_length(new_s, list_of_sequences)
            list_of_sequences.insert(index+1, new_s) 
            break
    return list_of_sequences


def remove_lists_of_same_length(list1, list_of_lists):
    cp = list(list_of_lists)
    for l in list_of_lists:
        if len(list1) == len(l):
            cp.remove(l)
    return cp

