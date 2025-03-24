import sys
import os
import pytest

# 添加src目录到Python路径
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import markov

def test_process_line():
    """测试单行文本处理"""
    # 测试基本功能 (k=1)
    line = "the cat sat"
    transitions = markov.process_line(line, k=1)
    expected = [
        ("BEGIN", "the"),
        ("the", "cat"),
        ("cat", "sat"),
        ("sat", "END")
    ]
    assert transitions == expected
    
    # 测试k=2的情况
    transitions = markov.process_line(line, k=2)
    expected = [
        ("BEGIN BEGIN", "the"),
        ("BEGIN the", "cat"),
        ("the cat", "sat"),
        ("cat sat", "END")
    ]
    assert transitions == expected

def test_process_textfile(tmp_path):
    """测试文本文件处理"""
    # 创建临时测试文件
    test_file = tmp_path / "test.txt"
    test_file.write_text("the cat sat\nthe dog ran")
    
    # 测试k=1的情况
    transitions = markov.process_textfile(str(test_file), k=1)
    assert "BEGIN" in transitions
    assert "the" in transitions
    assert len(transitions["the"]) == 2  # "cat" 和 "dog"
    
    # 测试k=2的情况
    transitions = markov.process_textfile(str(test_file), k=2)
    assert "BEGIN BEGIN" in transitions
    assert "the cat" in transitions
    assert "the dog" in transitions

def test_generate_line():
    """测试文本生成"""
    # 创建简单的转移字典
    transitions = {
        "BEGIN": ["the"],
        "the": ["cat", "dog"],
        "cat": ["END"],
        "dog": ["END"]
    }
    
    # 生成多个句子并检查
    for _ in range(10):
        line = markov.generate_line(transitions, k=1)
        words = line.split()
        assert words[0] == "the"
        assert words[1] in ["cat", "dog"]
        assert len(words) == 2

if __name__ == "__main__":
    pytest.main(["-v", __file__])