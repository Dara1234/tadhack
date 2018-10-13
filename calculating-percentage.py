import codecs
import os
topics_data = []
final_data = []
my_list = []
rm = ",:;?/-!."
topics_set = set()
number_set = set()
with codecs.open(os.path.abspath("/Users/dara/Desktop/Projects/python-extractor/new-dataset.csv")) as f:
    for line in f:
        a = line.split(',')
        for t in a:
            # print(t)
            topics_data.append(t)

for i in topics_data:
    # print(i)
    if i not in my_list:
        print([i, topics_data.count(i)])
        final_data.append([i, topics_data.count(i)])
        my_list.append(i)
    # number_set.add(topics_data.count(i))
# print(final_data)
# print  # (number_set)

# print(topics_data.count(i))
