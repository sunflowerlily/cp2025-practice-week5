import unittest
import sys
import os
import tempfile

# 添加源代码目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.markov import process_line, process_textfile, generate_line
#from solutions.markov_solution import process_line, process_textfile, generate_line

class TestMarkov(unittest.TestCase):
    def setUp(self):
        """创建测试用的临时文件"""
        self.test_text = '''In winter I get up at night
And dress by yellow candle-light.
In summer quite the other way,
I have to go to bed by day.'''
        
        # 创建临时文件
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
        self.temp_file.write(self.test_text)
        self.temp_file.close()

    def tearDown(self):
        """清理临时文件"""
        os.unlink(self.temp_file.name)

    def test_process_line_empty(self):
        """测试空行处理"""
        self.assertEqual(process_line(""), [])
        self.assertEqual(process_line("  "), [])
    
    def test_process_line_single_word(self):
        """测试单个单词的情况"""
        result = process_line("hello")
        expected = [("BEGIN", "hello"), ("hello", "END")]
        self.assertEqual(result, expected)
    
    def test_process_line_example(self):
        """测试文档中给出的示例"""
        result = process_line("In winter I get up at night")
        expected = [
            ('BEGIN', 'in'),
            ('in', 'winter'),
            ('winter', 'i'),
            ('i', 'get'),
            ('get', 'up'),
            ('up', 'at'),
            ('at', 'night'),
            ('night', 'END')
        ]
        self.assertEqual(result, expected)

    def test_process_textfile(self):
        """测试文件处理"""
        transitions = process_textfile(self.temp_file.name)
        
        # 测试一些预期的转换对
        self.assertIn('by', transitions)
        self.assertIn('yellow', transitions['by'])
        
        # 测试BEGIN和END的存在
        self.assertIn('BEGIN', transitions)
        self.assertTrue(any('END' in words for words in transitions.values()))

    def test_process_textfile_nonexistent(self):
        """测试处理不存在的文件"""
        transitions = process_textfile("nonexistent_file.txt")
        self.assertEqual(transitions, {})

    def test_generate_line(self):
        """测试文本生成"""
        # 创建一个简单的转换字典
        d = {
            'BEGIN': ['hello'],
            'hello': ['world', 'there'],
            'world': ['END'],
            'there': ['END']
        }
        
        # 生成多个句子并验证
        for _ in range(10):
            line = generate_line(d)
            # 验证生成的句子格式正确
            self.assertTrue(line.startswith('hello'))
            self.assertTrue(line.endswith('world') or line.endswith('there'))
    
    def test_generate_line_empty(self):
        """测试空字典的情况"""
        self.assertEqual(generate_line({}), "")

    def test_generate_line_single_word(self):
        """测试只有一个单词的情况"""
        d = {'BEGIN': ['hello'], 'hello': ['END']}
        self.assertEqual(generate_line(d), "hello")

if __name__ == '__main__':
    unittest.main()