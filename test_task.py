import pytest

from avl_tree import AVL_tree
from avl_tree import Node
from avl_tree import main

@pytest.mark.parametrize("f_v, s_v, t_v, f4_v, f5_v, req, req_v, exp_val", [
    (1,2,3,5,7,'m',3,3),
    (1,2,3,5,7,'m',5,7),
    (1,2,3,5,7,'n',6,4),
    (1,2,3,5,7,'n',8,5)
])
def test_add(f_v, s_v, t_v, f4_v, f5_v, req, req_v, exp_val):
    Tree = AVL_tree()
    rt = None
    rt = Tree.insert(f_v, rt)
    rt = Tree.insert(s_v, rt)
    rt = Tree.insert(t_v, rt)
    rt = Tree.insert(f4_v, rt)
    rt = Tree.insert(f5_v, rt)
    if req == 'n':
        check = Tree.n_request(rt,req_v,0)
    elif req == 'm':
        check = Tree.m_request(rt, req_v - 1)
    
    assert exp_val == check

@pytest.mark.parametrize("file_data, result", [
    ('k 3 k 5 k 7 k 1 k 2 m 3 m 1 m 5 n 4 k 4 k 8 k 10 k -1 k 11 k 12 m 3 m 6 m 9 n 4 n 10', '3 1 7 3 2 5 10 4 8'),
    ('k 3 k 9 k 4 k -2 m 1 m 2 n 4 k 5 k 1 k -5 m 1 m 2 n 4', '-2 3 2 -5 -2 4'), 
    ('k 1 k 2 k 3 k 4 k 5 m 1 m 2 m 3 m 4 k 1 k 2 k 3 m 1 m 2', '1 2 3 4 1 2')
])
def test_n_k_m(file_data, result):
    assert main(file_data) == result
