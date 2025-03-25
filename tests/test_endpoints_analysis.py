import unittest
from unittest.mock import patch
import numpy as np
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.endpoints_analysis import random_walk_finals
#from solutions.endpoints_analysis_solution import random_walk_finals

class TestRandomWalkFinals(unittest.TestCase):
    
    def setUp(self):
        self.num_steps = 1000
        self.num_walks = 100
        np.random.seed(42)  # 固定随机种子以保证测试结果可重复

    def test_output_shape(self):
        """测试输出的形状是否正确"""
        x_finals, y_finals = random_walk_finals(self.num_steps, self.num_walks)
        self.assertEqual(x_finals.shape, (self.num_walks,))
        self.assertEqual(y_finals.shape, (self.num_walks,))

    def test_random_walk_values(self):
        """测试随机游走的值是否在预期范围内"""
        x_finals, y_finals = random_walk_finals(self.num_steps, self.num_walks)
        self.assertTrue(np.all(np.abs(x_finals) <= self.num_steps))
        self.assertTrue(np.all(np.abs(y_finals) <= self.num_steps))

    @patch('src.endpoints_analysis.np.random.choice')
    def test_random_choice_called(self, mock_choice):
        """测试是否调用了np.random.choice"""
        mock_choice.return_value = np.ones(self.num_steps)
        random_walk_finals(self.num_steps, self.num_walks)
        mock_choice.assert_called_with([-1, 1], self.num_steps)

    def test_zero_steps(self):
        """测试步数为零的情况"""
        x_finals, y_finals = random_walk_finals(0, self.num_walks)
        self.assertTrue(np.all(x_finals == 0))
        self.assertTrue(np.all(y_finals == 0))

    def test_zero_walks(self):
        """测试游走次数为零的情况"""
        x_finals, y_finals = random_walk_finals(self.num_steps, 0)
        self.assertEqual(len(x_finals), 0)
        self.assertEqual(len(y_finals), 0)

if __name__ == '__main__':
    unittest.main()