import codecs
import os
topics_data = []
final_data = []
my_list = []
rm = ",:;?/-!."
topics_set = set()
with codecs.open(os.path.abspath("/Users/dara/Desktop/Projects/python-extractor/new-dataset.csv")) as f:
    for line in f:
        a = line.split(',')
        for t in a:
            # print(t)
            if t == 'reply':
                t = 'no reply'
            if t == 'network' or t == 'slow':
                t = 'slow network'
            if t == 'sembilan' or t == 'negeri':
                t = 'sembilan negeri'
            if t.rstrip() == 'worst' or t.rstrip() == 'telco':
                t = 'worst telco'
            if t.rstrip() == 'customer' or t.rstrip() == 'service':
                t = 'customer service'
            topics_data.append(t.rstrip())

for i in topics_data:
    if i not in my_list:
        if i != 'celcom':
            print([i, topics_data.count(i)])
            final_data.append([i, topics_data.count(i)])
            my_list.append(i)
    # number_set.add(topics_data.count(i))
# print(final_data)
# print  # (number_set)

# print(topics_data.count(i))
