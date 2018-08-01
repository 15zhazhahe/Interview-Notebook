## 【EASY】867. 转置矩阵（Transpose Matrix）

思路：转置一个矩阵，即把一个$n\times m$的矩阵变为$m \times n$，直接复制就好了即 $ans[i][j]=A[j][i]$

**代码：**[CPP](https://github.com/15zhazhahe/Interview-Notebook/blob/master/LeetCode/Array/code/CPP/transpose-matrix.cpp)&nbsp;&nbsp;&nbsp;&nbsp;[Python](https://github.com/15zhazhahe/Interview-Notebook/blob/master/LeetCode/Array/code/Python/transpose-matrix.py)

## 【EASY】561. 数组拆分I（Array Partition I）

思路：分n组，两两一组，取出每组里面的最小值，然后使得所有组的权重和最大。为了使得值大的元素不被掩盖，所以每组分配的时候，应该是两个数尽可能接近，所以直接排个序，相邻的划分为一组即可。

看到讨论区有用桶排的(空间换时间)，不过感觉这是建立在数据范围已经确立的基础上，感觉如果是作为面试的话，可以先答快排，再问时间优化时再进一步答桶排

**代码：**[CPP](https://github.com/15zhazhahe/Interview-Notebook/blob/master/LeetCode/Array/code/CPP/array-partition-i.cpp)&nbsp;&nbsp;&nbsp;&nbsp;[Python](https://github.com/15zhazhahe/Interview-Notebook/blob/master/LeetCode/Array/code/Python/array-partition-i.py)


## 【EASY】118. 杨辉三角（Pascal's Triangle）

思路：题面的gif已经表示的很清楚了，然后观察一下样例，可以找到递推式$ans[i][j] = ans[i-1][j]+ans[i-1][j-1]$，然后考虑一下边界条件就可以写出来了。

**代码：**[CPP](https://github.com/15zhazhahe/Interview-Notebook/blob/master/LeetCode/Array/code/CPP/pascals-triangle.cpp)&nbsp;&nbsp;&nbsp;&nbsp;[Python](https://github.com/15zhazhahe/Interview-Notebook/blob/master/LeetCode/Array/code/Python/pascals-triangle.py)

## 【EASY】566. 重塑矩阵（Reshape the Matrix）

思路：可以使用两个指针在原数组上进行移动，指向的元素加到新的数组里，一次列指针移动到最后一个元素时，就让行指针往下移一行，列指针置零。

**代码：**[CPP](https://github.com/15zhazhahe/Interview-Notebook/blob/master/LeetCode/Array/code/CPP/reshape-the-matrix.cpp)&nbsp;&nbsp;&nbsp;&nbsp;[Python](https://github.com/15zhazhahe/Interview-Notebook/blob/master/LeetCode/Array/code/Python/reshape-the-matrix.py)
