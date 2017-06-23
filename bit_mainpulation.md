# bit manipulation
- &
- |
- ~
- ^
- \<\<
- \>\>

see orgin source[url](https://discuss.leetcode.com/topic/50315/a-summary-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently)

## logical manipulation
and, or, not

## 左移右移
```
8<<1 = 16 = 8*2
8<<2 = 32 = 8*4
8<<3 = 64 = 8*8
8<<4 = 128= 8*16
```
```
7<<1 = 14 = 7*2
7<<2 = 28 = 7*4
7<<3 = 56 = 7*8
7<<4 = 112= 7*16
```
```
69>>1 = 34 = 69 / 2
69>>2 = 17 = 69 / 4
69>>3 = 8  = 69 / 8
```

# Examples
计算给定数二进制有多少个 1，例如 5，二进制是 101，ans=2
```python
def count_one(n):
	count = 0
	while n:
		n = n & (n - 1)
		count += 1
	return count
```
- n = n & n - 1
```
n=15 1111
15 & 14 = 14 = 15 - 1
14 & 13 = 12 = 14 - 2
12 & 11 = 8  = 12 - 4
8  & 7  = 0  = 8  - 8

n = 13 1101
13 & 12 = 12 = 13 - 1
12 & 11 = 8  = 12 - 4
8  & 7  = 0  = 8  - 8
```
```python
def isPowerOfFour(n):
    return not (n & (n - 1)) and bool(n & 0x55555555)
	# check the 1-bit location;
```
- n & n -1
	- 由上可得，如果 n 为 2 的倍数，则等于 0，相当于只有一个 1
	- 如果 n 为奇数的话，n&(n-1) 其结果肯定是 n-1
- n & 0x55555555
	如果 n 为 4 的倍数，则返回 n 本身（但是不唯一，取两个的交集即可）

## ^ 技巧
删除完全相同的数字和保存奇数，或保存不同的位，并删除相同的位

###　两个整数的和
```python
def getsum(a, b):
	return a if b==0 else getsum(a^b, (a&b)<<1)
```
### 找缺失的数
给定一个 n，0,1,2,3,4...n 找到缺失的数，nums=[0,1,3], 缺失 2
```python
def missingNumber(nums):
	int ret = 0
	for i in len(nums):
		ret ^= i
		ret ^= nums[i]
	return ret^=len(nums)
```
```
0^7 = 7
7^8 = 15
15^6 = 9
9^8 = 1
1^6 = 7
```
a^b 当 b 的个数为偶数的时候，就会返回 a 原先值，相当于负负得正

## | 技巧
尽可能保存多个 1bit
### 找到最大的 2 的幂指数
尽可能的保留 1
```
def largest_power(n):
	n = n | (n>>1)
	n = n | (n>>2)
	n = n | (n>>4)
	n = n | (n>>8)
	n = n | (n>>16)
	print bin(n)
	# 0b11111
	return (n+1)>>1
```

### 翻转位
```
def reverseBits(n):
	mask = 1 << 31
	res =0
	for i in range(32):
		if n & 1:
			res |= mask
		mask >>= 1
		n >>= 1
	return res
```
- n & 1, n 如果是奇数则返回 1，否则为 0
- mask >>=1 对 mask / 2
