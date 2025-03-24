import numpy as np
import matplotlib.pyplot as plt

def random_walk_2d(steps):
    """生成一个二维随机行走轨迹的终点"""
    x, y = 0, 0
    for _ in range(steps):
        dx, dy = np.random.choice([(1, 1), (1, -1), (-1, 1), (-1, -1)])
        x += dx
        y += dy
    return (x, y)

def generate_endpoints(n_walks, steps):
    """生成多个随机行走的终点分布"""
    return [random_walk_2d(steps) for _ in range(n_walks)]

def plot_endpoints_distribution(endpoints):
    """绘制终点分布的散点图"""
    x_coords, y_coords = zip(*endpoints)
    plt.scatter(x_coords, y_coords, alpha=0.5)
    plt.axis('equal')
    plt.title('终点分布散点图')
    plt.xlabel('X')
    plt.ylabel('Y')

def analyze_x_distribution(endpoints):
    """分析x坐标的分布并计算统计量"""
    x_coords = [point[0] for point in endpoints]
    return np.mean(x_coords), np.var(x_coords)

if __name__ == "__main__":
    np.random.seed(42)  # 设置随机种子以保证可重复性
    
    # 生成数据
    endpoints = generate_endpoints(1000, 1000)
    
    # 创建图形
    plt.figure(figsize=(12, 5))
    
    # 绘制终点分布
    plt.subplot(121)
    plot_endpoints_distribution(endpoints)
    
    # 绘制x坐标直方图
    plt.subplot(122)
    x_coords = [point[0] for point in endpoints]
    plt.hist(x_coords, bins=50, density=True, alpha=0.7)
    
    # 添加理论正态分布曲线
    mean, var = analyze_x_distribution(endpoints)
    x = np.linspace(min(x_coords), max(x_coords), 100)
    plt.plot(x, 1/np.sqrt(2*np.pi*var)*np.exp(-(x-mean)**2/(2*var)), 
             'r-', label='理论正态分布')
    
    plt.title('X坐标分布直方图')
    plt.xlabel('X')
    plt.ylabel('频率')
    plt.legend()
    
    # 打印统计量
    print(f"X坐标的样本均值: {mean:.2f}")
    print(f"X坐标的样本方差: {var:.2f}")
    
    plt.tight_layout()
    plt.show()