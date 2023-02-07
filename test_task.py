import pytest
from avl_tree import AVL_tree
from avl_tree import Node

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
