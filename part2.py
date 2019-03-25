from unittest import mock

m = mock.Mock()
# m.assert_called()
try:
    m.assert_called_once()
except AssertionError:
    assert True
else:
    assert False

try:
    m(1, foo='bar')
except RuntimeError:
    assert False
else:
    assert True
assert m.call_args == mock.call(1, foo='bar')
print(m.call_args_list)
assert len(m.call_args_list) >= 1

print(m.call_args_list)
m.reset_mock()
print(m.call_args_list)
assert m.call_args is None
