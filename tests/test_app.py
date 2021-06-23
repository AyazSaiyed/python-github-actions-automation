from app import index,index2


def test_index():
    assert index() == "welcome to the demo of python github actions"

def test_index2():
	assert index2() == "Hello, Ayaz!"
