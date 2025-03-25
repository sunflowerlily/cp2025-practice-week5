import matplotlib.pyplot as plt
import random
import numpy as np

def random_walk_2d(steps):
    """生成二维随机行走轨迹
    
    参数:
        steps (int): 随机行走的步数
        
    返回:
        list: 包含轨迹上所有点坐标的列表，每个点表示为 (x, y) 元组
    """
    # TODO: 实现随机行走算法
    # 1. 初始化起点(0,0)
    # 2. 每一步随机选择对角线方向移动
    # 3. 记录并返回完整轨迹
    pass

def plot_single_walk(path):
    """绘制单个随机行走轨迹
    
    参数:
        path (list): 包含轨迹点坐标的列表
    """
    # TODO: 实现单个轨迹的绘制
    # 1. 提取x和y坐标
    # 2. 绘制轨迹线
    # 3. 用不同颜色标记起点和终点
    # 4. 添加图例
    # 5. 保持坐标轴比例相等
    pass

def plot_multiple_walks():
    """在2x2子图中绘制四个不同的随机行走轨迹"""
    # TODO: 实现多个轨迹的绘制
    # 1. 创建2x2的子图布局
    # 2. 生成4个不同的随机行走轨迹
    # 3. 在每个子图中绘制一个轨迹
    # 4. 添加标题和图例
    # 5. 调整布局
    pass

if __name__ == "__main__":
    # 示例代码
    plt.figure(figsize=(8, 8))
    path = random_walk_2d(1000)
    plot_single_walk(path)
    plt.title('Single Random Walk Trajectory')
    plt.show()
    
    plot_multiple_walks()
    plt.show()