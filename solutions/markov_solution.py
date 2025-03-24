import random
import sys
import os

def process_line(line, k=1):
    '''
    Process a line of text to extract (state, new_word) pairs.
    Note that we remove uppercase letters in this example, though
    you don't have to.

    Example:
    process_line("In winter I get up at night") =
    [('BEGIN', 'in'),
     ('in', 'winter'),
     ('winter', 'i'),
     ('i', 'get'),
     ('get', 'up'),
     ('up', 'at'),
     ('at', 'night'),
     ('night', 'END')]

    We add the BEGIN and END keywords so that we can initialize the
    sentence and know when the line ends.
    '''
    # 将文本转换为小写并分割成单词
    words = line.lower().strip().split()
    if not words:
        return []
    
    transitions = []
    # 添加起始转换对
    transitions.append(('BEGIN', words[0]))
    
    # 添加单词之间的转换对
    for i in range(len(words)-1):
        transitions.append((words[i], words[i+1]))
    
    # 添加结束转换对
    if words:
        transitions.append((words[-1], 'END'))
    
    return transitions

def process_textfile(filename):
    '''
    Creates a dictionary with transition pairs
    based on a file provided

    For the first part of the assignment, we use a
    placeholder text that you will have to replace
    at some point.

    Based on the placeholder text, the dictionary
    should contain the following key-value pairs:

    'blue,': ['END']
    'by': ['yellow', 'day.', 'day?']
    'still': ['hopping', 'going']
    '''
    d = {}
    
    try:
        with open(filename, 'r') as f:
            # 读取每一行文本
            for line in f:
                line = line.strip()
                if not line:  # 跳过空行
                    continue
                    
                # 获取当前行的转移对
                transitions = process_line(line)
                
                # 将转移对添加到字典中
                for state, next_word in transitions:
                    if state not in d:
                        d[state] = []
                    d[state].append(next_word)
    except FileNotFoundError:
        print(f"错误：找不到文件 {filename}")
        return {}
    except Exception as e:
        print(f"处理文件时出错：{e}")
        return {}
    
    return d

def process_textfile(filename, k=1):
    """
    处理文本文件，构建状态转移字典
    """
    transitions = {}
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                # 获取当前行的转移对
                line_transitions = process_line(line, k)
                
                # 将转移对添加到字典中
                for state, next_word in line_transitions:
                    if state not in transitions:
                        transitions[state] = []
                    transitions[state].append(next_word)
    except FileNotFoundError:
        print(f"错误：找不到文件 {filename}")
        return {}
    except Exception as e:
        print(f"处理文件时出错：{e}")
        return {}
    
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

def generate_line(d):
    '''
    Generates a random sentence based on the dictionary
    with transition pairs

    Note that the first state is BEGIN but that we
    obviously do not want to return BEGIN

    Some sample output based on the placeholder text:
    'i have to go to go to go to go to play,'

    Hint: use random.choice to select a random element from a list
    '''
    if not d:
        return ""
    
    # 从BEGIN状态开始
    current_state = "BEGIN"
    words = []
    
    # 生成句子直到遇到END
    while True:
        if current_state not in d:
            break
            
        # 随机选择下一个单词
        next_word = random.choice(d[current_state])
        
        # 如果遇到END，结束生成
        if next_word == "END":
            break
            
        # 添加单词到结果中
        words.append(next_word)
        
        # 更新当前状态
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