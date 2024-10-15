import pytest
import segbutunittest as seg

def test_createGrid():
    s = 5
    r = seg.createGrid(s)
    expected = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
    assert r == expected

def test_getCounts():
    t = seg.getCounts([['', '', '', ''],['', '', '', ''],['', '', '', ''],['', '', '', '']], 0.5, 0.5)
    expected = (8, 4, 4)
    assert t == expected

def test_getSeed():
    t = seg.getSeed((8, 4, 4))
    expected = ["r", "r", "r", "r", "b", "b", "b", "b", "e", "e", "e", "e", "e", "e", "e", "e"]
    assert t == expected

def test_fillGrid():
    t = seg.fillGrid([['', '', '', ''],['', '', '', ''],['', '', '', ''],['', '', '', '']], ["e", "e", "e", "e", "e", "e", "e", "e", "r", "r", "r", "r", "b", "b", "b", "b"])
    expected = [["e", "e", "e", "e"], ["e", "e", "e", "e"], ["r", "r", "r", "r"], ["b", "b", "b", "b"]]
    assert t == expected

def test_getUpdateList():
    t = seg.getUpdateList([['e', 'r', 'b', 'e'],['b', 'b', 'b', 'r'],['r', 'b', 'b', 'b'],['b', 'e', 'b', 'b']], 0.5)
    expected = [(0, 1), (1, 3), (2, 0)]
    assert t == expected

def test_getEmptyList():
    t = seg.getEmptyList([['e', 'r', 'b', 'e'],['b', 'b', 'b', 'r'],['r', 'b', 'b', 'b'],['b', 'e', 'b', 'b']])
    expected = [(0, 0), (0, 3), (3, 1)]
    assert t == expected

def test_updateGridCheckSize():
    t = seg.updateGrid([['e', 'r', 'b', 'e'],['b', 'b', 'b', 'r'],['r', 'b', 'b', 'b'],['b', 'e', 'b', 'b']], [(0, 1), (1, 3), (2, 0)], [(0, 0), (0, 3), (3, 1)])
    expected = len([['e', 'r', 'b', 'e'],['b', 'b', 'b', 'r'],['r', 'b', 'b', 'b'],['b', 'e', 'b', 'b']])
    assert len(t) == expected

def test_updateGridCheckNestedSize():
    t = seg.updateGrid([['e', 'r', 'b', 'e'],['b', 'b', 'b', 'r'],['r', 'b', 'b', 'b'],['b', 'e', 'b', 'b']], [(0, 1), (1, 3), (2, 0)], [(0, 0), (0, 3), (3, 1)])
    expected = len(['e', 'r', 'b', 'e'])
    assert len(t[0]) == expected

def test_updateGridCheckAmntEmpty():
    t = seg.updateGrid([['e', 'r', 'b', 'e'],['b', 'b', 'b', 'r'],['r', 'b', 'b', 'b'],['b', 'e', 'b', 'b']], [(0, 1), (1, 3), (2, 0)], [(0, 0), (0, 3), (3, 1)])
    x = seg.getEmptyList(t)
    b = seg.getEmptyList([['e', 'r', 'b', 'e'],['b', 'b', 'b', 'r'],['r', 'b', 'b', 'b'],['b', 'e', 'b', 'b']])
    expected = len(b)
    assert len(x) == expected

def test_getPerSatisfied():
    t = seg.getPerSatisfied([['e', 'r', 'b', 'e'],['b', 'b', 'b', 'r'],['r', 'b', 'b', 'b'],['b', 'e', 'b', 'b']], 0.5)
    expected = 0.7692
    assert t == expected

