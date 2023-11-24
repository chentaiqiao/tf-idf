# tf-idf
文档集分词，计算索引项的tf-idf，绘制散点图
# 运行步骤：
1.先去该链接下载数据集：http://www.nlpir.org/wordpress/category/corpus%E8%AF%AD%E6%96%99%E5%BA%93/page/2/
```
wget http://www.nlpir.org/wordpress/download/tc-corpus-answer.rar
```
然后解压rar
```
unrar x tc-corpus-answer.rar
```
解压后的answer文件夹包含20个子文件夹，这里我们把所有txt都提取到./answer/total文件夹方便后续处理
```
mkdir total
cp -r ./*/*.txt total/
```

2.安装jieba库
```
pip install jieba
```
3.下载本项目
4.运行程序
```
python calculate.py
python huitu.py
```
