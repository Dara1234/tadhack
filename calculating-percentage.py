import codecs
import os
from operator import itemgetter
from terminaltables import AsciiTable
topics_data = []
final_data = []
my_list = []
list_data = []
rm = ",:;?/-!."
topics_set = set()
with codecs.open(os.path.abspath("/Users/dara/Desktop/Projects/python-extractor/new-dataset.csv")) as f:
    for line in f:
        a = line.split(',')
        for t in a:
            # print(t)
            if t.rstrip() == 'reply' or t.rstrip() == 'enquiry' or t.rstrip() == 'customer':
                t = 'no reply to customer enquiry'
            if t == 'network' or t == 'slow' or t == 'speed' or t == 'sembilan' or t == 'negeri' or t == 'pajam':
                t = 'slow network speed in pajam negeri sembilan'
            if t.rstrip() == 'worst' or t.rstrip() == 'telco':
                t = 'worst telco'
            if t.rstrip() == 'customer' or t.rstrip() == 'services':
                t = 'customer services'
            if t.rstrip() == 'money' or t.rstrip() == 'missing':
                t = 'money missing'
            if t.rstrip() == 'respond' or t.rstrip() == 'issue':
                t = 'respond issue'
            if t.rstrip() == 'change' or t.rstrip() == 'without' or t.rstrip() == 'notify' or t.rstrip() == 'terms':
                t = 'change terms without notifying'
            if t.rstrip() != 'become' and t.rstrip() != 'since' and t.rstrip() != 'still' and t.rstrip() != '.....':
                topics_data.append(t.rstrip())

list_data.append(['Issue', 'Occurence', 'Percentage'])
for i in topics_data:
    if i not in my_list:
        if i != 'celcom':
            # print([i, topics_data.count(i), (topics_data.count(i)/50)*100])
            final_data.append(
                {'issue': i, 'occurence': topics_data.count(i), 'percentage': (topics_data.count(i)/50)*100})
            my_list.append(i)
    # number_set.add(topics_data.count(i))
# print(final_data)
newlist = sorted(final_data,  key=itemgetter('percentage'), reverse=True)
for i in newlist:
    # print(i)
    list_data.append([i.get('issue'), i.get('occurence'), i.get('percentage')])

table = AsciiTable(list_data)
print(table.table)
# print(newlist)
# print  # (number_set)

# print(topics_data.count(i))
