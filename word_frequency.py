# -*- coding: utf-8 -*-
import os
import re
import json
import jsonlines
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
# import thulac
# thuseg = thulac.thulac(seg_only=True, filt = False)
# import MeCab                                           #日语分词
# mecab_tagger = MeCab.Tagger("-Owakati")


datafile = os.getcwd()+'/data_eng.jsonl'
file_result = os.getcwd() + "/corpus/"
# relevant_countries = ['us', 'uk', 'ca', 'au', 'nz', 'in', 'pk']
# relevant_countries = ['in']
# relevant_companies = ['h', 't', 'b']
# relevant_companies = ['b']
# badwords = ['约炮', '约 炮', '爆乳', '情趣', '迷奸', '内射', '吞精', '吞 精', '补肾', '偷情', '强奸', '捉奸', '轮奸', '献妻', '白翘', '宠幸', '屁眼', 'AV素人', '厕拍', '肥臀', 
#             '淫水', '啪啪', '女优', '女 优', '增大增粗', '潮吹', '潮 吹', '吃屌', '吃 屌', '裸照', 'porn']
# stopwords_zh = ['，', '的', '。', '、', '：', '和', '在', '中', '朝', '国', '了', '是', '“', '”', '为', '#', ':', '（', '）', '35520398', '🐱@', '_', '…@', '.', 'o', '去',
#                 '(', ')', '-', ',', '|', '就', '他们', '@', '…#', '要', '有', '看', '里', '地', '所', '一', '🐱#', '/', '】', '对', '！', '太', '真', '着', '很', '【', '入',
#                 '們', '写', '因为', '买', '来', '也', '。\x00PLAYTHE']
# stopwords_ja = ['の', 'が', 'で', 'を', 'は', '\x00@', 'た', 'に', 'て', 'れ', 'し', '，', '。', '、', '：', '“', '”', '#', ':', '（', '）', '🐱@', '_', '…@', '.', 'o', 
#                 '(', ')', '-', ',', '|', '@', '…#', '一', '🐱#', '/', '】', '【']
# stopwords_ko = []
# stopwords = {'zh': stopwords_zh, 'ja': stopwords_ja, 'ko': stopwords_ko}
# 不需要写大写的停用词，程序里判断时将text都变小写了。
stopwords = ['the', 'to', 'in', 'and', 'including', 'of', 'as', 'have', 'has', '&amp;', 'by', 'out', 'is', 'on', 'with', 'a', 'other', 'had', 'will', 'issues', 'issue',
            'several', 'be', 'au…@gauravcsawant:', 'already', 'citing', 'new', 'over', 'wechat.\x00no…@abhijitmajumder:', 'full', 'story:', 'but', 'are',
            'about', '-', 'looking', 'i', 'his', 'for', 'this', 'at','it', 'after', 'he', 'same', 'from', 'faces', 'added', "it,'", 'amid', "'we're", 'now', 'do', 'come',
            'comes', 'case', 'says', 'into', 'more', 'also', 'should', 'than', 'used', 'due', 'all', 'between', 'its', 'an', 'how', 'my', 'see', 'you', 'name', 'after',
            'not', "what's", 'what', '\x00\x00', 'that', 'another', 'one', 'why', 'here', 'can', 'may', 'going', 'want', 'where', 'would', 'or', 'they', 'it,', 
            'same,', 'was', 'use', 'let', 'get', 'we', 'shouldn’t', "shouldn't", 'It’s', "It's", 'been', 'by', 'visited', 'visit', 'said', 'if', 'much', 'able', 'many',
            'say', 'big', 'which', 'set', 'some', 'make', 'made', 'makes', 'like', 'very']

# def delurl(text, url):
#     for i in range (len(url)):
#         text = text.replace(str(url[i]), '')
#     return text

# def dataprep(text, lang):
#     url = re.findall(r'http[a-zA-Z0-9\.\?\/\&\=\:\^\%\$\#\!]*', text)
#     text = delurl(text, url)
#     if lang == 'zh':
#         text = thuseg.cut(text, text=True)
#     if lang == 'ja':
#         text = mecab_tagger.parse(text)
#     text = text.replace("\n", "\0")
#     if text[0:2] == 'RT':
#         text_delRT = text[3:]
#     else:
#         text_delRT = text
#     return text_delRT

def words_frequency(inputfile, outputfile1, outputfile2, stopwords_):
    # 获得词频
    print ("1、开始计算词频...")
    wordlist = inputfile.split()
    counted_words = []
    words_count = {}
    for i in range(len(wordlist)):                       # 先把带's的词的's全去掉
        if wordlist[i].endswith("'s"):
            wordlist[i] = wordlist[i][:-2]
        elif wordlist[i].endswith("'") or wordlist[i].endswith("’")  or wordlist[i].endswith(".")  or wordlist[i].endswith(","):
            wordlist[i] = wordlist[i][:-1]
    for i in range(len(wordlist)):
        lemmatized_word = wnl.lemmatize(wordlist[i])
        if lemmatized_word == 'ha':
            # print (wordlist[i])
            lemmatized_word = 'have'
        if lemmatized_word == 'wa':
            # print (wordlist[i])
            lemmatized_word = 'be'
        if lemmatized_word not in counted_words:
            counted_words.append(lemmatized_word)
            words_count[lemmatized_word] = 1
            for j in range(i+1, len(wordlist)):
                if wordlist[i] == wordlist[j]:
                    words_count[lemmatized_word] += 1
    # 合并词与对应频数
    print ("2、合并词与对应频数...")
    words = []
    counts = []
    for items in words_count:
        words.append(items)
        counts.append(words_count[items])
    combined = list(zip(words, counts))
    # 冒泡法排大小，获得未去除停用词的词频表
    print ("3、冒泡法排大小...")
    for k in range(len(combined)-1):
        for i in range(len(combined)-1):
            if combined[i][1] < combined[i+1][1]:
                variable = combined[i]
                combined[i] = combined[i+1]
                combined[i+1] = variable
    with open (file_result + "{}.txt".format(outputfile1), "w", encoding='utf-8') as file:
        file.write(str(combined))
    # 去除停用词后的词频表
    print ("4、去除停用词...")
    combined_no_stopwords = []
    for n in range(len(combined)):
        if combined[n][0].lower() in stopwords_:
            continue
        combined_no_stopwords.append(combined[n])
    with open (file_result + "{}.txt".format(outputfile2), "w", encoding='utf-8') as file:
        file.write(str(combined_no_stopwords))

print ("开始汇总语段：")

full_text = ''
# print (pairs)
with open (datafile, 'r', encoding='utf-8') as f:
    count = 0
    try:
        for article in jsonlines.Reader(f):
            count += 1
            # text = dataprep(tweets['abstract'], 'en')
            assert article['year'] >= 2010 and article['year'] <= 2020
            text = article['abstract']
            full_text += text
            with open (file_result + "full_text_en" + ".txt", "a", encoding='utf-8') as file:
                file.write(text + ' ')
    except:
        print (count)


# with open (file_result + 'full_text_en.jsonl', "w", encoding='utf-8') as file:
#     # file.write(str(text_all))
#     file.write(json.dumps(full_text)+'\n')

print ("开始求词频：")

words_frequency(full_text, 'words_frequency_original', 'words_frequency_no_stopwords', stopwords)

print ("完成！")
