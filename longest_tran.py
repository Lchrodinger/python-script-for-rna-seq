# _*_  coding: utf-8 _*_
"""
@authur: lyr
@Date: 2019/12/10
@Description: A script to extract the longest transcript sequences from fasta file and designate as the corresponding gene sequence.
"""
import sys

def Usage():
    print('Usage: python3 script_name.py [fasta_file] [output_file]')
def readfasta(filename):
    fa = open(filename, 'r')
    res = {}
    ID = ''
    for line in fa:
        if line.startswith('>'):
            ID = line.strip('\n')
            res[ID] = ''
        else:
            res[ID] += line.strip('\n')
    return res

res = readfasta(sys.argv[1])
uniq = {}
longest = 0
for k,v in res.items():
    i = k.split(' ', 1)
    if len(i) == 1:
        title = (i[0]).split('.')
        title = '.'.join(title[:2])+'\n'
    else:
        title = (i[1]).split('=')
        title = '>'+title[1]+'\n'
    v = [v]
    if title not in uniq:
        uniq[title] = v
    else:
        uniq[title] += v

max_seq = {}
for k,v in uniq.items():
    seq = max(v, key = len)
    max_seq[k] = seq+'\n'

w = open(sys.argv[2], 'w')
for k,v in max_seq.items():
    w.write(k)
    w.write(v)
w.close

try:
    main()
except:
    Usage()

