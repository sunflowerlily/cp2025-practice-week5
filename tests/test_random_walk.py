import sys
import os
import numpy as np
import pytest

# 添加src目录到Python路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import random_walk

def test_generate_random_walk():
    """测试随机游走生成函数"""
    num_steps = 100
    x, y = random_walk.generate_random_walk(num_steps)
    
    # 检查数组长度
    assert len(x) == num_steps
    assert len(y) == num_steps
    
    # 检查起点是否为原点
    assert x[0] == 0
    assert y[0] == 0
    
    # 检查每一步的步长是否为±1
    for i in range(1, num_steps):
        assert abs(x[i] - x[i-1]) == 1
        assert abs(y[i] - y[i-1]) == 1

def test_analyze_walks_statistics():
    """测试随机游走统计分析函数"""
    num_walks = 100
    num_steps = 100
    
    # 运行分析函数
    msd = random_walk.analyze_walks_statistics(num_walks, num_steps)
    
    # 检查均方位移是否为正数
    assert msd > 0
    
    # 检查均方位移是否与步数成正比（近似关系）
    # 理论上，二维随机游走的均方位移应该约等于步数的2倍
    assert 0.5 * num_steps < msd < 4 * num_steps

def test_compare_mean_squared_displacement():
    """测试均方位移与步数关系的函数"""
    # 运行比较函数
    step_sizes, msd_values = random_walk.compare_mean_squared_displacement()
    
    # 检查返回的数组长度是否一致
    assert len(step_sizes) == len(msd_values)
    
    # 检查均方位移是否随步数增加而增加
    for i in range(1, len(step_sizes)):
        assert msd_values[i] > msd_values[i-1]
    
    # 检查均方位移与步数的近似线性关系
    ratios = [msd / steps for msd, steps in zip(msd_values, step_sizes)]
    avg_ratio = sum(ratios) / len(ratios)
    
    # 检查比值是否在合理范围内（理论上约为2）
    for ratio in ratios:
        assert 0.5 * avg_ratio < ratio < 1.5 * avg_ratio

if __name__ == "__main__":
    pytest.main(["-v", __file__])