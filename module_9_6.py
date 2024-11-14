import itertools


def all_variants(text: str):
    l = len(text)
    for cur_size in range(1, l+1):
        cur_pos = 0
        while cur_pos <= l-cur_size:
            sub = text[cur_pos:cur_pos+cur_size]
            yield sub
            cur_pos += 1


a = all_variants("abc")
for i in a:
    print(i)
