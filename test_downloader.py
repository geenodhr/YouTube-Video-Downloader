import unittest
from unittest.mock import patch, MagicMock
import importlib

# Since the filename has a hyphen, we need to import it dynamically
yt_downloader = importlib.import_module("yt-downloader")

class TestVideoDownloaderApp(unittest.TestCase):
    @patch.object(yt_downloader, 'ttk')
    @patch.object(yt_downloader, 'filedialog')
    @patch.object(yt_downloader, 'tk')
    def test_select_destination(self, mock_tk, mock_filedialog, mock_ttk):
        # Mock master and app creation
        master = MagicMock()
        app = yt_downloader.VideoDownloaderApp(master)

        # Mock the return value of askdirectory
        mock_filedialog.askdirectory.return_value = "/test/directory"

        # Call the method
        app.select_destination()

        # Assert that the label is configured with the correct text
        app.dest_label.config.assert_called_once_with(text="Directory set to /test/directory")

if __name__ == '__main__':
    unittest.main()
