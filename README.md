## bloom filter

布隆过滤器，类似于 BitMap ，也有一个很大的比特存储空间 N。

然后对数据经过 K 次不同的哈希，在比特表里将每个哈希值的位置置为1。

如果某条数据的每个哈希值都已被置1，说明他可能有重复。

布隆过滤器会出现误判，比如说其实没有重复，但是被判断成重复。但是不会有错判，将一个有重复的值，判断为没有重复。

python 的里的布隆过滤器，常用 bitarray 实现。

其主要参数为 N,K,哈希函数，影响布隆过滤器的效率。
