# coding=utf-8


import bitarray
import hashlib


# TODO struct unpack
md5 = lambda x: int(hashlib.md5(x).hexdigest(), 16)
sha1 = lambda x: int(hashlib.sha1(x).hexdigest(), 16)


class BFilter(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.bit_array = bitarray.bitarray(capacity, endian='little')
        self.bit_array.setall(False)
        self.hash_func = [md5, sha1, hash]

    def hash(self, value):
        hashes = []
        for func in self.hash_func:
            hashes.append(func(value))
        return hashes

    def add(self, value):
        hashes = self.hash(value)
        if hashes in self:
            return False
        for h in hashes:
            self.bit_array[h % self.capacity] = 1
        return True

    def __contains__(self, item):
        if isinstance(item, list):
            hashes = item
        else:
            hashes = self.hash(item)

        return all(map(lambda x: self.bit_array[x % self.capacity], hashes))


if __name__ == '__main__':
    s = BFilter(100)
    print s.add('https://baidu.com')
    print s.add('http://baidu.com')
    print s.add('https://ele.me')
    print s.add('https://baidu.com')
