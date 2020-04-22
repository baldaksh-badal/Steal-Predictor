def slicer(list_to_slice: list) -> 'list':
    """Slices the data provided to it and returns it as a list of
    data in 2 piece chunks. Starting at index position 0."""
    i = 0
    list_to_return = []
    while i < (len(list_to_slice)):
        list_to_return.append(list_to_slice[i: (i + 2):])
        i += 2
    return list_to_return


def slicer_odd(list2slice: list) -> 'list':
    """Slices the data provided to it and returns it as a
        list of data in 2 piece chunks. Starting at index position 1."""
    i = 1
    list2return = [list2slice[0:1]]
    while i < (len(list2slice)):
        list2return.append(list2slice[i: (i + 2):])
        i += 2
    return list2return


def logger(file_name: str) -> 'None':
    """It receives sequence, result and tries as input and logs
        it into the file name variable 'tries' number of times."""
    tries = int(input("Enter number of inputs: "))
    i = 0
    while i < tries:
        sequence = input("Enter sequence of signals used: ").upper()
        result = input("Enter result (Steal or NoSteal): ").upper()
        ifsteal = is_steal(result)
        with open(file_name, 'a') as log:
            print(sequence, ifsteal, file=log, end=' | ')
        i += 1


def is_steal(result: str) -> 'int':
    """Converts Steal and NoSteal into a True or False value."""
    if result.lower() == 'steal':
        stealnt = 1
    else:
        stealnt = 0
    return stealnt


def extractor(file_name: str) -> 'dict':
    """Makes work easier by returning the dictionary of sequence
     and its respective result from the given text file."""
    with open(file_name) as log:
        data = {}
        for item in log:
            huge_list = item.split(' | ')
            for element in huge_list:
                data0list = element.split(' ')
                key = data0list[0]
                val = data0list[1]
                data[key] = bool(int(val))
            return data


def true_chunker(data: dict) -> 'list':
    """Returns a list of all the chunks that
        could potentially be the correct sequence."""
    true_chunks = []
    for key in data:
        if data[key]:
            sliced_keys = slicer(key)
            more_sliced_keys = slicer_odd(key)
            for item in sliced_keys:
                true_chunks.append(item)
            for more_item in more_sliced_keys:
                true_chunks.append(more_item)

    for chunk in true_chunks.copy():
        if len(chunk) < 2:
            true_chunks.remove(chunk)
    return true_chunks


def false_chunker(data: dict) -> 'list':
    """Returns a list of the chunks of all the sequences with the result False."""
    false_chunks = []
    for key in data:
        if not data[key]:
            sliced_keys = slicer(key)
            more_sliced_keys = slicer_odd(key)
            for item in sliced_keys:
                false_chunks.append(item)
            for more_item in more_sliced_keys:
                false_chunks.append(more_item)
    for chunk in false_chunks.copy():
        if len(chunk) < 2:
            false_chunks.remove(chunk)
    return false_chunks


def true_slicer(data: dict) -> 'list':
    """Returns a list of lists of sliced sequences with result True."""
    true_slices = []
    for key in data:
        chunk_list = []
        if data[key]:
            for item in slicer(key):
                chunk_list.append(item)
            for item in slicer_odd(key):
                chunk_list.append(item)
        for chunk in chunk_list.copy():
            if len(chunk) < 2:
                chunk_list.remove(chunk)

        true_slices.append(chunk_list)
        for sliced_keys_list in true_slices.copy():
            if len(sliced_keys_list) == 0:
                true_slices.remove(sliced_keys_list)
    return true_slices


def find_intersection(container: list) -> 'list':
    """Returns the common slice from the list of LISTS of slices.Given enough
     input, it would it would return list of only one chunk."""
    i = len(container)
    x = 1
    prediction = container[0]

    while i-x != 0:
        prediction = list(set(prediction) & set(container[x]))
        x += 1
    return prediction
