# thucydides
数据收集：Google Scholar检索thucydides trap，时间2020.11.05下午14:27，自定义时间范围：2010至今。按相关性排序，不限语言，
不包括专利，不包括引用，不包括书籍，不包括学位论文。检索结果前50篇，记录标题、作者、国家（以作者机构为准）、期刊（会议、机构）、
被引（以谷歌学术显示的为准）和摘要（或首尾两段）。保存在data_eng.jsonl中。

媒体数据使用Factiva（纽约时报、华尔街日报）和慧科新闻数据（人民日报、环球时报）收集2010.1.1至2020.11.6的所有提及修昔底德陷阱（'thucydides trap'）
的新闻报道。手动复制粘贴（或使用后羿采集器）保存在pictures_news文件夹的Excel中。

word_frequency.py计算论文摘要的词频，清点国家数，保存在corpus文件夹中。draw_wordvector.py画词向量图，保存在pictures文件夹中。

pic_papers.py画论文发表数量按年趋势图，保存在pictures文件夹中。

pic_news.py画媒体发文数量按年趋势图，并计算各媒体文章标题的词频，保存在pictures_news文件夹中。
