import random

def generate_random_sequence(length=50):
    x = range(length)
    random.shuffle(x)
    return x


[2, 6, 1, 8, 5, 4, 0, 3, 9, 7]

def lis2(sequence):
    lengths = []
    for i, s in enumerate(sequence):
        # If it's the first item, the max length can only be 1
        if i == 0:
            lengths.append(1)
        else:
            possibles = []
            for j, length in enumerate(lengths):
                # if the item is bigger than the end of the other subsequences
                if s > sequence[j]:
                    # add one
                    possibles.append(length + 1)
                else:
                    # otherwise it's smaller and can't be added
                    possibles.append(1)
            # add the longest out of all possibilities
            lengths.append(max(possibles))
    return max(lengths)



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

