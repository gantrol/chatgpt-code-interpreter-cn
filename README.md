# chatgpt-code-interpreter-cn

## 不支持xx库，怎么办？

以导入结巴（jieba）库为例：（概率成功，估计会被修复）

![导入结巴库](assets/导入结巴库.png)

## 不支持中文分词

直接下载结巴（[jieba · PyPI](https://pypi.org/project/jieba/#files)）库，上传后要求安装（概率成功，估计会被修复）

![导入结巴库](assets/导入结巴库.png)

## 中文自然语言分析，结果出了很多常用且无意义的词（停用词）

下载并上传停用词词表 https://github.com/CharyHong/Stopwords/blob/main/stopwords_cn.txt