from st2tests.base import BaseActionTestCase
from mock import patch, mock_open
from lib.log import LogAction

class LogActionTestCase(BaseActionTestCase):
    action_cls = LogAction
    
    def test_init(self):
        action = self.get_action_instance({})
        self.assertIsInstance(action, LogAction)

    @patch('builtins.open', new_callable=mock_open)
    def test_run(self, mock_file):
        fake_file_path = "/home/vagrant/foo.txt"
        content = "Fake log message"
        action = self.get_action_instance({})
        action.run(file_path=fake_file_path, log=content)
        mock_file.assert_called_with(fake_file_path, "w")
        mock_file.return_value.__enter__().write.assert_called_once_with(content)

    # def test_run(self):
    #     fake_file_path = "fake/file/path"
    #     content = "Fake log message"
    #     action = self.get_action_instance({})

    #     with mock.patch('builtins.open', mock.mock_open()) as mocked_file:
    #         FileWriter().write(fake_file_path, content)

    #         # assert if opened file on write mode 'w'
    #         mocked_file.assert_called_once_with(fake_file_path, 'w')

    #         # assert if write(content) was called from the file opened
    #         # in another words, assert if the specific content was written in file
    #         mocked_file().write.assert_called_once_with(content)
