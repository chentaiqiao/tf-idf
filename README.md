# tf-idf
文档集分词，计算索引项的tf-idf，绘制散点图
# 运行步骤：
## 1.先去该链接下载数据集：http://www.nlpir.org/wordpress/category/corpus%E8%AF%AD%E6%96%99%E5%BA%93/page/2/
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

## 2.安装jieba库
```
pip install jieba
```
## 3.克隆本项目
```
git clone https://github.com/chentaiqiao/tf-idf.git
```
## 4.运行程序
计算文档集索引项的TF和IDF值，并保存到tf_idf_output.txt，该步骤需要较长时间，我在项目中给出了运行成功后的tf_idf_output.txt.
```
python calculate.py
```
读取tf_idf_output.txt中每个索引项的TF、IDF值排序后绘图
```
python huitu.py
```
