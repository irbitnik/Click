import unittest
from unittest.mock import patch, ANY
from utils import Image, rand_click
from config import Settings
import pyautogui

class TestImage(unittest.TestCase):

    @patch("pyautogui.locateOnScreen")
    def test_find_image_found(self, mock_locate):
        """Test: image is found on screen"""
        mock_locate.return_value = (100, 100, 50, 50)
        img = Image("image/gnomes.png")
        result = img.find_image()
        self.assertTrue(result)

    @patch("pyautogui.locateOnScreen")
    def test_find_image_not_found(self, mock_locate):
        """Test: image not found — returns False"""
        mock_locate.side_effect = pyautogui.ImageNotFoundException
        img = Image("image/gnomes.png")
        result = img.find_image()
        self.assertFalse(result)


class TestRandClick(unittest.TestCase):

    @patch("pyautogui.click")
    @patch("random.randint", side_effect=[200, 300])
    @patch("random.uniform", return_value=0.7)
    def test_rand_click_first_slot(self, _, __, mock_click):
        """Test: click in the first slot with longer duration"""
        coord = Settings.COORD[0]  # First slot
        rand_click(coord)
        mock_click.assert_called_with(200, 300, duration=0.7, tween=ANY)

    @patch("pyautogui.click")
    @patch("random.randint", side_effect=[400, 500])
    @patch("random.uniform", return_value=0.3)
    def test_rand_click_other_slot(self, _, __, mock_click):
        """Test: click in another slot with shorter duration"""
        coord = Settings.COORD[1]  # Not the first slot
        rand_click(coord)
        mock_click.assert_called_with(400, 500, duration=0.3, tween=ANY)


if __name__ == "__main__":
    unittest.main()