# LinearAlgebra
最近在bilibili上看宋浩老师的线性代数视频，发现里面的很多计算方式很适合写成代码，决定慢慢写一下；每个方法都使用同济教材习题册中的答案进行了一些自测
- /determinant 逆序数与行列式的计算，余子式和代数余子式的计算
- /matrix 矩阵的加减法，数乘，矩阵相乘，矩阵转置，伴随矩阵/逆矩阵的计算，阶梯形矩阵，矩阵的秩
- /vector 向量相加，点积，数乘，施密特正交化
## 感慨
线性代数的大题其实都不算太难，求行列书，求矩阵的逆，求线性方程组的基础解系，求特征值特征向量，对角化矩阵等等，都是特别有套路的题。就是计算量实在太大了，把这一部分转换成程序交给计算机来机械处理就方便多了。
## todo
- 计算精度是个大问题，2/3总是被表示成0.666667，1/5都会被表示成0.1999999，咋整呢
- 求矩阵特征值也没啥好办法，感觉只能穷举[-100,100]之间的整数，虽然这基本能解决书上的习题，但是作用不大鸭
