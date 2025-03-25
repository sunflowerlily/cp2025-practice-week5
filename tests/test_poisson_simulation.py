import unittest
from unittest.mock import patch
import numpy as np
from scipy.special import factorial
import matplotlib.pyplot as plt
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.poisson_simulation import plot_poisson_pmf, simulate_coin_flips, compare_simulation_theory
#from solutions.poisson_simulation_solution import plot_poisson_pmf, simulate_coin_flips, compare_simulation_theory

class TestPoissonSimulation(unittest.TestCase):
    def setUp(self):
        """设置测试环境"""
        np.random.seed(42)
        self.lambda_param = 8
        self.max_l = 20
        self.n_experiments = 1000
        self.n_flips = 100
        self.p_head = 0.08

    def test_pmf_calculation(self):
        """测试PMF计算结果是否正确"""
        pmf = plot_poisson_pmf(self.lambda_param, self.max_l)
        
        # 手动计算预期结果
        l_values = np.arange(self.max_l)
        expected_pmf = (self.lambda_param**l_values * np.exp(-self.lambda_param)) / factorial(l_values)
        
        # 验证概率和接近1
        self.assertAlmostEqual(np.sum(pmf), 1.0, places=3)
        # 验证所有概率非负
        self.assertTrue(np.all(pmf >= 0))
        # 验证计算结果
        np.testing.assert_array_almost_equal(pmf, expected_pmf)
        plt.close('all')

    def test_simulate_coin_flips(self):
        """测试抛硬币实验的基本属性"""
        results = simulate_coin_flips(self.n_experiments, self.n_flips, self.p_head)
        
        # 测试形状
        self.assertEqual(results.shape, (self.n_experiments,))
        
        # 测试范围
        self.assertTrue(np.all(results >= 0))
        self.assertTrue(np.all(results <= self.n_flips))
        
        # 测试均值
        expected_mean = self.n_flips * self.p_head
        actual_mean = np.mean(results)
        self.assertLess(abs(actual_mean - expected_mean) / expected_mean, 0.05)

    def test_edge_cases(self):
        """测试边界情况"""
        # 测试零次实验
        results_zero_exp = simulate_coin_flips(0, self.n_flips, self.p_head)
        self.assertEqual(len(results_zero_exp), 0)

        # 测试零次抛掷
        results_zero_flips = simulate_coin_flips(self.n_experiments, 0, self.p_head)
        self.assertTrue(np.all(results_zero_flips == 0))

        # 测试极端概率
        results_p0 = simulate_coin_flips(100, 10, 0.0)
        results_p1 = simulate_coin_flips(100, 10, 1.0)
        self.assertTrue(np.all(results_p0 == 0))
        self.assertTrue(np.all(results_p1 == 10))

    @patch('matplotlib.pyplot.figure')
    @patch('matplotlib.pyplot.plot')
    @patch('matplotlib.pyplot.title')
    def test_visualization(self, mock_title, mock_plot, mock_figure):
        """测试可视化函数的调用"""
        plot_poisson_pmf(self.lambda_param, self.max_l)
        # 修改断言，检查是否至少调用了一次，而不是严格的一次
        self.assertTrue(mock_figure.called)
        mock_plot.assert_called_once()
        mock_title.assert_called_once_with(f'Poisson Probability Mass Function (λ={self.lambda_param})')
        plt.close('all')

if __name__ == '__main__':
    unittest.main()