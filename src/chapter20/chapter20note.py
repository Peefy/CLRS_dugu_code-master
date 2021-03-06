# coding:utf-8
# usr/bin/python3
# python src/chapter20/chapter20note.py
# python3 src/chapter20/chapter20note.py
'''

Class Chapter20_1

Class Chapter20_2

Class Chapter20_3

Class Chapter20_4

'''
from __future__ import absolute_import, division, print_function

import math as _math
import random as _random
import time as _time
from copy import copy as _copy
from copy import deepcopy as _deepcopy
from random import randint as _randint

import numpy as np
from numpy import arange as _arange
from numpy import array as _array
from numpy import * 

if __name__ == '__main__':
    import fibonacciheap as fh
else:
    from . import fibonacciheap as fh

class Chapter20_1:
    '''
    chpater20.1 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter20.1 note

        Example
        ====
        ```python
        Chapter20_1().note()
        ```
        '''
        print('chapter20.1 note as follow')  
        print('第20章 斐波那契堆')
        print('二项堆可以在时间O(lgn)的最坏情况时间支持可合并堆操作INSERT,MINIMUM,',
            'EXTRACT-MIN和UNION以及操作DECREASE-KEY和DELETE')
        # !斐波那契堆不涉及删除元素的可合并堆操作仅需要O(1)的平摊时间
        print('波那契堆不涉及删除元素的可合并堆操作仅需要O(1)的平摊时间,这是斐波那契堆的好处')
        print('从理论上来看，当相对于其他操作的数目来说，EXTRACT-MIN与DELETE操作的数目较小时,斐波那契堆是很理想的')
        print(' 例如某些图问题的算法对每条边都调用一次DECRESE-KEY。对有许多边的稠密图来说，每一次DECREASE-KEY调用O(1)平摊时间加起来')
        print(' 就是对二叉或二项堆的Θ(lgn)最坏情况时间的一个很大改善')
        print(' 比如解决诸如最小生成树和寻找单源最短路径等问题的快速算法都要用到斐波那契堆')
        print('但是，从实际上看，对大多数应用来说，由于斐波那契堆的常数因子以及程序设计上的复杂性',
            '使得它不如通常的二叉(或k叉)堆合适')
        print('因此，斐波那契堆主要是具有理论上的意义')
        print('如果能设计出一种与斐波那契堆有相同的平摊时间界但又简单得多的数据结构，',
            '那么它就会有很大的实用价值了')
        # !和二项堆一样，斐波那契堆由一组树构成
        print('和二项堆一样，斐波那契堆由一组树构成，实际上，这种堆松散地基于二项堆')
        print('如果不对斐波那契堆做任何DECREASE-KEY或DELETE操作，则堆中的每棵树就和二项树一样')
        print('两种堆相比，斐波那契堆的结构比二项堆更松散一些，可以改善渐进时间界。',
            '对结构的维护工作可被延迟到方便再做')
        # !斐波那契堆也是以平摊分析为指导思想来设计数据结构的很好的例子(可以利用势能方法)
        print('斐波那契堆也是以平摊分析为指导思想来设计数据结构的很好的例子(可以利用势能方法)')
        # !和二项堆一样，斐波那契堆不能有效地支持SEARCH操作
        print('和二项堆一样，斐波那契堆不能有效地支持SEARCH操作')
        print('20.1 斐波那契堆的结构')
        # !与二项堆一样，斐波那契堆是由一组最小堆有序树构成，但堆中的树并不一定是二项树
        print('与二项堆一样，斐波那契堆是由一组最小堆有序树构成，但堆中的树并不一定是二项树')
        # !与二项堆中树都是有序的不同，斐波那契堆中的树都是有根而无序的
        print('与二项堆中树都是有序的不同，斐波那契堆中的树都是有根而无序的')
        print('每个结点x包含一个指向其父结点的指针p[x],以及一个指向其任一子女的指针child[x],',
            'x所有的子女被链接成一个环形双链表,称为x的子女表。',
            '子女表的每个孩子y有指针left[y]和right[y]分别指向其左，右兄弟')
        print('如果y结点是独子，则left[y]=right[y]=y。各兄弟在子女表中出现的次序是任意的')
        # !在斐波那契堆中采用环形双链表
        print('在斐波那契堆中采用环形双链表有两个好处。',
            '首先可以在O(1)时间内将某结点从环形双链表中去掉')
        print(' 其次，给定两个这样的表，可以在O(1)时间内将它们连接为一个环形双链表')
        print('另外一个结点中的另外两个域也很有用。结点x的子女表中子女的个数存储于degree[x]')
        print('布尔值域mark[x],指示自从x上一次成为另一个结点子女以来，它是否失掉了一个孩子')
        print('新创建的结点是没有标记的，且当结点x成为另一个结点的孩子时也是没有标记的')
        print('DECREASE-KEY操作，才会置所有的mark域为FALSE')
        print('对于给定的斐波那契堆H,可以通过指向包含最小关键字的树根的指针min[H]来访问')
        print(' 这个结点被称为斐波那契堆中的最小结点。如果一个斐波那契堆H是空的，则min[H]=None')
        print('在一个斐波那契堆中，所有树的根都通过用其left和right指针链接成一个环形的双链表，称为该堆的根表')
        print('在根表中各树的顺序可以是任意的')
        print('斐波那契堆H中目前所包含的结点个数为n[H]')
        print('势函数')
        print(' 对一个给定的斐波那契堆H，用t(H)来表示H的根表中树的棵数，用m(H)来表示H中有标记结点的个数')
        print(' 斐波那契堆H的势定义为Φ(H)=t(H)+2m(H)')
        print(' 一组斐波那契堆的势为各成分斐波那契堆的势之和。')
        print(' 假定一个单位的势可以支付常数量的工作，此处该常数足够大，',
            '可以覆盖我们可能遇到的任何常数时间的工作')
        print(' 假定斐波那契堆应用在开始时，都没有堆。于是，初始的势就为0，且根据方程，势始终是非负的')
        print(' 对某一操作序列来说，其总的平摊代价的一个上界也就是这个操作序列总的实际代价的一个上界')
        print('最大度数')
        print(' 在包含n个结点的斐波那契堆中，结点的最大度数有一个已知的上界D(n)')
        print(' 当斐波那契堆仅支持可合并堆操作时,D(n)<=[lgn]')
        print(' 当斐波那契堆还需支持DECREASE-KEY和DELETE操作时,D(n)=O(lgn)')
        # python src/chapter20/chapter20note.py
        # python3 src/chapter20/chapter20note.py

class Chapter20_2:
    '''
    chpater20.2 note and function
    '''
    def putxkeydownykey(self, heap : fh.FibonacciHeap, xkey, ykey):
        '''
        构造20.3的斐波那契堆
        '''
        ynode = heap.search(ykey)
        root = ynode
        node = fh.make_fib_node(xkey)
        fh.link(node, root)
        heap.keynum += 1

    def buildheap(self):
        '''
        构造20.3的斐波那契堆
        '''
        heap = fh.make_fib_heap()
        heap.insertkey(7)
        heap.insertkey(18)
        heap.insertkey(38)

        self.putxkeydownykey(heap, 24, 7)
        self.putxkeydownykey(heap, 17, 7)
        self.putxkeydownykey(heap, 23, 7)

        self.putxkeydownykey(heap, 26, 24)
        self.putxkeydownykey(heap, 46, 24)
        self.putxkeydownykey(heap, 35, 26)

        self.putxkeydownykey(heap, 30, 17)

        self.putxkeydownykey(heap, 21, 18)
        self.putxkeydownykey(heap, 39, 18)
        self.putxkeydownykey(heap, 52, 21)

        self.putxkeydownykey(heap, 41, 38)

        return heap

    def note(self):
        '''
        Summary
        ====
        Print chapter20.2 note

        Example
        ====
        ```python
        Chapter20_2().note()
        ```
        '''
        print('chapter20.2 note as follow')  
        print('20.2 可合并堆的操作')
        print('介绍斐波那契堆所实现的各种可合并堆操作。',
            '如果仅需要支持MAKE-HEAP,INSERT,MINIMUM,EXTRACT-MI和UNION操作')
        print('则每个斐波那契堆就只是一组\"无序的\"的二项树')
        print('无序的二项树和二项树一样，也是递归定义的')
        print('无序的二项树U0包含一个结点，一棵无序的二项树Uk包含两颗无序的二项树Uk-1')
        # !如果一个有n个结点的斐波那契堆由一组无序二项树构成，则D(n)=lgn
        print('可能要花Ω(lgn)时间向一个二项堆中插入一个结点或合并两个二项堆。',
            '当向斐波那契堆中插入新结点或者合并两个斐波那契堆时，并不去合并树')
        print(' 而是将这个工作留给EXTRACT-MIN操作，那是就真正需要找出新的最小结点了')
        print('斐波那契堆插入一个结点')
        print(' 与BINOMIAL-HEAP-INSERT过程不同，FIB-HEAP-INSERT并不对斐波那契堆中的树进行合并')
        print(' 如果连续执行了k次FIB-HEAP-INSERT操作，则k棵单结点的树被加到了根表中')
        print(' 为了确定FIB-HEAP-INSERT的平摊代价，设H为输入的斐波那契堆，H‘为结果斐波那契堆')
        print(' 于是，t(H‘)=t(H)+1,m(H‘)=m(H),且势的增加为1')
        print(' 因为实际的代价为O(1)，故平摊的代价为O(1)+1=O(1)')
        print('寻找最小结点')
        print(' 在一个斐波那契堆H中,最小的结点由指针min[H],故可以在O(1)实际时间内找到最小结点')
        print(' 又因为H的势没有变化，所以这个操作的平摊代价就等于其O(1)的实际代价')
        print('合并两个斐波那契堆')
        print(' 合并斐波那契堆H1和H2，同时破坏H1和H2，仅仅简单地将H1和H2的两根表并置,然后确定一个新的最小结点')
        print(' 势的改变为0,FIB-HEAP-UNION的平摊代价与其O(1)的实际代价相等')
        print('抽取最小结点')
        print(' 斐波那契堆FIB-HEAP-EXTRACT-MIN的操作是最复杂的。')
        print(' 先前对根表中的树进行合并这项工作是被推后的，那么到了这儿最终必须由这个操作完成')
        print(' 假定从链表中删除一个结点时，仍在表中的指针被更新，而被抽取结点的指针则无变化。该过程还用到辅助过程CONSOLIDATE')
        print(' 在抽取最小结点之前的势为t(H)+2m(H),而在此之后的势至多为(D(n)+1)+2m(H)')
        print(' 因为在该操作之后至多留下D(n)+1个根，且操作中没有任何结点被加标记，所以总的平摊代价至多为O(D(n))')
        print(' 这是因为可以通过扩大势的单位来支配O(t(H))中隐藏的常数。')
        print(' 从直觉上看，执行每一次链接的代价是由势的减少来支付的，',
            '而势的减少又是由于链接操作使根的数目减少1而引起的')
        print(' 若D(n)=O(lgn),所以抽取最小结点的平摊代价为O(lgn)')
        print('练习20.2-1 给出图20-3中所示的斐波那契堆调用FIB-HEAP-EXTRACT-MIN后得到的斐波那契堆')
        heap = self.buildheap()
        print('remove before')
        heap.print()
        heap.extractmin()
        print('remove after')
        heap.print()
        print('练习20.2-2 证明：引理19.1(二项树的性质)对无序二项树也成立')
        print('练习20.2-3 证明：如果仅需支持可合并堆操作，',
            '则在包含n个结点的斐波那契堆中结点的最大度数D(n)至多为[lgn]')
        print('练习20.2-4 McGee教授设计了一种新的基于斐波那契堆的数据结构')
        print(' McGee堆与斐波那契堆具有相同的结构，也支持可合并堆操作。',
            '各操作的实现与斐波那契堆中的相同,不同的是插入和合并在最后的步骤中做合并调整')
        print('练习20.2-5 论证：如果关键字的唯一操作是比较两个关键字，',
            '则并非所有的可合并堆操作都有O(1)的平摊时间')
        # python src/chapter20/chapter20note.py
        # python3 src/chapter20/chapter20note.py

class Chapter20_3:
    '''
    chpater20.3 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter20.3 note

        Example
        ====
        ```python
        Chapter20_3().note()
        ```
        '''
        print('chapter20.3 note as follow')
        print('20.3 减小一个关键字于删除一个结点')
        print('减小斐波那契堆中某结点的关键字，平摊时间为O(1)')
        print('从包含n个结点的斐波那契堆中删除一个结点，平摊时间O(D(n))')
        print('这些操作不包吃斐波那契堆中的所有树都是无序二项树的性质')
        print('因而可以用O(lgn)来限界最大度数D(n)')
        print('FIB-HEAP-EXTRACT-MIN和FIB-HEAP-DELETE的平摊运行时间为O(lgn)')
        print('练习20.3-1 假设一个斐波那契堆中某个根x是有标记的。')
        print(' 请解释x是如何成为有标记的根')
        print(' 另说明x有无标记对分析来说没有影响，',
            '即使他不是先被链接到另一个结点，然后又失去一个子结点的根')
        print('练习20.3-2 使用聚焦分析来证明FIB-HEAP-DECREASE-KEY的平摊时间O(1)是每个操作的平均代价')
        # python src/chapter20/chapter20note.py
        # python3 src/chapter20/chapter20note.py

class Chapter20_4:
    '''
    chpater20.4 note and function
    '''
    def note(self):
        '''
        Summary
        ====
        Print chapter20.4 note

        Example
        ====
        ```python
        Chapter20_4().note()
        ```
        '''
        print('chapter20.4 note as follow')
        print('20.4 最大度数的界')
        print('为了证明FIB-HEAP-EXTRACT-MIN和FIB-HEAP-DELETE的平摊时间为O(lgn)')
        print('必须首先证明，在包含n个结点的斐波那契堆中，任意结点的度数的上界D(n)为O(lgn)')
        print('引理20.1 设x为斐波那契堆中任一结点，且假设degree[x]=k，',
            '设y1,y2,...,yk表示按与x链接的次序排列的x的子女，从最早的到最迟的，则对i=2,3,...,k',
            '有degree[y1]>=0和degree[yi]>=i-2')
        print('引理20.2 对所有整数k>=0,F(k+2)=1+∑F(i)')
        print('引理20.3 设x为斐波那契的任一结点，且k=degree[x],那么size(x)>=Fk+2>=Φ^k,其中Φ=(1+sqrt(5))/2')
        print('推论20.4 在一个包含n个结点的斐波那契堆中，结点的最大度数D(n)为O(lgn)')
        print('练习20.4-1 Pinocchio教授声称，包含n个结点的斐波那契堆的高度为O(lgn)')
        print(' 请证明他是错的，即对于任意的正整数n，给出一个斐波那契堆操作序列，',
            '它创建一个仅包含一棵树的堆,该树是n个结点的线性链')
        print('练习20.4-2 假设将级联切断规则加以推广，使得当某个结点x失去其第k个孩子时')
        print(' 就将其与父结点的联系切断，此处k为常整数。k取什么值时，有D(n)=O(lgn)')
        print('思考题20-1 删除的另一种实现')
        print('思考题20-2 其他斐波那契堆的操作')
        print(' 增强斐波那契堆H，使之支持两种新的操作，同时，还不改变其他斐波那契堆操作的平摊运行时间')
        print('FIB-HEAP-CHANGE-KEY(H, x. k) 将结点x的关键字改变为k')
        print('FIB-HEAP-PRUNE(H, r) 将min(r, n[H])个结点从H中删除')
        # python src/chapter20/chapter20note.py
        # python3 src/chapter20/chapter20note.py

chapter20_1 = Chapter20_1()
chapter20_2 = Chapter20_2()
chapter20_3 = Chapter20_3()
chapter20_4 = Chapter20_4()

def printchapter20note():
    '''
    print chapter20 note.
    '''
    print('Run main : single chapter twenty!')  
    chapter20_1.note()
    chapter20_2.note()
    chapter20_3.note()
    chapter20_4.note()

# python src/chapter20/chapter20note.py
# python3 src/chapter20/chapter20note.py
if __name__ == '__main__':  
    printchapter20note()
else:
    pass
