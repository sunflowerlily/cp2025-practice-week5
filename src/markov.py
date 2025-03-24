import random
import sys
import os

def process_line(line, k=1):
    """
    处理单行文本，提取状态转移对
    
    参数:
        line: 输入的文本行
        k: 状态包含的单词数量
        
    返回:
        transitions: 包含(当前状态, 下一个单词)的元组列表
    """
    # TODO: 实现文本行处理逻辑
    # 提示: 使用 line.split() 分割文本
    # 提示: 记得添加 BEGIN 和 END 标记
    
    return []

def process_textfile(filename, k=1):
    """
    处理文本文件，构建状态转移字典
    
    参数:
        filename: 文本文件路径
        k: 状态包含的单词数量
        
    返回:
        transitions: 状态转移字典
    """
    # TODO: 实现文件处理逻辑
    # 提示: 使用 open() 打开文件
    # 提示: 调用 process_line() 处理每一行
    
    return {}

def generate_line(transitions, k=1):
    """
    根据状态转移字典生成随机文本
    
    参数:
        transitions: 状态转移字典
        k: 状态包含的单词数量
        
    返回:
        line: 生成的文本行
    """
    # TODO: 实现文本生成逻辑
    # 提示: 从 BEGIN 状态开始
    # 提示: 使用 random.choice() 随机选择下一个单词
    
    return ""

if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) != 2:
        print("使用方法: python markov.py <文本文件>")
        sys.exit(1)
        
    # 获取文本文件路径
    filename = sys.argv[1]
    
    # 生成不同阶数的马尔可夫链文本
    for k in [1, 2]:
        print(f"\n使用 {k} 阶马尔可夫链生成文本:")
        transitions = process_textfile(filename, k)
        for _ in range(5):
            print(generate_line(transitions, k))