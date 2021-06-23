# https://pure-taiga-43039.herokuapp.com/

from app import index,index2


def test_index():
    assert index() == "welcome to python github actions demo"
    

def test_index2():
	assert index2() == "Hello, Ayaz!"
