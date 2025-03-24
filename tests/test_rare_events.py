import sys
import os
import numpy as np
import pytest

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
#from solutions.rare_events_solution import calculate_poisson_pmf, simulate_coin_flips, analyze_waiting_times
from src.rare_events import calculate_poisson_pmf, simulate_coin_flips, analyze_waiting_times

def test_calculate_poisson_pmf():
    """测试泊松分布概率质量函数计算"""
    l_values = np.array([0, 1, 2], dtype=float)
    pmf = calculate_poisson_pmf(l_values, lambda_val=1)
    
    # 手动计算预期值
    expected = np.array([np.exp(-1), np.exp(-1), np.exp(-1)/2])
    
    # 检查结果是否接近预期值
    assert np.allclose(pmf, expected, rtol=1e-10)
    
    # 检查概率和是否接近1
    l_values = np.arange(0, 20, dtype=float)
    pmf = calculate_poisson_pmf(l_values, lambda_val=8)
    assert abs(np.sum(pmf) - 1) < 0.001

def test_simulate_coin_flips():
    """测试硬币翻转模拟"""
    N = 1000
    n = 100
    p = 0.08
    
    # 运行模拟
    heads_count = simulate_coin_flips(N, n, p)
    
    # 检查返回数组的长度
    assert len(heads_count) == N
    
    # 检查结果是否在合理范围内
    assert np.all(heads_count >= 0)
    assert np.all(heads_count <= n)
    
    # 检查平均值是否接近预期值
    expected_mean = n * p
    actual_mean = np.mean(heads_count)
    assert abs(actual_mean - expected_mean) < expected_mean * 0.1

def test_analyze_waiting_times():
    """测试等待时间分析"""
    num_flips = 1000
    p = 0.08
    
    # 运行分析
    waiting_times = analyze_waiting_times(num_flips, p)
    
    # 检查返回值是否为数组
    assert isinstance(waiting_times, np.ndarray)
    
    # 检查等待时间是否都是正数
    assert np.all(waiting_times > 0)
    
    # 检查平均等待时间是否接近理论值 (1/p)
    expected_mean = 1/p
    actual_mean = np.mean(waiting_times)
    assert abs(actual_mean - expected_mean) < expected_mean * 0.2

if __name__ == "__main__":
    pytest.main(["-v", __file__])