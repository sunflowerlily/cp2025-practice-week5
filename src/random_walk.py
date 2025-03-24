import numpy as np
import matplotlib.pyplot as plt

def generate_random_walk(num_steps=1000):
    """
    生成一个二维随机游走轨迹
    
    参数:
        num_steps: 随机游走的步数
        
    返回:
        x, y: 包含轨迹坐标的数组
    """
    # 初始化坐标数组
    x = np.zeros(num_steps)
    y = np.zeros(num_steps)
    
    # TODO: 实现随机游走算法
    # 提示: 使用 np.random.choice([-1, 1]) 生成随机步长
    
    return x, y

def plot_single_walk(x, y):
    """
    绘制单个随机游走轨迹
    
    参数:
        x, y: 轨迹坐标数组
    """
    # TODO: 实现单个轨迹的绘制
    # 提示: 使用 plt.plot() 绘制轨迹，并用 plt.axis('equal') 确保比例正确
    
    return plt

def plot_multiple_walks(num_walks=4):
    """
    绘制多个随机游走轨迹
    
    参数:
        num_walks: 轨迹数量
    """
    # TODO: 实现多个轨迹的并排绘制
    # 提示: 使用 plt.subplot() 创建子图，确保所有子图使用相同的坐标轴范围
    
    return plt

def analyze_walks_statistics(num_walks=1000, num_steps=1000):
    """
    分析多个随机游走的统计特性
    
    参数:
        num_walks: 随机游走次数
        num_steps: 每次随机游走的步数
    
    返回:
        mean_squared_displacement: 均方位移
    """
    # 初始化数组存储终点位置和位移
    x_final = np.zeros(num_walks)
    y_final = np.zeros(num_walks)
    displacement = np.zeros(num_walks)
    
    # TODO: 实现多个随机游走的生成和统计分析
    # 提示: 使用循环或向量化操作生成多个轨迹，并计算终点位置和位移
    
    # TODO: 绘制终点散点图
    
    # TODO: 绘制位移直方图
    
    # TODO: 绘制位移平方直方图
    
    # TODO: 使用半对数和对数-对数坐标系分析分布
    
    # TODO: 计算均方位移
    mean_squared_displacement = 0  # 替换为实际计算
    
    return mean_squared_displacement

def compare_mean_squared_displacement():
    """
    比较不同步数的均方位移
    
    返回:
        step_sizes: 步数数组
        msd_values: 对应的均方位移值
    """
    step_sizes = [1000, 2000, 3000, 4000]
    msd_values = []
    
    # TODO: 实现不同步数的均方位移计算
    # 提示: 对每个步数调用 analyze_walks_statistics 函数
    
    # TODO: 绘制均方位移与步数的关系
    
    return step_sizes, msd_values

if __name__ == "__main__":
    # 任务a: 绘制单个随机游走轨迹
    x, y = generate_random_walk()
    plot_single_walk(x, y)
    
    # 任务b: 绘制四个随机游走轨迹
    plot_multiple_walks()
    
    # 任务a-e: 分析1000次随机游走的统计特性
    msd_1000 = analyze_walks_statistics()
    print(f"1000步随机游走的均方位移: {msd_1000:.2f}")
    
    # 任务f: 比较不同步数的均方位移
    step_sizes, msd_values = compare_mean_squared_displacement()
    for steps, msd in zip(step_sizes, msd_values):
        print(f"{steps}步随机游走的均方位移: {msd:.2f}")