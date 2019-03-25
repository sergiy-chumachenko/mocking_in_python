from unittest import mock, TestCase

from patched_func import work_on


class TestWorkMockingModule(TestCase):
    @mock.patch('patched_func.os')
    def test_using_decorator(self, mocked_os):
        work_on()
        mocked_os.getcwd.assert_called_once()

    def test_using_return_value(self):
        with mock.patch('patched_func.os.getcwd', return_value='testing'):
            work_on()
            assert work_on() == 'testing'
