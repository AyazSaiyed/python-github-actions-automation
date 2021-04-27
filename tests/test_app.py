from app import index,index2


def test_index():
    assert index() == "Hello, world!"

def test_index2():
	assert index2() == "Hello, Ayaz!"