import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

def calculate_poisson_pmf(l_values, lambda_val=8):
    """
    计算泊松分布概率质量函数
    """
    # 使用浮点数数组避免溢出
    l_values = np.array(l_values, dtype=float)
    
    # 计算泊松分布概率
    pmf = np.exp(-lambda_val) * (lambda_val**l_values) / factorial(l_values)
    
    return pmf

def simulate_coin_flips(N=1000, n=100, p=0.08):
    """
    模拟不公平硬币的翻转
    """
    # 生成随机数矩阵并与概率比较
    flips = np.random.random((N, n)) < p
    
    # 计算每次试验中正面的次数
    heads_count = np.sum(flips, axis=1)
    
    return heads_count

def analyze_waiting_times(num_flips=1000, p=0.08):
    """
    分析连续正面之间的等待时间
    """
    # 生成硬币翻转序列
    flips = np.random.random(num_flips) < p
    
    # 找出所有正面的位置
    heads_positions = np.nonzero(flips)[0]
    
    # 计算连续正面之间的等待时间
    waiting_times = np.diff(heads_positions)
    
    # 绘制等待时间分布
    plt.figure(figsize=(10, 6))
    plt.hist(waiting_times, bins=30, alpha=0.7)
    plt.title('等待时间分布')
    plt.xlabel('等待时间')
    plt.ylabel('频率')
    plt.grid(True)
    plt.show()
    
    # 半对数图
    plt.figure(figsize=(10, 6))
    plt.hist(waiting_times, bins=30, alpha=0.7, log=True)
    plt.title('等待时间分布 (半对数)')
    plt.xlabel('等待时间')
    plt.ylabel('频率 (对数尺度)')
    plt.grid(True)
    plt.show()
    
    # 对数-对数图
    plt.figure(figsize=(10, 6))
    unique_times = np.unique(waiting_times)
    frequencies = [np.sum(waiting_times == t) for t in unique_times]
    plt.loglog(unique_times, frequencies, 'o-')
    plt.title('等待时间分布 (对数-对数)')
    plt.xlabel('等待时间 (对数尺度)')
    plt.ylabel('频率 (对数尺度)')
    plt.grid(True)
    plt.show()
    
    return waiting_times

def plot_distribution_comparison(experimental_data, theoretical_data):
    """
    比较实验分布和理论分布
    """
    plt.figure(figsize=(10, 6))
    
    # 绘制实验数据的直方图
    plt.hist(experimental_data, bins=range(int(max(experimental_data))+2),
             density=True, alpha=0.7, label='实验数据')
    
    # 绘制理论分布
    l_values = np.arange(len(theoretical_data))
    plt.plot(l_values, theoretical_data, 'r-', label='理论分布')
    
    plt.title('实验结果与理论分布比较')
    plt.xlabel('正面次数')
    plt.ylabel('概率/频率')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # 任务a: 绘制泊松分布
    l_values = np.arange(0, 20, dtype=float)
    pmf = calculate_poisson_pmf(l_values)
    plt.figure(figsize=(10, 6))
    plt.bar(l_values, pmf)
    plt.title('泊松分布 (λ=8)')
    plt.xlabel('l')
    plt.ylabel('P(l)')
    plt.grid(True)
    plt.show()
    
    # 任务b-d: 模拟硬币翻转并与理论分布比较
    heads_count = simulate_coin_flips()
    theoretical_pmf = calculate_poisson_pmf(np.arange(0, int(max(heads_count))+1))
    plot_distribution_comparison(heads_count, theoretical_pmf)
    
    # 任务e: 大规模模拟
    heads_count_large = simulate_coin_flips(N=1000000)
    theoretical_pmf = calculate_poisson_pmf(np.arange(0, int(max(heads_count_large))+1))
    plot_distribution_comparison(heads_count_large, theoretical_pmf)
    
    # 任务a-c: 分析等待时间
    waiting_times = analyze_waiting_times()
    print(f"平均等待时间: {np.mean(waiting_times):.2f}")
    
    # 大规模等待时间分析
    waiting_times_large = analyze_waiting_times(num_flips=1000000)
    print(f"大规模模拟的平均等待时间: {np.mean(waiting_times_large):.2f}")