# chatgpt-code-interpreter-cn

## 问题

- 关于虚机操作系统跟硬件配置，可见[虚机配置](虚机配置.md)
- 关于Python依赖包，可见[Python](python/Python.md)

### 不支持xx库，怎么办？

以导入结巴（jieba）库为例：（概率成功，估计会被修复）。链接： https://chat.openai.com/share/1242c227-feff-409d-9054-324386c92e2b

如果官方没有给whl包，或许需要非官方的whl包：https://www.lfd.uci.edu/~gohlke/pythonlibs/

### 不支持中文分词

直接下载结巴（[jieba · PyPI](https://pypi.org/project/jieba/#files)）库，上传后要求安装（概率成功，估计会被修复）

![导入结巴库](assets/导入结巴库.png)

### 中文自然语言分析，结果出了很多常用且无意义的词（停用词）

下载并上传停用词词表 https://github.com/CharyHong/Stopwords/blob/main/stopwords_cn.txt

## 限制

### 上传文件限制

https://chat.openai.com/share/4df43bab-57f9-4cbd-81c6-1c100e463333

- 大小上限：5GB
- 文件类型：上传无限制，但是处理能力要看依赖包。详见[文件类型](python/filetypes.md)

### 不支持中文分词

无稳定方法，见“问题”一节

### 硬件

- 主要问题是无GPU，关于其他虚机操作系统跟硬件配置，可见[虚机配置](虚机配置.md)

## 用途

### ChatGPT 说自己的用途

> 1. **数据分析**：你可以上传一些数据文件，比如CSV或者Excel文件，我可以帮你分析这些数据，生成统计报告，或者作图来可视化数据。
> 2. **文件转换**：我可以帮你把一种文件格式转换成另一种，比如把CSV文件转换成Excel文件，或者反过来。
> 3. **代码审查和修改**：你可以上传一些代码文件，我可以帮你审查代码，提供修改建议，或者帮你解决代码中的问题。
> 4. **机器学习模型训练和评估**：如果你上传了包含机器学习项目的文件，我可以帮你训练模型，评估模型性能，甚至帮你优化模型。
>
> 这只是其中一部分，实际上我能做的事情远不止这些。你有什么特别的需求吗？

### 机器学习

#### 最简单的手写识别

下载[mnist数据集](http://yann.lecun.com/exdb/mnist/)，参考：https://chat.openai.com/share/14393776-5d48-48bb-8eee-a0229cb23359

试了一下：

![img.png](assets/机器学习识别8.png)

#### 某AI课程的第一个作业，预测新冠未来情况

失败：https://chat.openai.com/share/cf1c0da0-8e0e-4cc1-92c9-58422e15a1f0

就连优化也是负优化：https://chat.openai.com/share/5f5fb472-2c30-4ceb-8da6-9c44f0a9bc56

#### 聚类分析

[Python 包聚类](https://chat.openai.com/share/4df43bab-57f9-4cbd-81c6-1c100e463333)

> 这是我们的聚类结果：
>
> - **Cluster 0** 包括 "Brotli", "Faker", "PyAudio", "PyNaCl", "Shapely" 等包。
> - **Cluster 1** 包括 "PyPDF2", "PyWavelets", "PyYAML", "anytree", "argcomplete" 等包。
> - **Cluster 2** 包括 "Flask", "Flask-CacheBuster", "Flask-Cors", "Flask-Login", "IMAPClient" 等包。
> - **Cluster 3** 包括 "ipykernel", "ipython", "jupyter-client", "jupyter-core", "jupyter-server" 等包。
> - **Cluster 4** 包括 "Babel", "CairoSVG", "EbookLib", "Fiona", "Jinja2" 等包。
>
> 聚类结果可能会提供一些洞见，比如 Cluster 2 中的包主要与 Flask 相关，Cluster 3 中的包主要与 Jupyter 有关。然而，这个结果并不完美，部分原因可能是我们随机选择了聚类数量，以及我们的数据可能没有明显的聚类结构。对于更好的结果，我们可能需要尝试不同的聚类数量，或者尝试其他的聚类算法或特征提取方法。

### 数据分析

#### 分析社交媒体个人账号

详见《[ChatGPT老师指导我运营微博](https://github.com/gantrol/BeyondAI/blob/main/ChatGPT老师指导我运营微博.md)》与《[ChatGPT老师教我运营即刻](https://github.com/gantrol/BeyondAI/blob/main/ChatGPT老师教我运营即刻.md)》

## 总结

像个实习生，凑合用吧，还能咋滴。

