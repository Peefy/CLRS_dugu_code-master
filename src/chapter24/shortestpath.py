
import graph as _g
import math as _math
from copy import deepcopy as _deepcopy

class _ShortestPath:
    '''
    单源最短路径算法集合
    '''
    def __init__(self, *args, **kwords):
        pass

    def initialize_single_source(self, g : _g.Graph, s : _g.Vertex):
        '''
        最短路径估计和前趋进行初始化 时间复杂度Θ(V)
        '''
        for v in g.veterxs:
            v.d = _math.inf
            v.pi = None
        s.d = 0

    def relax(self, u : _g.Vertex, v : _g.Vertex, weight):
        '''
        一步松弛操作
        '''
        if v.d > u.d + weight:
            v.d = u.d + weight
            v.pi = u
    
    def bellman_ford(self, g : _g.Graph, s : _g.Vertex):
        '''
        Bellmax-Ford算法能在一般的情况下(存在负边权的情况)下,解决单源最短路径问题

        时间复杂度 O(VE)

        Args
        ===
        `g` : 图G=(V,E)

        `w` : 加权函数

        `s` : 源顶点

        Return
        ===
        `exist` : bool 返回一个布尔值,表明图中是否存在着一个从源点可达的权为负的回路
        若存在这样的回路的话,算法说明该问题无解;若不存在这样的回路,算法将产生最短路径以及权值

        '''
        if type(s) is not _g.Vertex:
            s = g.veterxs_atkey(s)
        self.initialize_single_source(g, s)
        n = g.vertex_num
        for i in range(n - 1):
            for edge in g.edges:
                u, v = edge.vertex1, edge.vertex2
                u = g.veterxs_atkey(u)
                v = g.veterxs_atkey(v)
                self.relax(u, v, edge.weight)
        for edge in g.edges:
            u, v = edge.vertex1, edge.vertex2
            u = g.veterxs_atkey(u)
            v = g.veterxs_atkey(v)
            if v.d > u.d + edge.weight:
                return False
        return True 

__shortest_path_instance = _ShortestPath()
bellman_ford = __shortest_path_instance.bellman_ford

def test_bellman_ford():
    g = _g.Graph()
    g.clear()
    vertexs = [_g.Vertex('s'), _g.Vertex('t'), _g.Vertex(
        'x'), _g.Vertex('y'), _g.Vertex('z')]
    g.veterxs = vertexs
    g.addedgewithweight('s', 't', 6, _g.DIRECTION_TO)
    g.addedgewithweight('s', 'y', 7, _g.DIRECTION_TO)
    g.addedgewithweight('t', 'x', 5, _g.DIRECTION_TO)
    g.addedgewithweight('t', 'y', 8, _g.DIRECTION_TO)
    g.addedgewithweight('t', 'z', -4, _g.DIRECTION_TO)
    g.addedgewithweight('x', 't', -2, _g.DIRECTION_TO)
    g.addedgewithweight('y', 'x', -3, _g.DIRECTION_TO)
    g.addedgewithweight('y', 'z', 9, _g.DIRECTION_TO)
    g.addedgewithweight('z', 'x', 7, _g.DIRECTION_TO)
    g.addedgewithweight('z', 's', 2, _g.DIRECTION_TO)
    print(bellman_ford(g, vertexs[0]))
    del g

def test():
    '''
    测试函数
    '''
    test_bellman_ford()

if __name__ == '__main__':
    test()
else:
    pass
