import pytest
import numpy as np
from src.endpoints_analysis import random_walk_2d, generate_endpoints, analyze_x_distribution

def test_random_walk_2d():
    """测试单次随机行走"""
    endpoint = random_walk_2d(1000)
    assert isinstance(endpoint, tuple)
    assert len(endpoint) == 2
    assert isinstance(endpoint[0], (int, float))
    assert isinstance(endpoint[1], (int, float))

def test_generate_endpoints():
    """测试多次随机行走"""
    endpoints = generate_endpoints(100, 1000)
    assert len(endpoints) == 100
    assert all(isinstance(p, tuple) and len(p) == 2 for p in endpoints)

def test_analyze_x_distribution():
    """测试统计分析函数"""
    # 创建模拟数据
    test_endpoints = [(1, 0), (-1, 0), (2, 0), (-2, 0)]
    mean, var = analyze_x_distribution(test_endpoints)
    assert mean == 0.0
    assert var == pytest.approx(3.0, rel=1e-10)

def test_statistical_properties():
    """测试随机行走的统计特性"""
    endpoints = generate_endpoints(1000, 1000)
    mean, var = analyze_x_distribution(endpoints)
    
    # 由于中心极限定理，均值应该接近0
    assert abs(mean) < 5.0
    
    # 方差应该随步数增加而增加
    assert var > 0