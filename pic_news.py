import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# from wordcloud import WordCloud

basic_path = os.getcwd()

# def drawwordcloud(text, file_target):
#     font = basic_path + '/simfang.ttf'
#     wordcloud = WordCloud(background_color="white", font_path=font, collocations=False, width=1000, height=860, margin=2).generate(text)
#     wordcloud.to_file(file_target)

def drawtripic(h, record1, record2, picname, xname, yname, Ylim, picsize, file_target):
    y1 = []
    y2 = []
    for t in h:
        y1.append(float(record1[t]))
        y2.append(float(record2[t]))
    lenh = range(len(h))
    # print ('h = ', h)
    # print ('y = ', y)
    # plt.figure(figsize = picsize)
    plt.plot(lenh, y1, linewidth = 3, color = 'blue', label='Positive Percentage')
    plt.plot(lenh, y2, linewidth = 3, color = 'green', label='Negative Percentage')
    plt.xticks(lenh, h, rotation = 45)
    plt.tick_params(axis='x', labelsize = 16)
    plt.tick_params(axis='y', labelsize = 25)
    # plt.ylim(Ylim)
    font_x = {'family': 'Times New Roman', 'weight': 'normal', 'size'   : 28}
    font_y = {'family': 'Times New Roman', 'weight': 'normal', 'size'   : 28}
    font_title = {'family': 'Times New Roman', 'weight': 'normal', 'size'   : 40}
    plt.xlabel(xname, font_x)
    plt.ylabel(yname, font_y)
    plt.title(picname, font_title)
    # plt.legend()
    plt.legend(loc = 0, prop = {'size':35})
    plt.savefig(file_target + "/{}.jpg".format(picname))
    plt.clf()

years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
nyt = {'2010': 0, '2011': 2, '2012': 1, '2013': 1, '2014': 1, '2015': 1, '2016': 0, '2017': 9, '2018': 2, '2019': 2, '2020': 1}
wsj = {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 1, '2017': 9, '2018': 5, '2019': 3, '2020': 0}

drawtripic(years, nyt, wsj, 'US_media', 'Year', 'Number of Articles', 0, 0, basic_path + '/pictures_news')

# drawwordcloud(tweets_pos_en, file_result + "/tweets_pos_en.png")
# drawwordcloud(tweets_neg_en, file_result + "/tweets_neg_en.png")
# drawwordcloud(tweets_pos_zh, file_result + "/tweets_pos_zh.png")
# drawwordcloud(tweets_neg_zh, file_result + "/tweets_neg_zh.png")
# drawwordcloud(tweets_pos_zhs, file_result + "/tweets_pos_zhs.png")
# drawwordcloud(tweets_neg_zhs, file_result + "/tweets_neg_zhs.png")
# drawwordcloud(tweets_pos_zht, file_result + "/tweets_pos_zht.png")
# drawwordcloud(tweets_neg_zht, file_result + "/tweets_neg_zht.png")

# common_words_en = ['China', 'National', 'Day', 'day', '70th', 'People', '70year']
# common_words_zh = ['中国', '国庆', '香港']
# common_words_zhs = ['中国', '国庆']
# common_words_zht = ['香港']

# drawwordcloud(delurl(tweets_pos_en, common_words_en), file_result + "/tweets_pos_delcom_en.png")
# drawwordcloud(delurl(tweets_neg_en, common_words_en), file_result + "/tweets_neg_delcom_en.png")
# drawwordcloud(delurl(tweets_pos_zh, common_words_zh), file_result + "/tweets_pos_delcom_zh.png")
# drawwordcloud(delurl(tweets_neg_zh, common_words_zh), file_result + "/tweets_neg_delcom_zh.png")
# drawwordcloud(delurl(tweets_pos_zhs, common_words_zhs), file_result + "/tweets_pos_delcom_zhs.png")
# drawwordcloud(delurl(tweets_neg_zhs, common_words_zhs), file_result + "/tweets_neg_delcom_zhs.png")
# drawwordcloud(delurl(tweets_pos_zht, common_words_zht), file_result + "/tweets_pos_delcom_zht.png")
# drawwordcloud(delurl(tweets_neg_zht, common_words_zht), file_result + "/tweets_neg_delcom_zht.png")