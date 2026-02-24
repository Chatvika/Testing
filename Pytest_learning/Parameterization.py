'''Parametrization:

Used to run same test with multiple inputs.'''

import pytest

@pytest.mark.parametrize("a,b,result",[
(2,3,5),
(5,5,10),
(10,1,12)
])

def test_add(a , b, result):
    assert a+b ==result