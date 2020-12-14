from collections import Counter
from playStats.descriptive_stats import frequency
from playStats.descriptive_stats import mode

if __name__ == '__main__':

    # test conuter
    data = [2, 2, 2, 2, 1, 1, 1, 3, 3]
    counter = Counter(data)
    print(counter.most_common())
    print(counter.most_common()[0][1])

    # test frequency
    freq = frequency(data)
    print(freq)

    # test mode
    data = [2, 2, 2, 1, 1, 1, 3, 3]
    mode_elements, mode_count = mode(data)
    print(mode_elements)
    print(mode_count)
