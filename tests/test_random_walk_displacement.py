import unittest
import numpy as np
import sys
import os

# 添加src目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Change this line to test student implementation
from src.random_walk_displacement import random_walk_displacement
#from solutions.random_walk_displacement_solution import random_walk_displacement

class TestRandomWalk(unittest.TestCase):
    def setUp(self):
        self.num_steps = 100
        self.num_simulations = 50
    
    def test_output_shape(self):
        """测试输出数组的形状是否正确"""
        result = random_walk_displacement(self.num_steps, self.num_simulations)
        self.assertEqual(result.shape, (2, self.num_simulations))
    
    def test_step_size(self):
        """测试每步移动的大小是否为1"""
        result = random_walk_displacement(1, self.num_simulations)
        self.assertTrue(np.all(np.abs(result) <= 1))
    
    def test_random_distribution(self):
        """测试随机性是否合理"""
        np.random.seed(42)  # Set seed for reproducibility
        result = random_walk_displacement(self.num_steps, 1000)
        mean = np.mean(result)
        # 大量样本的均值应接近0，放宽标准到0.2
        self.assertTrue(abs(mean) < 0.2)
    
    def test_invalid_input(self):
        """测试无效输入的处理"""
        with self.assertRaises(ValueError):
            random_walk_displacement(-1, 10)
        with self.assertRaises(ValueError):
            random_walk_displacement(10, -1)

if __name__ == '__main__':
    unittest.main()