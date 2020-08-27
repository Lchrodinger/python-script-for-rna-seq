#!/usr/bin/python3.6
# 用途：用于统计甜瓜基因组文件中每条染色体长度及N碱基的数目
# 创建人：lyr
# 创建时间： 2019/10/28
import re
input = '/mnt/f/rna-seq-project/2/reference/CM3.6.1_pseudomol.fa'
output = 'fasta_stat.txt'
dict = {}
dict2 = {}

with open(input, 'r') as read_fas:
    for line in read_fas:
        if line[0] == '>':
            key = line.strip('[>\n]')
            dict[key] = 0
            dict2[key] = 0
        else:
            value = line.strip()
            seq_len = len(value)
            dict[key] += seq_len
            N_sum = len(re.findall('[nN]',value))
            dict2[key] += N_sum
read_fas.close()

basic_stat = open(output, 'w')
print('chr length',dict, file = basic_stat)
print('Total N(bp):',dict2, file = basic_stat)



