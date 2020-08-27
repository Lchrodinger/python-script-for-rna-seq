# -*- coding: utf-8 -*-
# gene-trans.py
# @author liu yarong
# @description 
# @created 2020-07-11T10:56:17.478Z+08:00
# @last-modified 2020-07-11T11:47:24.242Z+08:00
#

import sys
if len(sys.argv) != 4:
    print('\nusage:\npython3 gene-trans.py<genome.fa><gene-trans.list><trans.fa>\n')
    exit()

# 统计gene和转录本的对应关系，并输出到gene-trans.list中
genome = open(sys.argv[1],'r')
gene_trans = open(sys.argv[2],'w')
transfa = open(sys.argv[3],'w')
for line in genome:
    line = line.strip() 
    if line.startswith('>'):
        line = line.split(' ')
        trans = line[0].split('>')[1]
        genes = line[1].split('=')[1]
        gene_trans.write(f'{genes}\t{trans}\n')
        transfa.write(f'{line[0]}\n')
    else:
        lines =line.strip('\n')
        transfa.write(lines+'\n')

gene_trans.close()
genome.close()
transfa.close()






 