import random
import sys
import os

def process_line(line, k=1):
    """
    处理单行文本，提取状态转移对
    """
    # 分割文本为单词列表
    words = line.strip().split()
    if not words:
        return []
    
    # 添加开始和结束标记
    words = ["BEGIN"] * k + words + ["END"]
    transitions = []
    
    # 提取状态转移对
    for i in range(len(words) - k):
        # 当前状态（k个单词）
        current_state = " ".join(words[i:i+k])
        # 下一个单词
        next_word = words[i+k]
        transitions.append((current_state, next_word))
    
    return transitions

def process_textfile(filename, k=1):
    """
    处理文本文件，构建状态转移字典
    """
    transitions = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                # 处理每一行文本
                line_transitions = process_line(line, k)
                
                # 更新转移字典
                for current_state, next_word in line_transitions:
                    if current_state not in transitions:
                        transitions[current_state] = []
                    transitions[current_state].append(next_word)
    except FileNotFoundError:
        print(f"错误：找不到文件 {filename}")
        sys.exit(1)
    except Exception as e:
        print(f"处理文件时出错：{e}")
        sys.exit(1)
    
    return transitions

def generate_line(transitions, k=1):
    """
    根据状态转移字典生成随机文本
    """
    if not transitions:
        return ""
    
    # 从BEGIN状态开始
    current_state = " ".join(["BEGIN"] * k)
    words = []
    
    # 生成文本直到遇到END
    while True:
        if current_state not in transitions:
            break
            
        # 随机选择下一个单词
        next_word = random.choice(transitions[current_state])
        
        if next_word == "END":
            break
            
        words.append(next_word)
        
        # 更新当前状态
        if k > 1:
            state_words = current_state.split()[1:] + [next_word]
            current_state = " ".join(state_words)
        else:
            current_state = next_word
    
    return " ".join(words)

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