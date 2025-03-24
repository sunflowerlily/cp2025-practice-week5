import numpy as np
import matplotlib.pyplot as plt

def random_walk_2d(steps):
    """生成一个二维随机行走轨迹的终点
    
    参数:
        steps (int): 随机行走的步数
        
    返回:
        tuple: 随机行走终点的坐标 (x, y)
    """
    # TODO: 实现随机行走算法并返回终点坐标
    pass

def generate_endpoints(n_walks, steps):
    """生成多个随机行走的终点分布
    
    参数:
        n_walks (int): 随机行走的次数
        steps (int): 每次随机行走的步数
        
    返回:
        list: 包含所有终点坐标的列表
    """
    # TODO: 实现多次随机行走并收集终点
    pass

def plot_endpoints_distribution(endpoints):
    """绘制终点分布的散点图
    
    参数:
        endpoints (list): 终点坐标列表
    """
    # TODO: 实现终点分布的散点图
    pass

def analyze_x_distribution(endpoints):
    """分析x坐标的分布并计算统计量
    
    参数:
        endpoints (list): 终点坐标列表
        
    返回:
        tuple: (期望值, 方差)
    """
    # TODO: 实现统计分析
    pass

if __name__ == "__main__":
    # 生成数据
    endpoints = generate_endpoints(1000, 1000)
    
    # 绘制终点分布
    plt.figure(figsize=(10, 5))
    plt.subplot(121)
    plot_endpoints_distribution(endpoints)
    
    # 绘制x坐标直方图
    plt.subplot(122)
    x_coords = [point[0] for point in endpoints]
    plt.hist(x_coords, bins=50, density=True)
    plt.title('X坐标分布直方图')
    
    # 计算并打印统计量
    mean, var = analyze_x_distribution(endpoints)
    print(f"X坐标的样本均值: {mean:.2f}")
    print(f"X坐标的样本方差: {var:.2f}")
    
    plt.tight_layout()
    plt.show()