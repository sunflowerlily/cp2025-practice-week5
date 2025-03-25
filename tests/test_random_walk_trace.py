import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.testing.decorators import check_figures_equal
import pytest

# 添加项目根目录到 Python 路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.random_walk_trace import random_walk_2d, plot_single_walk, plot_multiple_walks

def test_random_walk_2d_output_format():
    """测试随机行走函数的输出格式"""
    steps = 100
    path = random_walk_2d(steps)
    
    assert isinstance(path, list), "路径应该是一个列表"
    assert len(path) == steps + 1, "路径长度应该等于步数+1"
    assert all(isinstance(p, tuple) and len(p) == 2 for p in path), "每个点应该是二维坐标元组"

def test_random_walk_2d_start_point():
    """测试起点是否为原点(0,0)"""
    path = random_walk_2d(10)
    assert path[0] == (0, 0), "起点应该是原点(0,0)"

def test_random_walk_2d_step_size():
    """测试每一步的步长是否正确（对角线移动）"""
    path = random_walk_2d(100)
    for i in range(1, len(path)):
        dx = abs(path[i][0] - path[i-1][0])
        dy = abs(path[i][1] - path[i-1][1])
        assert dx == 1 and dy == 1, "每一步应该是对角线移动"

def test_random_walk_2d_different_paths():
    """测试多次运行是否产生不同的路径"""
    path1 = random_walk_2d(100)
    path2 = random_walk_2d(100)
    assert path1 != path2, "多次运行应该产生不同的路径"

@pytest.mark.mpl_image_compare
def test_plot_single_walk():
    """测试单个随机行走的绘图功能"""
    path = random_walk_2d(10)
    plt.figure()
    plot_single_walk(path)
    assert plt.gcf().get_axes(), "图形应该包含至少一个坐标轴"
    plt.close()

@pytest.mark.mpl_image_compare
def test_plot_multiple_walks():
    """测试多个随机行走的绘图功能"""
    plt.figure()
    plot_multiple_walks()
    assert len(plt.gcf().get_axes()) == 4, "应该有4个子图"
    plt.close()

def test_plot_single_walk_elements():
    """测试单个随机行走图的元素是否完整"""
    path = random_walk_2d(10)
    plt.figure()
    plot_single_walk(path)
    fig = plt.gcf()
    
    # 检查图例是否存在
    assert len(plt.gca().get_legend().get_texts()) == 2, "应该有起点和终点两个图例项"
    
    # 检查散点图数量（起点和终点）
    assert len(plt.gca().collections) == 2, "应该有两个散点图对象（起点和终点）"
    
    plt.close()

def test_plot_multiple_walks_layout():
    """测试多个随机行走图的布局"""
    plt.figure()
    plot_multiple_walks()
    fig = plt.gcf()
    
    # 检查子图数量
    assert len(fig.axes) == 4, "应该有4个子图"
    
    plt.close()

if __name__ == "__main__":
    pytest.main(["-v"])