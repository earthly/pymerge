from timeit import timeit
import random
import matplotlib.pyplot as plt
import textwrap
import merge
from heapq import merge as hmerge

def merge_fewer_branches(a,b):
#    m1 = merge.merge_latin(a, b)
   m1 = merge.merge_fewer_branches(a, b)

def merge_special(a,b):
#    m1 = merge.merge_latin(a, b)
   m1 = merge.merge_int(a, b)

def merge_simple(a,b):
   m1 = merge.merge(a, b)

def sort(a,b):
   m2 = a + b 
   m2.sort()

def merge_sorted_lists(l1, l2):
        sorted_list = []
        i = 0
        j = 0
        while i < len(l1) or j < len(l2):
            if i == len(l1):
                sorted_list.append(l2[j])
                j += 1
                continue
            if j == len(l2):
                sorted_list.append(l1[i])
                i += 1
                continue
            if l1[i] < l2[j]:
                sorted_list.append(l1[i])
                i += 1
            else:
                sorted_list.append(l2[j])
                j += 1
        return sorted_list

def heap_merge(a,b):
    list(hmerge(a,b))
num_data_points = 200
step = 100
methods = [
    # "merge_sorted_lists(a,b)",
    # "heap_merge(a,b)",
    # "sort(a,b)",
    "merge_simple(a,b)",
    "merge_special(a,b)",
    "merge_fewer_branches(a,b)",
]
labels = [
    # "merge_sorted_lists(a,b) #Python Two List Merge",
    # "list(heapq.merge(a,b)) #Python Iterable Merge",
    # "(a+b).sort() #TimSort",
    "merge.merge(a,b) #general C Merge",
    "merge.merge_special(a,b) #specialized C Merge",
    "merge_fewer_branches(a,b)",
]

x = list(range(0, num_data_points * step, step))
y = [[] for _ in methods]
for i in x:
    list_a = random.sample(range(1, 100000000), i) 
    list_b = random.sample(range(1, 100000000), int(i/4)) 
    list_a.sort()
    list_b.sort()
    # list_a = [str(x) for x in list_a]
    # # list_b = [str(x) for x in list_b]
    setup = textwrap.dedent(f"""\
        from __main__ import merge_special, merge_simple, sort, merge_sorted_lists, heap_merge, merge_fewer_branches
        a = {list_a}; b = {list_b}
        """)
    for method_index, method in enumerate(methods):
        y[method_index].append(timeit(method, setup=setup, number=30))
    print(i, "out of", num_data_points * step)

ax = plt.axes()
for method_index, method in enumerate(labels):
    ax.plot(x, y[method_index], label=method)
ax.set(xlabel="number of elements lists", ylabel="time (s) (lower is better)")
ax.legend()
plt.show()
# plt.savefig('perf.png')
