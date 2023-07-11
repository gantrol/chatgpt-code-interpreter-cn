# chatgpt-code-interpreter-cn

## 问题

### 不支持xx库，怎么办？

以导入结巴（jieba）库为例：（概率成功，估计会被修复）

![导入结巴库](assets/导入结巴库.png)

### 不支持中文分词

直接下载结巴（[jieba · PyPI](https://pypi.org/project/jieba/#files)）库，上传后要求安装（概率成功，估计会被修复）

![导入结巴库](assets/导入结巴库.png)

### 中文自然语言分析，结果出了很多常用且无意义的词（停用词）

下载并上传停用词词表 https://github.com/CharyHong/Stopwords/blob/main/stopwords_cn.txt

## 机器学习

### 最简单的手写识别

下载[mnist数据集](http://yann.lecun.com/exdb/mnist/)，参考：https://chat.openai.com/share/14393776-5d48-48bb-8eee-a0229cb23359

试了一下：

![img.png](assets/机器学习识别8.png)

