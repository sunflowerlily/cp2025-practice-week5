import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

def calculate_poisson_pmf(l_values, lambda_val=8):
    """
    计算泊松分布概率质量函数
    
    参数:
        l_values: l值数组
        lambda_val: 泊松分布参数λ
        
    返回:
        概率数组
    """
    # TODO: 实现泊松分布概率计算
    # 提示: 使用 np.exp() 和 factorial() 函数
    
    return None

def simulate_coin_flips(N=1000, n=100, p=0.08):
    """
    模拟不公平硬币的翻转
    
    参数:
        N: 试验次数
        n: 每次试验的翻转次数
        p: 正面朝上的概率
        
    返回:
        heads_count: 每次试验中正面的次数数组
    """
    # TODO: 实现硬币翻转模拟
    # 提示: 使用 np.random.random() 生成随机数
    
    return None

def analyze_waiting_times(num_flips=1000, p=0.08):
    """
    分析连续正面之间的等待时间
    
    参数:
        num_flips: 翻转总次数
        p: 正面朝上的概率
        
    返回:
        waiting_times: 等待时间数组
    """
    # TODO: 实现等待时间分析
    # 提示: 使用 np.nonzero() 和 np.diff() 函数
    
    return None

def plot_distribution_comparison(experimental_data, theoretical_data):
    """
    比较实验分布和理论分布
    
    参数:
        experimental_data: 实验数据
        theoretical_data: 理论数据
    """
    # TODO: 实现分布比较的可视化
    # 提示: 使用 plt.hist() 和 plt.plot() 函数
    
    pass

if __name__ == "__main__":
    # 任务a: 绘制泊松分布
    l_values = np.arange(0, 20, dtype=float)
    pmf = calculate_poisson_pmf(l_values)
    
    # 任务b-d: 模拟硬币翻转并与理论分布比较
    heads_count = simulate_coin_flips()
    theoretical_pmf = calculate_poisson_pmf(np.arange(0, max(heads_count)+1))
    plot_distribution_comparison(heads_count, theoretical_pmf)
    
    # 任务a-b: 分析等待时间
    waiting_times = analyze_waiting_times()
    print(f"平均等待时间: {np.mean(waiting_times):.2f}")