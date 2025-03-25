import unittest
import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from unittest.mock import patch

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 从学生作业中导入待测试的函数
from src.waiting_times import (
    generate_coin_sequence,
    calculate_waiting_times,
    analyze_waiting_time,
    plot_waiting_time_histogram
)
# 从参考答案中导入待测试的函数
#from solutions.waiting_times_solution import generate_coin_sequence, calculate_waiting_times, analyze_waiting_time, plot_waiting_time_histogram

class TestWaitingTimes(unittest.TestCase):
    
    def setUp(self):
        """设置测试环境"""
        # 设置随机种子以保证测试结果可重复
        np.random.seed(42)
        self.p_head = 0.08
    
    def test_generate_coin_sequence(self):
        """测试硬币序列生成函数"""
        # 测试生成序列的长度
        n_flips = 1000
        sequence = generate_coin_sequence(n_flips, self.p_head)
        self.assertEqual(len(sequence), n_flips)
        
        # 测试序列中只包含0和1
        self.assertTrue(np.all((sequence == 0) | (sequence == 1)))
        
        # 测试正面概率近似于p_head
        # 对于较大的样本量，正面比例应该接近p_head
        n_flips_large = 10000
        sequence_large = generate_coin_sequence(n_flips_large, self.p_head)
        proportion_heads = np.mean(sequence_large)
        self.assertAlmostEqual(proportion_heads, self.p_head, delta=0.01)
    
    def test_calculate_waiting_times(self):
        """测试等待时间计算函数"""
        # 使用已知序列测试
        test_sequence = np.array([0, 0, 1, 0, 0, 0, 1, 0, 1])
        expected_waiting_times = np.array([3, 1])  # 第一个1和第二个1之间有3个0，第二个1和第三个1之间有1个0
        
        waiting_times = calculate_waiting_times(test_sequence)
        np.testing.assert_array_equal(waiting_times, expected_waiting_times)
        
        # 测试没有正面的情况
        no_heads_sequence = np.zeros(10)
        waiting_times = calculate_waiting_times(no_heads_sequence)
        self.assertEqual(len(waiting_times), 0)
        
        # 测试只有一个正面的情况
        one_head_sequence = np.array([0, 0, 1, 0, 0])
        waiting_times = calculate_waiting_times(one_head_sequence)
        self.assertEqual(len(waiting_times), 0)
    
    def test_analyze_waiting_time(self):
        """测试等待时间分析函数"""
        # 使用简单的等待时间数组
        waiting_times = np.array([10, 12, 8, 14, 11])
        stats = analyze_waiting_time(waiting_times)
        
        # 测试均值计算
        self.assertAlmostEqual(stats["mean"], np.mean(waiting_times))
        
        # 测试标准差计算
        self.assertAlmostEqual(stats["std"], np.std(waiting_times))
        
        # 测试理论均值计算
        theoretical_mean = (1 - self.p_head) / self.p_head
        self.assertAlmostEqual(stats["theoretical_mean"], theoretical_mean)
        
        # 测试指数分布均值计算
        exponential_mean = 1 / self.p_head
        self.assertAlmostEqual(stats["exponential_mean"], exponential_mean)
        

    
    @patch('matplotlib.pyplot.figure')
    @patch('matplotlib.pyplot.hist')
    @patch('matplotlib.pyplot.show')
    def test_plot_waiting_time_histogram(self, mock_show, mock_hist, mock_figure):
        """测试直方图绘制函数（使用mock避免实际显示图形）"""
        waiting_times = np.array([10, 12, 8, 14, 11])
        
        # 测试普通坐标
        plot_waiting_time_histogram(waiting_times, log_scale=False, n_flips=1000)
        mock_figure.assert_called()
        mock_hist.assert_called()
        mock_show.assert_called()
        
        # 测试对数坐标
        plot_waiting_time_histogram(waiting_times, log_scale=True, n_flips=1000)
        self.assertEqual(mock_show.call_count, 2)

if __name__ == '__main__':
    unittest.main()