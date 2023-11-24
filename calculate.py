import os
import jieba
import math

def calculate_tf_idf(documents_folder, output_file):
    # 获取文件夹下所有txt文档的路径
    file_paths = [os.path.join(documents_folder, file) for file in os.listdir(documents_folder) if file.endswith('.txt')]

    # 计算每个词的词频（TF）和文档频率（IDF）
    word_idf = {}#每个词，在几个文档出现
    word_count = {}#每个词，在所有文档总次数
    total_documents = len(file_paths)

    for path in file_paths:#每篇文档
        with open(path, 'r',  encoding='gbk',errors='replace') as file:
            text = file.read()
            words = jieba.lcut(text)
        # 统计词频
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        # 统计词在文档中是否出现
        for word in set(words):
            word_idf[word] = word_idf.get(word, 0) + 1
            
    # 计算每个词的TF
    tf_values = {word: 1 + math.log(freq_sum) for word, freq_sum in word_count.items()
    # 计算每个词的IDF
    word_idf = {word: math.log(total_documents / idf) for word, idf in word_idf.items()}

    # 将结果写入输出文件
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, tf in tf_values.items():
            idf = word_idf[word]
            file.write(f"{word},{tf},{idf}\n")

documents_folder = './answer/total'  # 文档文件夹路径
output_file = './tf_idf_output.txt'  # 输出文件路径
calculate_tf_idf(documents_folder, output_file)