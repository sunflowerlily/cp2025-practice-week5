import unittest
import numpy as np
import sys
import os

# 添加源代码路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#from solutions.mean_square_displacement_solution import random_walk_finals, calculate_mean_square_displacement, analyze_step_dependence
from src.mean_square_displacement import random_walk_finals, calculate_mean_square_displacement, analyze_step_dependence

class TestRandomWalk(unittest.TestCase):
    def setUp(self):
        """设置测试参数"""
        self.num_steps = 1000
        self.num_walks = 1000
        np.random.seed(42)  # 固定随机数种子以保证测试结果可重复
        
    def test_random_walk_finals_output_shape(self):
        """测试随机游走函数的输出形状"""
        x_finals, y_finals = random_walk_finals(self.num_steps, self.num_walks)
        self.assertEqual(x_finals.shape, (self.num_walks,))
        self.assertEqual(y_finals.shape, (self.num_walks,))
        
    def test_random_walk_finals_step_size(self):
        """测试每步移动的大小"""
        x_finals, y_finals = random_walk_finals(1, 1000)
        self.assertTrue(all(abs(x) <= 1 for x in x_finals))
        self.assertTrue(all(abs(y) <= 1 for y in y_finals))
        
    def test_mean_square_displacement_output(self):
        """测试均方位移计算的输出"""
        steps, msd = calculate_mean_square_displacement()
        self.assertEqual(len(steps), 4)  # 测试步数数组长度
        self.assertEqual(len(msd), 4)    # 测试均方位移数组长度
        self.assertTrue(all(m > 0 for m in msd))  # 均方位移应该为正
        
    def test_step_dependence(self):
        """测试步数依赖性分析"""
        steps, msd, k = analyze_step_dependence()
        
        # 测试拟合系数k应该接近2
        self.assertGreater(k, 1.5)
        self.assertLess(k, 2.5)
        
        # 测试均方位移应该随步数增加而增加
        self.assertTrue(all(msd[i] < msd[i+1] for i in range(len(msd)-1)))
        
    def test_theoretical_relationship(self):
        """测试与理论预期的关系"""
        steps, msd = calculate_mean_square_displacement()
        
        # 理论上均方位移应该近似等于2倍步数
        relative_errors = np.abs(msd - 2*steps) / (2*steps)
        self.assertTrue(all(err < 0.2 for err in relative_errors))  # 相对误差应小于20%

if __name__ == '__main__':
    unittest.main()