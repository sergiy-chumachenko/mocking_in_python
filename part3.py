from unittest import TestCase, mock

from patched_func import work_on


class TestWorkMockingModule(TestCase):

    def test_using_context_manager(self):
        with mock.patch('patched_func.os') as mocked_os:
            work_on()
            mocked_os.getcwd.assert_called_once()
