# 计算物理实践 - 第五周作业

本仓库包含计算物理实践课程第五周的编程作业，涵盖多个随机过程的数值模拟与数据分析。

## 目录结构

```
cp2025-practice-week5/
├── data/                      # 数据文件目录
│   └── sample_text.txt        # 随机文本生成器的示例文本
├── src/                       # 源代码目录（学生实现）
│   ├── random_walk.py         # 随机游走模拟
│   ├── rare_events.py         # 稀有事件模拟
│   └── markov.py             # 随机文本生成器
├── results/                   # 结果目录
│   ├── random_walk_report.md  # 随机游走实验报告
│   ├── rare_events_report.md  # 稀有事件实验报告
│   └── markov_report.md      # 文本生成实验报告
├── solutions/                 # 参考解答目录
│   ├── random_walk_solution.py
│   ├── rare_events_solution.py
│   └── markov_solution.py
├── tests/                     # 测试文件目录
│   ├── test_random_walk.py
│   ├── test_rare_events.py
│   └── test_markov.py
├── docs/                      # 文档目录
│   ├── 随机行走模拟.md
│   ├── 稀有事件.md
│   └── 随机文本生成器.md
├── .github/                   # GitHub配置目录
│   └── workflows/             # GitHub Actions工作流
│       └── classroom.yml      # 自动评分配置
├── requirements.txt           # 项目依赖
└── README.md                  # 本文件
```

## 作业内容

本次作业包含三个独立的随机过程模拟：

1. **随机游走模拟**：实现二维随机游走，研究其统计特性。
2. **稀有事件模拟**：实现泊松分布和等待时间分析。
3. **随机文本生成器**：基于马尔可夫链实现文本生成。

## 使用说明

### 运行测试
```bash
# 运行所有测试
python -m pytest tests/

# 运行特定测试
python -m pytest tests/test_random_walk.py -v
```
### 提交作业
1. 完成 src/ 目录下的所有实现文件
2. 确保所有测试通过
3. 提交到GitHub仓库
4. 在 results/ 目录下对应的markdown文件中上传程序运行结果，包括生成的图像文件和结果讨论
## 评分标准
每个模型实现占15分，总分45分。评分将通过自动测试完成，测试通过即得满分。

## 参考资料
- 《Python物理建模初学者指南》第六章