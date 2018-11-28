#!/usr/bin/python
# -*- coding:utf-8 -*-
import jieba
from glob import glob
import os
import re
import pandas as pd





#     f = open('stopwords.txt','r',encoding='utf-8')

# def loadStopwords():
#     stopwords = []
#     for line in f.readlines():
#         stopwords.append(line.strip())
#     return stopwords

def seg(origin, file_dir,wordMatrix,pdfno):
    combine_dict = {}
    first_word = []
    index0=pdfno.find('\\')
    index = pdfno.rfind('\\')
    foldname=pdfno[index0+1:index0+5]
    pdfdate=pdfno[index+1:index+9]
    wordnum = [foldname,pdfdate]
    for line in open(file_dir, "r", encoding='utf-8-sig'):  # 把同义词存成字典
        seperate_word = line.strip().split("\t")
        first_word.append(seperate_word[0])
        num = len(seperate_word)
        first_word.append(seperate_word[0])
        for i in range(0, num - 1):
            combine_dict[seperate_word[i + 1]] = seperate_word[0]
        for word in seperate_word:
            origin=origin.replace(word,seperate_word[0])
        n =len(re.findall(seperate_word[0], origin))
        wordnum.append(n)
        # print(wordnum)
    wordMatrix.append(wordnum)
    print(wordMatrix)
    return wordMatrix
    # stopwords = loadStopwords()
    #
    # combine_dict = {}
    # first_word = []
    # for line in open(file_dir, "r", encoding='utf-8'):  # 把同义词存成字典
    #     seperate_word = line.strip().split("\t")
    #     num = len(seperate_word)
    #     first_word.append(seperate_word[0])
    #     for i in range(0, num - 1):
    #         combine_dict[seperate_word[i + 1]] = seperate_word[0]
    #     jieba.suggest_freq('马大', tune=True)  # 输入所有同义词典中的分词
    #     jieba.suggest_freq('马利亚', tune=True)
    #
    # seg_list = jieba.cut(origin.replace('\n', '')) #是否使用HMM模型
    # segs = list(seg_list)
    # for word in segs:
    #     if word in stopwords:
    #         segs.remove(word)
    # final_sentence = []
    # for word in segs:
    #     if word in combine_dict:
    #         word = combine_dict[word]
    #         final_sentence.append(word)
    #     else:
    #         final_sentence.append(word)

    # count = segs.count('马大')
    # print(count)

        # print(first_word[word])
        # count = segs.count(first_word[word])
        # print(count)



# return #'/'.join(segs)


# origin = open("C:\\\Users\\Administrator\\Desktop\\new\\a.txt", "r").read()
# origin = open("C:\\Users\\Deep Learning\\Desktop\\new\\a.txt","r",encoding='utf-8').read()
# jieba.suggest_freq("马大", tune = True)
# jieba.suggest_freq("大黑牛", tune = True)
# jieba.suggest_freq("能力者", tune = True)
# seg_list = jieba.cut(origin, cut_all = False)
# seg_list = jieba.cut(origin.replace('\n',''))
# f = "/".join(seg_list)
# fn = f.split("/")
# count = fn.count('马大')
# print(count)

def main():
    dir_path = 'C:/Users/Deep Learning/Desktop/new/fold'
    file_dir='C:/Users/Deep Learning/Desktop/new/dic.txt' # 同义词词典地址
    fold_list = glob(os.path.join(dir_path, '*'))

    wordMatrix = []
    for Pdf_fold_no in fold_list:
        pdf_list = glob(os.path.join(dir_path, Pdf_fold_no, '*.txt'))
        for pdfno in pdf_list:

            origin = open(pdfno, "r", encoding='utf-8-sig').read()
            wordMatrix = seg(origin,file_dir,wordMatrix,pdfno)

    df=pd.DataFrame(wordMatrix)
    df.to_csv('C:/Users/Deep Learning/Desktop/new/testcsv.csv',encoding='GB18030')#gb2312
            # fn = segs.split("/")
            # count=fn.count('马大')
            # print(count)



# output_1 = open("C:\\\Users\\Administrator\\Desktop\\new\\c.txt", "w")
#     output_1 = open("C:\\Users\\Deep Learning\\Desktop\\new\\c.txt", "wb+")
#     output_1.write(segs.encode('utf-8'))
#     output_1.close()
if __name__ == '__main__':
    main()

