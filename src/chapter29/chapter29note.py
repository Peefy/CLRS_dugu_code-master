# coding:utf-8
# usr/bin/python3
# python src/chapter29/chapter29note.py
# python3 src/chapter29/chapter29note.py
"""

Class Chapter29_1

Class Chapter29_2

Class Chapter29_3

Class Chapter29_4

Class Chapter29_5

"""
from __future__ import absolute_import, division, print_function

import numpy as np

class Chapter29_1:
    """
    chapter29.1 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter29.1 note

        Example
        ====
        ```python
        Chapter29_1().note()
        ```
        """
        print('chapter29.1 note as follow')
        print('第29章 线性规划')
        print('在给定有限的资源和竞争约束情况下，很多问题都可以表述为最大化或最小化某个目标')
        print('如果可以把目标指定为某些变量的一个线性函数,而且如果可以将资源的约束指定为这些变量的等式或不等式',
            '则得到一个线性规划问题.线性规划出现在许多世纪应用中')
        print('比如如下线性规划问题')
        print('argmin(x1+x2+x3+x4)')
        print('满足约束条件')
        print('-2 * x1 + 8 * x2 +  0 * x3 + 10 * x4 >= 50')
        print(' 5 * x1 + 2 * x2 +  0 * x3 +  0 * x4 >= 100')
        print(' 3 * x1 - 5 * x2 + 10 * x3 -  2 * x4 >= 25')
        print(' x1 >= 0; x2 >= 0; x3 >= 0; x4 >= 0')
        print('一般线性规划')
        print('  在一般线性规划的问题中,希望最优化一个满足一组线性不等式约束的线性函数。',
            '已知一组实数a1,a2,...,an和一组变量x1,x2,...,xn,在这些变量上的一个线性函数f定义为：',
            'f(x1,x2,...,xn)=a1x1+a2x2+...+anxn')
        print('  如果b是一个实数而f是一个线性函数,则等式f(x1,x2,...,xn)=b是一个线性等式')
        print('  不等式f(x1,x2,...,xn)<=b和f(x1,x2,...,xn)>=b都是线性不等式')
        print('用线性约束来表示线性等式或线性不等式')
        print('在线性规划中,不允许严格的不等式')
        print('正式地说,线性规划问题是这样的一种问题,要最小化或最大化一个受限一组有限的线性约束的线性函数')
        print('如果是要最小化,则称此线性规划为最小化线性规划;如果是要最大化,则称此线性规划为最大化线性规划')
        print('虽然有一些线性规划的多项式时间算法。但是单纯形法是最古老的线性规划算法.',
            '单纯形算法在最坏的情况下不是在多项式时间内运行,但是相当有效,而且在实际中被广泛使用')
        print('比如双变量的线性规划直接在笛卡尔直角坐标系中表示出可行域和目标函数曲线即可')
        print('线性规划概述')
        print('  非正式地,在标准型中的线性规划是约束为线性不等式的线性函数的最大化',
            '而松弛型的线性规划是约束为线性等式的线性函数的最大化')
        print('  通常使用标准型来表示线性规划,但当描述单纯形算法的细节时,使用松弛形式会比较方便')
        print('受m个线性不等式约束的n个变量上的线性函数的最大化')
        print('如果有n个变量,每个约束定义了n维空间中的一个半空间.这些半空间的交集形成的可行区域称作单纯形')
        print('目标函数现在成为一个超平面,而且因为它的凸性,故仍然有一个最优解在单纯形的一个顶点上取得的')
        print('单纯形算法以一个线性规划作为输入,输出它的一个最优解.从单纯形的某个顶点开始,执行一系列的迭代',
            '在每次迭代中,它沿着单纯形的一条边从当前定点移动到一个目标值不小于(通常是大于)当前顶点的相邻顶点',
            '当达到一个局部的最大值,即一个顶点的目标值大于其所有相邻顶点的目标值时,单纯形算法终止.')
        print('因为可行区域是凸的而且目标函数是线性的,所以局部最优事实上是全局最优的')
        print('将使用一个称作\"对偶性\"的概念来说明单纯形法算法输出的解的确是最优的')
        print('虽然几何观察给出了单纯形算法操作过程的一个很好的直观观察',
            '但是在讨论单纯形算法的细节时,并不显式地引用它.相反地，采用一种代数方法,首先将已知的线性规划写成松弛型,即线性等式的集合',
            '这些线性等式将表示某些变量,称作\"基本变量\",而其他变量称作\"非基本变量\".从一个顶点移动到另一个顶点伴随着将一个基本变量',
            '变为非基本变量,以及将一个非基本变量变为基本变量.',
            '这个操作称作一个\"主元\",而且从代数的观点来看,只不过是将线性规划重写成等价的松弛型而已')
        print('识别无解的线性规划,没有有限最优解的线性规划,以及原点不是可行解的线性规划 ')
        print('')
        print('')
        print('')
        print('')
        print('')
        # python src/chapter29/chapter29note.py
        # python3 src/chapter29/chapter29note.py

class Chapter29_2:
    """
    chapter29.2 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter29.2 note

        Example
        ====
        ```python
        Chapter29_2().note()
        ```
        """
        print('chapter29.2 note as follow')
        # python src/chapter29/chapter29note.py
        # python3 src/chapter29/chapter29note.py

class Chapter29_3:
    """
    chapter29.3 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter29.3 note

        Example
        ====
        ```python
        Chapter29_3().note()
        ```
        """
        print('chapter29.3 note as follow')
        # python src/chapter29/chapter29note.py
        # python3 src/chapter29/chapter29note.py

class Chapter29_4:
    """
    chapter29.4 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter29.4 note

        Example
        ====
        ```python
        Chapter29_4().note()
        ```
        """
        print('chapter29.4 note as follow')
        # python src/chapter29/chapter29note.py
        # python3 src/chapter29/chapter29note.py

class Chapter29_5:
    """
    chapter29.5 note and function
    """
    def __init__(self):
        pass

    def note(self):
        """
        Summary
        ====
        Print chapter29.5 note

        Example
        ====
        ```python
        Chapter29_5().note()
        ```
        """
        print('chapter29.5 note as follow')
        # python src/chapter29/chapter29note.py
        # python3 src/chapter29/chapter29note.py

chapter29_1 = Chapter29_1()
chapter29_2 = Chapter29_2()
chapter29_3 = Chapter29_3()
chapter29_4 = Chapter29_4()
chapter29_5 = Chapter29_5()

def printchapter29note():
    """
    print chapter29 note.
    """
    print('Run main : single chapter twenty-nine!')
    chapter29_1.note()
    chapter29_2.note()
    chapter29_3.note()
    chapter29_4.note()
    chapter29_5.note()

# python src/chapter29/chapter29note.py
# python3 src/chapter29/chapter29note.py

if __name__ == '__main__':  
    printchapter29note()
else:
    pass
