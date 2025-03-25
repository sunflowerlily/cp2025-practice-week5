import numpy as np
import matplotlib.pyplot as plt

def random_walk_2d(steps):
    """生成一个二维随机行走轨迹的终点"""
    x, y = 0, 0
    for _ in range(steps):
        choice = np.random.choice(4)  # 0,1,2,3 四个方向
        if choice == 0:
            dx, dy = 1, 1
        elif choice == 1:
            dx, dy = 1, -1
        elif choice == 2:
            dx, dy = -1, 1
        else:
            dx, dy = -1, -1
        x += dx
        y += dy
    return (x, y)  # 只返回终点坐标

def generate_endpoints(n_walks, steps):
    """生成多个随机行走的终点分布"""
    return [random_walk_2d(steps) for _ in range(n_walks)]

def plot_endpoints_distribution(endpoints):
    """绘制终点分布的散点图"""
    x_coords, y_coords = zip(*endpoints)  # 直接解包坐标
    plt.scatter(x_coords, y_coords, alpha=0.5)
    plt.axis('equal')
    plt.title('Endpoint Distribution Scatter Plot')
    plt.xlabel('X')
    plt.ylabel('Y')

def analyze_x_distribution(endpoints):
    """分析x坐标的分布并计算统计量"""
    if not endpoints:
        raise ValueError("输入列表不能为空")
    x_coords = [point[0] for point in endpoints]
    return np.mean(x_coords), np.var(x_coords, ddof=1)  # 修改：使用样本方差（ddof=1）

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
             'r-', label='Theoretical Normal Distribution')
    
    plt.title('X-Coordinate Distribution Histogram')
    plt.xlabel('X')
    plt.ylabel('Frequency')
    plt.legend()
    
    # Print statistics
    print(f"Sample mean of X-coordinates: {mean:.2f}")
    print(f"Sample variance of X-coordinates: {var:.2f}")
    
    plt.tight_layout()
    plt.show()