import multiprocessing, time

def read_info(name):
    all_data = []
    with open(name) as f:
        line = f.readline()
        while line is not None and line != "":
            all_data.append(line)
            line = f.readline()
    return f'Done reading {name}'


filenames = [f'./file {number}.txt' for number in range(1, 5)]

'''
lts = time.time()
for f in filenames:
    read_info(f)
print('Linear time elapsed', time.time() - lts)
#Linear time elapsed 2.2668933868408203
'''


if __name__ == "__main__":
    mts = time.time()
    with multiprocessing.Pool() as p:
        p.map(read_info, filenames)
    print('Multiprocess time elapsed', time.time() - mts)

#Multiprocess time elapsed 0.8374595642089844
