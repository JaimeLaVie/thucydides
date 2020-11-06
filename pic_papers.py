# coding=utf-8
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

def drawtripic(h, record1, picname, xname, yname, Ylim, picsize, file_target):
    y1 = []
    for t in h:
        y1.append(float(record1[t]))
    lenh = range(len(h))
    # print ('h = ', h)
    # print ('y = ', y)
    # plt.figure(figsize = picsize)
    plt.plot(lenh, y1, linewidth = 3, color = 'blue')
    plt.xticks(lenh, h, rotation = 45)
    plt.tick_params(axis='x', labelsize = 16)
    plt.tick_params(axis='y', labelsize = 16)
    # plt.ylim(Ylim)
    font_x = {'family': 'Times New Roman', 'weight': 'normal', 'size'   : 16}
    font_y = {'family': 'Times New Roman', 'weight': 'normal', 'size'   : 16}
    font_title = {'family': 'Times New Roman', 'weight': 'normal', 'size'   : 20}
    plt.xlabel(xname, font_x)
    plt.ylabel(yname, font_y)
    plt.title(picname, font_title)
    # plt.legend()
    plt.legend(loc = 0, prop = {'size':15})
    plt.savefig(file_target + "/{}.jpg".format(picname))
    plt.clf()

years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
eng = {'2010': 0, '2011': 0, '2012': 0, '2013': 1, '2014': 2, '2015': 1, '2016': 4, '2017': 16, '2018': 16, '2019': 30, '2020': 14}
zhn = {'2010': 0, '2011': 0, '2012': 1, '2013': 6, '2014': 18, '2015': 62, '2016': 86, '2017': 66, '2018': 91, '2019': 69, '2020': 18}

drawtripic(years, eng, 'English Papers', 'Year', 'Number of Papers', 0, 0, basic_path + '/pictures')
drawtripic(years, zhn, 'Chinese Papers', 'Year', 'Number of Papers', 0, 0, basic_path + '/pictures')

