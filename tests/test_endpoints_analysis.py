import sys
import os
import pytest
import numpy as np
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 修改导入语句，确保只从一个源导入
from solutions.endpoints_analysis_solution import random_walk_2d, generate_endpoints, plot_endpoints_distribution, analyze_x_distribution

# 注释掉重复的导入
# from src.endpoints_analysis import random_walk_2d, generate_endpoints, plot_endpoints_distribution, analyze_x_distribution

def test_random_walk_2d_output_format():
    """测试随机行走函数的输出格式"""
    endpoint = random_walk_2d(100)
    assert isinstance(endpoint, tuple), "返回值应该是元组类型"
    assert len(endpoint) == 2, "返回值应该是二维坐标"
    assert all(isinstance(x, (int, float)) for x in endpoint), "坐标值应该是数值类型"

def test_random_walk_2d_step_size():
    """测试随机行走的步长"""
    np.random.seed(42)  # 固定随机种子以保证可重复性
    endpoint = random_walk_2d(1)
    assert endpoint[0] in [-1, 1], "x方向步长应该是±1"
    assert endpoint[1] in [-1, 1], "y方向步长应该是±1"

def test_generate_endpoints_length():
    """测试生成的终点列表长度"""
    n_walks = 100
    endpoints = generate_endpoints(n_walks, 1000)
    assert len(endpoints) == n_walks, "终点列表长度应该等于行走次数"
    assert all(isinstance(p, tuple) and len(p) == 2 for p in endpoints), "每个终点都应该是二维坐标元组"

def test_generate_endpoints_randomness():
    """测试生成的终点是否具有随机性"""
    endpoints1 = generate_endpoints(100, 1000)
    endpoints2 = generate_endpoints(100, 1000)
    assert endpoints1 != endpoints2, "多次生成的终点序列应该不同"

def test_plot_endpoints_distribution(tmp_path):
    """测试终点分布图的绘制"""
    endpoints = [(1, 1), (-1, -1), (2, 2), (-2, -2)]
    plt.figure()
    plot_endpoints_distribution(endpoints)
    
    # 检查图形元素
    ax = plt.gca()
    assert len(ax.collections) > 0, "应该有散点图对象"
    assert ax.get_xlabel() == "X", "应该有X轴标签"
    assert ax.get_ylabel() == "Y", "应该有Y轴标签"
    
    # 保存图形用于视觉检查
    plt.savefig(tmp_path / "test_plot.png")
    plt.close()

def test_analyze_x_distribution_basic():
    """测试基本的统计分析功能"""
    endpoints = [(1, 0), (-1, 0), (2, 0), (-2, 0)]
    mean, var = analyze_x_distribution(endpoints)
    assert mean == 0.0, "对称数据的均值应该为0"
    assert var == pytest.approx(3.0, rel=1e-10), "方差计算错误"

def test_analyze_x_distribution_statistical():
    """测试大量数据的统计特性"""
    np.random.seed(42)
    endpoints = generate_endpoints(1000, 1000)
    mean, var = analyze_x_distribution(endpoints)
    
    # 由于中心极限定理，均值应该接近0
    assert abs(mean) < 50.0, "大量样本的均值应该接近0"
    assert var > 0, "方差应该为正数"

def test_analyze_x_distribution_empty():
    """测试空输入的处理"""
    with pytest.raises(ValueError):
        analyze_x_distribution([])

if __name__ == "__main__":
    pytest.main(["-v"])