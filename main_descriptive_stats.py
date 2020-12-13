from collections import Counter

if __name__ == '__main__':
    data = [2, 2, 2,2 ,1,1,1,3,3]
    counter = Counter(data)
    print(counter.most_common())
    print(counter.most_common()[0][1])