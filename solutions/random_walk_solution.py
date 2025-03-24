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
    
    # 生成随机步长 (±1, ±1)
    for i in range(1, num_steps):
        x[i] = x[i-1] + np.random.choice([-1, 1])
        y[i] = y[i-1] + np.random.choice([-1, 1])
        
    return x, y

def plot_single_walk(x, y):
    """
    绘制单个随机游走轨迹
    
    参数:
        x, y: 轨迹坐标数组
    """
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, 'b-', alpha=0.7)
    plt.plot(x[0], y[0], 'go', markersize=10, label='起点')  # 起点
    plt.plot(x[-1], y[-1], 'ro', markersize=10, label='终点')  # 终点
    plt.title('二维随机游走轨迹')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axis('equal')  # 确保x和y轴比例相同
    plt.legend()
    plt.show()
    
    return plt

def plot_multiple_walks(num_walks=4):
    """
    绘制多个随机游走轨迹
    
    参数:
        num_walks: 轨迹数量
    """
    plt.figure(figsize=(12, 10))
    
    # 找出所有轨迹的最大范围，以便统一坐标轴
    all_x = []
    all_y = []
    
    # 首先生成所有轨迹并找出坐标范围
    walks = []
    for i in range(num_walks):
        x, y = generate_random_walk()
        walks.append((x, y))
        all_x.extend(x)
        all_y.extend(y)
    
    # 确定坐标轴范围
    x_min, x_max = min(all_x), max(all_x)
    y_min, y_max = min(all_y), max(all_y)
    
    # 绘制每个轨迹
    for i, (x, y) in enumerate(walks):
        plt.subplot(2, 2, i+1)
        plt.plot(x, y, '-', alpha=0.7)
        plt.plot(x[0], y[0], 'go', markersize=8, label='起点')
        plt.plot(x[-1], y[-1], 'ro', markersize=8, label='终点')
        plt.title(f'随机游走 #{i+1}')
        plt.grid(True)
        
        # 设置统一的坐标轴范围
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)
        plt.axis('equal')
    
    plt.tight_layout()
    plt.show()
    
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
    
    # 生成多个随机游走
    for i in range(num_walks):
        x, y = generate_random_walk(num_steps)
        x_final[i] = x[-1]
        y_final[i] = y[-1]
        displacement[i] = np.sqrt(x[-1]**2 + y[-1]**2)
    
    # 绘制终点散点图
    plt.figure(figsize=(10, 8))
    plt.scatter(x_final, y_final, alpha=0.5)
    plt.title(f'{num_walks}次随机游走的终点分布')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.axis('equal')
    plt.show()
    
    # 绘制位移直方图
    plt.figure(figsize=(10, 6))
    plt.hist(displacement, bins=30, alpha=0.7)
    plt.title(f'{num_walks}次随机游走的位移分布')
    plt.xlabel('位移')
    plt.ylabel('频率')
    plt.grid(True)
    plt.show()
    
    # 绘制位移平方直方图
    plt.figure(figsize=(10, 6))
    plt.hist(displacement**2, bins=30, alpha=0.7)
    plt.title(f'{num_walks}次随机游走的位移平方分布')
    plt.xlabel('位移平方')
    plt.ylabel('频率')
    plt.grid(True)
    plt.show()
    
    # 半对数图
    plt.figure(figsize=(10, 6))
    plt.hist(displacement**2, bins=30, alpha=0.7, log=True)
    plt.title(f'{num_walks}次随机游走的位移平方分布 (半对数)')
    plt.xlabel('位移平方')
    plt.ylabel('频率 (对数尺度)')
    plt.grid(True)
    plt.show()
    
    # 计算均方位移
    mean_squared_displacement = np.mean(displacement**2)
    print(f"{num_steps}步随机游走的均方位移: {mean_squared_displacement:.2f}")
    
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
    
    for steps in step_sizes:
        msd = analyze_walks_statistics(num_walks=500, num_steps=steps)
        msd_values.append(msd)
    
    # 绘制均方位移与步数的关系
    plt.figure(figsize=(10, 6))
    plt.plot(step_sizes, msd_values, 'o-', linewidth=2)
    plt.title('均方位移与步数的关系')
    plt.xlabel('步数')
    plt.ylabel('均方位移')
    plt.grid(True)
    plt.show()
    
    # 对数-对数图
    plt.figure(figsize=(10, 6))
    plt.loglog(step_sizes, msd_values, 'o-', linewidth=2)
    plt.title('均方位移与步数的关系 (对数-对数)')
    plt.xlabel('步数 (对数尺度)')
    plt.ylabel('均方位移 (对数尺度)')
    plt.grid(True)
    plt.show()
    
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