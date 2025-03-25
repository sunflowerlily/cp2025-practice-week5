import unittest
import numpy as np
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.random_walk_trace import random_walk_2d, plot_single_walk, plot_multiple_walks
#from solutions.random_walk_trace_solution import random_walk_2d, plot_single_walk, plot_multiple_walks

class TestRandomWalkTrace(unittest.TestCase):
    def setUp(self):
        self.steps = 100
        
    def test_random_walk_output(self):
        """测试随机行走函数的输出格式"""
        path = random_walk_2d(self.steps)
        self.assertIsInstance(path, tuple)
        self.assertEqual(len(path), 2)
        self.assertEqual(len(path[0]), self.steps)
        self.assertEqual(len(path[1]), self.steps)
        
    def test_step_size(self):
        """测试每步移动的大小是否为1"""
        path = random_walk_2d(self.steps)
        x_diff = np.diff(path[0])
        y_diff = np.diff(path[1])
        self.assertTrue(np.all(np.abs(x_diff) == 1))
        self.assertTrue(np.all(np.abs(y_diff) == 1))
        
    def test_plot_functions(self):
        """测试绘图函数是否正常运行"""
        path = random_walk_2d(self.steps)
        plt.figure()
        plot_single_walk(path)
        plt.close()
        
        plt.figure()
        plot_multiple_walks()
        plt.close()

if __name__ == '__main__':
    unittest.main()