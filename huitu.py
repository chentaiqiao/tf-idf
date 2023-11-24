import matplotlib.pyplot as plt
import numpy as np

def read_output(output_file):
    word_values = []
    with open(output_file, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):  # Enumerate the lines with line numbers
            try:#输出文档可能有空行
                word, tf, idf = line.strip().split(',')
                word_values.append((word, float(tf), float(idf)))
            except:
                pass
    # Sort words based on TF value in descending order
    word_values.sort(key=lambda x: x[1], reverse=True)
    return word_values

output_file = './tf_idf_output.txt'

# Read data from the output file
word_values = read_output(output_file)

x_old=range(1, len(word_values) + 1)
x_new=x_old
'''
x_new=[]
temp=0
index=1
for i in range(len(x_old)):
    if word_values[i][1]==temp:#相等序号
        x_new.append(index)
    else:#不相等序号
        x_new.append(index)
        index=index+1
    temp=word_values[i][1]
    '''

    
# Create scatter plot for TF and IDF values
plt.scatter(x_new, [tf for _, tf, _ in word_values], label='TF',s=1)
plt.scatter(x_new, [idf for _, _, idf in word_values], label='IDF', alpha=0.5,s=1)

#plt.xscale('log')

plt.xlabel('Word Number')
plt.ylabel('Value')
plt.title('TF and IDF Scatter Plot')
plt.legend()

plt.show()
plt.savefig('buquchong-nolog.png')
