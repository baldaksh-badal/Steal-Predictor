import tools


tools.logger('predictor.log')


data4work = tools.extractor('predictor.log')

true_slice_list = tools.true_slicer(data4work)

true_chunks = tools.true_chunker(data4work)
false_chunks = tools.false_chunker(data4work)

for true_slice in true_slice_list:
    for chunk in true_slice.copy():
        if chunk in false_chunks:
            true_slice.remove(chunk)
            true_chunks.remove(chunk)


print(tools.find_intersection(true_slice_list))
