from unittest import mock


'''
The main characteristic of a Mock object is that it will 
return another Mock instance when:

1) accessing one of its attributes
2) calling the object itself
'''
m = mock.Mock()
assert isinstance(m.foo, mock.Mock)
assert isinstance(m.bar, mock.Mock)
assert isinstance(m(), mock.Mock)
assert m.foo is not m.bar is not m()


'''
You can assign a value to an attribute in the Mock by:

1) Assign it directly, like you’d do with any Python object;
2) Use the configure_mock method on an instance;
3) Or pass keyword arguments to the Mock class on creation;
'''
m.foo = 'bar'
assert m.foo == 'bar'

m.configure_mock(bar='baz')
assert m.bar == 'baz'

'''
The Mock will always return the same value on all calls, this, again,
can also be configured by using the side_effect attribute:

1) If you’d like to return different values on each call you can assign an iterable to side_effect.
'''
m.return_value = 42
assert m() == 42

m.side_effect = ['foo', 'bar', 'baz']
assert m() == 'foo'
assert m() == 'bar'
assert m() == 'baz'
try:
    m()
except StopIteration:
    assert True
else:
    assert False

'''
2) If you’d like to raise an exception when calling the Mock you can simply assign the exception object to side_effect.
'''

m.side_effect = RuntimeError('Boom!')
try:
    m()
except RuntimeError:
    assert True
else:
    assert False
