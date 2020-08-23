# coding=utf-8

import bitarray
import random
import matplotlib.pyplot as plt


def generate(n):
    # 不考虑2月29日生的同学
    bit_array = bitarray.bitarray(365)
    bit_array.setall(False)

    for i in range(n):
        bit_array[random.randrange(365)] = 1

    return n - bit_array.count()


def calculate():
    # wrong calculate solution
    for i in range(1, 40):
        rate = generate(i * 10) / (i * 10.0)
        print i*10, rate


def exist_two_same(total=1000):
    ys = []
    for i in range(2, 366):
        exist = 0
        for _ in range(total):
            bit_array = bitarray.bitarray(365)
            bit_array.setall(False)
            for _ in range(i):
                r = random.randrange(365)
                if bit_array[r]:
                    exist += 1
                    break
                bit_array[r] = 1
        # print i, exist / float(total)
        ys.append(exist / float(total))
    return range(2, 366), ys


def same_with_me(total=1000):
    ys = []
    for i in range(2, 366):
        same = 0
        me = random.randrange(365)
        for _ in range(total):
            for _ in range(i):
                if random.randrange(365) == me:
                    same += 1

        # print i, same, same / float(total)
        ys.append(same / float(total))
    return range(2, 366), ys


def draw():
    plt.xlabel("frequency")
    plt.ylabel("probability")
    ex, ey = exist_two_same()
    sx, sy = same_with_me()
    plt.plot(ex, ey, color="skyblue", label="exist_two_same")
    plt.plot(sx, sy, color="yellow", label="same_with_me")
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    # calculate()
    # exist_two_same()
    # same_with_me()
    draw()
