import Задача1

def test_passing():
	assert Задача1.greet('World', greeting='Hello') == "'greet' вернула 'Hello, World!'"

def test_not_passing():
	assert Задача1.greet('World', greeting='hello') != "'greet' вернула 'Hello, World!'"