from collections import Counter
from playStats.descriptive_stats import frequency
from playStats.descriptive_stats import mode
from playStats.descriptive_stats import median
from playStats.descriptive_stats import mean
from playStats.descriptive_stats import rng
from playStats.descriptive_stats import quartile
from playStats.descriptive_stats import variance
from playStats.descriptive_stats import std
from playStats.descriptive_stats import covariance, cor

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

    # test median
    data = [1, 4, 2, 3]
    print(median(data))

    # test mean
    data = [1, 4, 2, 3, 5, 99]
    print(mean(data))

    # test rng
    print(rng(data))

    # test quartile
    data = [1, 4, 2, 3, 5, 8]
    print(quartile(data))

    # test variance
    data = [1, 4, 2, 3, 5, 8]
    print(variance(data))

    # test std_variance
    print(std(data))

    # 测试协方差，相关系数
    score = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    happy = [1, 3, 2, 6, 4, 5, 8, 10, 9, 7]
    print(covariance(score, happy))
    print(cor(score, happy))
