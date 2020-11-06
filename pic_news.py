import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# from wordcloud import WordCloud
import thulac
thuseg = thulac.thulac(seg_only=True, filt = False)

basic_path = os.getcwd()

# def drawwordcloud(text, file_target):
#     font = basic_path + '/simfang.ttf'
#     wordcloud = WordCloud(background_color="white", font_path=font, collocations=False, width=1000, height=860, margin=2).generate(text)
#     wordcloud.to_file(file_target)

def drawtripic(h, record1, record2, label1, label2, picname, xname, yname, Ylim, picsize, file_target):
    y1 = []
    y2 = []
    for t in h:
        y1.append(float(record1[t]))
        y2.append(float(record2[t]))
    lenh = range(len(h))
    # print ('h = ', h)
    # print ('y = ', y)
    # plt.figure(figsize = picsize)
    plt.plot(lenh, y1, linewidth = 3, color = 'blue', label = label1)
    plt.plot(lenh, y2, linewidth = 3, color = 'red', label = label2)
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
rmrb = {'2010': 0, '2011': 1, '2012': 1, '2013': 4, '2014': 7, '2015': 40, '2016': 34, '2017': 28, '2018': 8, '2019': 14, '2020': 4}
gt = {'2010': 0, '2011': 0, '2012': 1, '2013': 3, '2014': 9, '2015': 22, '2016': 17, '2017': 31, '2018': 34, '2019': 25, '2020': 11}
nyt = {'2010': 0, '2011': 2, '2012': 1, '2013': 1, '2014': 1, '2015': 1, '2016': 0, '2017': 9, '2018': 2, '2019': 2, '2020': 1}
wsj = {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 1, '2017': 9, '2018': 5, '2019': 3, '2020': 0}

drawtripic(years, rmrb, gt, "People's Daily", "Global Times", 'Chinese_media', 'Year', 'Number of Articles', 0, 0, basic_path + '/pictures_news')
drawtripic(years, nyt, wsj, 'New York Times', 'Wall Street Journal', 'US_media', 'Year', 'Number of Articles', 0, 0, basic_path + '/pictures_news')

stopwords_zh = ['“', '”', '，', '。', '：', '的']
stopwords_en = ['the', 'to', 'in', 'and', 'including', 'of', 'as', 'have', 'has', '&amp;', 'by', 'out', 'is', 'on', 'with', 'a', 'other', 'had', 'will', 'issues', 'issue',
            'several', 'be', 'au…@gauravcsawant:', 'already', 'citing', 'new', 'over', 'wechat.\x00no…@abhijitmajumder:', 'full', 'story:', 'but', 'are',
            'about', '-', 'looking', 'i', 'his', 'for', 'this', 'at','it', 'after', 'he', 'same', 'from', 'faces', 'added', "it,'", 'amid', "'we're", 'now', 'do', 'come',
            'comes', 'case', 'says', 'into', 'more', 'also', 'should', 'than', 'used', 'due', 'all', 'between', 'its', 'an', 'how', 'my', 'see', 'you', 'name', 'after',
            'not', "what's", 'what', '\x00\x00', 'that', 'another', 'one', 'why', 'here', 'can', 'may', 'going', 'want', 'where', 'would', 'or', 'they', 'it,', 
            'same,', 'was', 'use', 'let', 'get', 'we', 'shouldn’t', "shouldn't", 'It’s', "It's", 'been', 'by', 'visited', 'visit', 'said', 'if', 'much', 'able', 'many',
            'say', 'big', 'which', 'set', 'some', 'make', 'made', 'makes', 'like', 'very']

rmrb_title = "命运与共呼唤团结合作，命运与共同凉热（中国制度面对面(14)），最难对付需要空前团结（人民论坛），中美应加强战略协调，为世界提供确定性和正能量，坚持和完善独立自主的和平外交政策（深入学习贯彻党的十九届四中全会精神），超越“认知藩篱” 消弭“理解赤字”，新时代的中国与世界，新时代的中国与世界，新时代的中国与世界，世上本无“修昔底德陷阱”，世上本无“修昔底德陷阱”，天下为公行大道（“今日之中国”系列述评），战略误判，后果严重，任何挑战都挡不住中国前进的步伐，任何挑战都挡不住中国前进的步伐，“中国未来一定会更好”（海客谈神州），大国当有合作的胸怀（钟声），美国乱贴“经济侵略”标签实属荒唐之举，全球变局的机遇与挑战，对“世纪之问”的理性思考，中国智慧推动国际合作（新知新觉），构建国际关系理论的中国学派（构建中国特色哲学社会科学），构建强起来的中国哲学（构建中国特色哲学社会科学），走出思维误区才能跨越陷阱（大家手笔），为世界提供更多国际公共产品（适势求是），世界，不确定中孕育着希望（权威论坛·寰宇·格局之变），世界，不确定中孕育着希望（权威论坛·寰宇·格局之变），破除“修昔底德陷阱”的迷思，合作共赢才是大国相处之道（人民观察），并不存在大国之间必有一战的规律（大家手笔），消弭“修昔底德陷阱”思维（势所必然），领航，思想的力量开辟新时代，领航，思想的力量开辟新时代，独立自主 崇尚和平（钟声·推动构建人类命运共同体⑧），战略引领，推动中美关系更大发展（钟声），共赢理念展现中国方案优势（势所必然），书写中国特色大国外交新篇章，推动中美关系行稳致远（钟声），避免落入西方学者预设的“陷阱”（热点辨析），众行致远，推动金砖合作再上新台阶（全球治理·中国担当），人类命运共同体理念引领人类文明进步方向（治国理政新理念新思想新战略），讲好中国的改革故事（新论），中国治理绽放独特魅力（人民观察），中美合作的需要远远大于分歧（钟声），深刻把握人类命运共同体的丰富内涵和构建路径（深入学习贯彻习近平同志系列重要讲话精神），军费增长避免陷入“修昔底德陷阱”（观点），美中两国可以实现双赢（高端访谈·中美关系），为新型国际关系提供学理支撑，携手共创自由贸易的未来（权威论坛），合作是中美两国唯一正确选择（钟声），美国应欢迎中国提供更多公共产品，共同构建人类命运共同体，全球治理，“中国力量”如何加码（新论），弘扬伟大的长征精神(人民要论)，建设各国共享的百花园(人民观点)，携手同行 合作共赢（治国理政新思想新实践·新理念带来新变化），携手同行 合作共赢（治国理政新思想新实践·新理念带来新变化），交出更加优异答卷的行动纲领（深入学习贯彻习近平同志系列重要讲话精神），不忘初心 继续前进 不断开拓治国理政新境界，事关根本利益就当锲而不舍（钟声），以机制性对话增信释疑（钟声），两面性有损中美战略互信（钟声），伟大成就坚定道路自信（思想纵横），如何跨越修昔底德陷阱，如何跨越修昔底德陷阱”时代主题变化决定了战争不能解决问题 中美不会陷入修昔底德陷阱，如何跨越修昔底德陷阱，关键是自身发展起来 以新型大国关系取代对抗性大国关系，如何跨越修昔底德陷阱，合则两利，斗则俱伤 公共外交时代更有条件合作共赢，如何跨越修昔底德陷阱  相互依赖  对话融通 全球价值链有助于抛弃冷战思维，标注治国理政新高度（治国理政新思想新实践），标注治国理政新高度（治国理政新思想新实践），莫让“冷战思维”影响中美关系（热点辨析），中华民族近代以来最伟大的梦想，正确认识“修昔底德陷阱”（人民观察·本期主题），告别传统大国冲突 的历史“铁律”（大家手笔），拓展全球开放型经济发展新境界（人民要论)，当代中国马克思主义哲学创新发展的典范（深入学习贯彻习近平同志系列重要讲话精神），从延续民族文化血脉中开拓前行（治国理政新实践），从延续民族文化血脉中开拓前行（治国理政新实践），凝聚共识，开创治理新境界（人民观点），大格局　大手笔　大胸怀（治国理政新实践），大格局　大手笔　大胸怀（治国理政新实践），以“世界意识”成就共同梦想（人民观点），阔步走在中华民族伟大复兴的历史征程上（治国理政新实践），阔步走在中华民族伟大复兴的历史征程上（治国理政新实践），阔步走在中华民族伟大复兴的历史征程上（治国理政新实践），以“使命意识”拓展中国道路（人民观点），站在中国与世界的命运交汇点，站在中国与世界的命运交汇点，绽放中国特色　共创世界未来，人类发展之路上的追求与担当（钟声·学习习近平主席在联合国系列峰会上阐述的重要理念④），格局调整　局部震荡，格局调整　局部震荡，关系发展全局的深刻变革，关系发展全局的深刻变革，以“五大发展理念”引领新的变革（评论员观察），和平与发展是中国外交战略核心（国际论坛），以合作共赢理念引领国际关系，负责任大国形象的新诠释（专题深思），丰收之旅引领中美关系未来（钟声·习近平主席美国、联合国之行系列评论①），谱写跨越太平洋的合作新篇章，期望“跨越太平洋的合作”开启未来（人民论坛），习近平会见美国国会参众两院领导人，一步一个脚印构建中美新型大国关系，人民日报全媒体平台·2015·中央厨房烹制新闻美味），创造中美关系更美好明天（钟声），习近平同美国总统奥巴马会晤，在华盛顿州当地政府和美国友好团体联合欢迎宴会上的演讲，共同谱写中美合作新篇章，瞩望新型大国关系新航程，瞩望新型大国关系新航程，中国正在走和平发展的强国之路（人民要论），温故知新　继往开来，走好中美构建新型大国关系之路（大使随笔），管控分歧，把握中美关系大方向（权威论坛），构建中美新型大国关系具有重大意义，小算盘阻不了中美大生意（新论），中美，用合作夯实战略互信（权威论坛），坚持对话合作 不断向前发展（钟声），理解捍卫和平的“中国逻辑”（人民时评），共商安全合作  共话世界和平，以战略定力促中美关系行稳致远（钟声），对话·互信·合作，构建中美新型大国关系（权威论坛），推动中美新型大国关系取得新进展，坚定信心　把握方向（钟声），勇毅笃行开拓中国特色国家安全道路（深入学习贯彻习近平同志系列重要讲话精神），中美军事交流曲折向前（观点），中等发达国家之中国特征初探（人民要论），当中国梦想进入世界坐标（人民论坛），世界需要中美新型大国关系（国际论坛），让和平永驻人间，让和平永驻人间，和平发展，彰显智慧和担当(钟声·学习习近平主席访欧阐述的重要外交理念（7）)，新丝绸之路：两大文明的再度交汇未来掌握在我们自己手中（域外听风），中美专家研讨新型大国关系，坚定不移走和平发展道路 为实现  中华民族伟大复兴营造良好国际环境，时机重要　意义深远，中美要力避“修昔底德陷阱”（新论），在世界舞台彰显“责任大国”（畅怀），诚心实意做合作伙伴(国际论坛)"
gt_title = "中美关系：到丢弃幻想的时候了? 年轻人热捧“入关学”的思考，华盛顿为“历史妄想症”找替罪羊，扎牢南海和平稳定之锚，人大重阳问卷调查百名中国学者，九成受访者相信—— 中国能应对好美国“新冷战”攻势，多位美国权威冷战问题专家接受《环球时报》采访 推崇“新冷战”将让美国更痛苦，世界应给“问题解决者”中国更多信赖，美国黑石集团董事长兼联合创始人苏世民接受本报专访 2021年，大部分国家经济将复苏，修昔底德陷阱提出者格雷厄姆?艾利森接受《环球时报》专访： 疫情应成为美中管控竞争的契机，中国人为什么到非洲维和，亚洲前政要另种视角看“一带一路”，跳出权力转移误区看中美关系，让“新冷战”落空，中国就将笑到最后，美国知名学者、 哈佛大学教授约瑟夫 ·奈接受《环球时报》 专访“美中必有一战 ” 非美国主流看法，中尼 “世代友好” 跨越珠峰 中印 “龙象共舞” 维护和平习近平访南亚成果受瞩目，欧洲没有选择与美国站在一起，中国特色社会主义为什么 “行”，美国老布什美中关系基金会总裁方大为接受 《 环球时报》专访 “贸易战明年结束， 不管谁当总统，中美关系正能量真的变少了吗，“崛起的中国惠及我们所有人”，中国实践大步向前，中国理论得跟上，战略稳定框架让中美都受益，中美的未来难从历史中找到答案，如何判断美国对华政策的转变，爱尔兰媒体转载美国知名国际问题学者裴敏欣的文章 将对华竞争视为文明冲突，愚蠢！应对共同挑战，中美该存异求同 《环球时报》记者：在美参加“全球创业峰会”，我仿佛身处中国某内地省份，什么才是今天最大的“全球性问题”，冷战史权威专家、哈佛大学学者文安立接受本报专访 中美“冷战2.0”是无稽之谈，大国国民心态的修炼过程无法省略，“修昔底德陷阱”当然是可避免的，西方人对中国认知变化的根源，中国如何跨越“第二经济大国陷阱”，在国际舆论场上保持定力和微笑，中美应当寻找真正的共同敌人，中美当然可以走出“历史窠臼”，“修昔底德陷阱”提出者艾利森接受《环球时报》记者专访：让美国接受中国崛起，过程会很长，2019，中美关系向何处去——环球时报年会第一议题嘉宾讨论精彩内容摘编，世界结构性矛盾正愈益显现，绕过四大陷阱，中国使出四招，非洲应向世界讲述与中国的故事，美国社会纠偏机制仍在起作用，反思“一战”须跳出西方逻辑陷阱，约瑟夫·奈：中美进入“合作竞争”阶段，中美之间，“战争”可以避免——华盛顿需掂量十个重大问题，造谣中国干涉被批粗鲁  借口“大国竞赛”转移焦点 彭斯演讲，美国要走“新冷战”之路？为特朗普的无端指责造势，无凭无据无人信 美公司诬中国钓鱼邮件干涉选举，跳出经验主义牢笼看问题，牛津大学中国研究中心主任拉纳?米特接受《环球时报》专访 中美关系不会掉进“修昔底德陷阱”，中国今年最大主场外交     中非关系新的历史时刻  中非合作论坛今天开峰会，事关世界秩序大棋局的中美关系，中国改革开放40年释放的信息，改革开放40年，成功秘诀何在，印媒：中美终将达成平衡贸易关系，世界和平论坛秘书长、清华大学国际关系研究院院长阎学通接受本报专访 中美有机会避免“模式之争”，美对华冷战判断是完全错误的，抹黑中国贷款，美报告用心恶劣，美国行事像外星人，自私且反历史，跨越各色“陷阱”的陷阱，世界多极化呼唤全球合作新框架，中国崛起超越大国对抗逻辑，从资本三百年看全球治理的未来，“陷阱说”本身，可能就是个“陷阱” ，美智库臆想大国冲突“18种状况”，伟大复兴不以赶超美国为目标，用智慧化解中美敏感问题的“对抗性” ，知识才是大国竞争制高点，中印接下来到底该如何相处，“大国崛起必有一战”思维过时了，专访美国著名国际关系理论学者、普林斯顿大学教授罗伯特·基欧汉 中国崛起势必带来冲突？错！世界会走向混沌不清、方向迷离吗，中美博弈是“变和”而非“零和”，修昔底德陷阱？不必担心！感叹崛起势头强劲 认为内外挑战不少 外媒称中国是2017年赢家 ，提质增效稳中求进 防控风险重中之重 外媒聚焦中国进入“后GDP时代” ，英媒出歪招对付中国“锐实力”，对“反恐大联盟”不可期望太高，又到重塑国际权责平衡的时候了，中美大战略在“互动式调整” ，中美走向更有韧性的战略稳定关系，“修昔底德陷阱”已成伪命题，美智库：中国需跨越四个陷阱，中国建设现代化强国，外界无需担心，中国的2050年目标不是我赢你输的，中美关系转型升级呈现出新特征，新时代的中国将如何与世界对接五年历史性变革后，新时代不会失约，西方对中国从不屑到惊慌，中美之间的下一个文明冲突，美俄互怼加剧下的中国战略运筹，是不是谁的经济军事实力最强，谁就是对国际社会的最大威胁？ 中方驳斥美“最大威胁”说，美学者：美不会被盟友拖入对华战争，美韩罕见公开实弹演练 平壤严厉警告“军事赌博”朝批美轰炸机在“火药库玩火” ，中东版“修昔底德陷阱”难生热战，中国专家更懂特朗普外交？中俄关系成功避开修昔底德陷阱，期待习特会为中美关系做战略定调，全球性知识短缺或导致严重后果，亚洲无需外部平衡器，东北亚秩序重置需新外交想象力，法媒：特朗普对华须避金德尔伯格难题，我们没有误解新加坡，中美构筑桥梁需要新基辛格，大国需要培育信任，中国更有可能避免别人犯过的错误，逾万民众夹道欢迎 多项协议昨天签署 柬埔寨欢呼习近平来访，美国是一辆停不下来的“战车” ，突破东亚困局要靠非传统思路，决心避免战略误判 直面沟通棘手议题 中美对话寻求管控分歧，随时树敌，美国的战略“刚需” ，开展大国外交正处在关键时刻，中美“修昔底德陷阱”的另一面，南海问题：沉住气、全面看、有信心，中美只有“交心”才能避免战略误判，战略引导是习奥会的首要价值，西方能量正枯竭，希望在中国，发现利益汇合点，中美合作可办大事，中美关系的悖论，美媒：遏制中国只会付出代价，听约瑟夫·奈纵论2015，中国为走出“发展的焦虑”探寻路径，2049年，中国会怎样，日媒：应庆幸现在的美中关系，对华战略言行不一的美式纠结，中美关系已过临界点？亚太安全取决于中美合作，45万亿，美中经济的差距，炒作“修昔底德陷阱”是种学术讹诈，联大演讲展现大国担当 白宫会晤“校正”中美关系 外媒盘点习近平美国行，前美国安局局长、首任网络司令部司令接受《环球时报》专访 前“黑客沙皇”看好美中网络合作，拒绝“修昔底德陷阱”，习奥共划底线，“上访”般泡沫干扰不了习近平访美，美国白宫宣布将设国宴 中国外长强调增信释疑 习近平主席下周访美国，智库与军方专家、议员、媒体正掀起前所未有的对华政策大辩论 听十名美国顶尖学者论中美，中美关系重心的历史性调整，美国“莽汉式博弈”才是真危险，莫用历史旧逻辑往中美身上套，索罗斯“世界大战论”逻辑荒诞，日媒：“修昔底德陷阱”不适用于中美，亚投行改写国际体系变革方式，美媒：须直面中国的四种挑战，美中滑向“战争不可避免论”? 中美掉入修昔底德陷阱了吗，美智库：北京为何重欧轻美，官方交流 “真诚而坦率” 媒体争论 “谁教训了谁” 美防长结束在华 “ 碰硬之旅”，日媒：中美陷入“囚徒困境”，探究中美关系冷暖 聚焦大国对俄态度 世界舆论反复琢磨“习奥会” ，欧盟该睁眼看世界了，披露钓鱼岛应对方案 建议自卫队主动开火 日本预想迫降中国军机，猜忌主导下的中日关系很危险，安保条约或成美日互设的陷阱，新报：美应减轻北京的焦虑，南海统一战线东盟不积极 重返亚太战略国内唱反调 希拉里亚洲行不会轻松 "
nyt_title = "The Chinese Decade The Lesson History Teaches Is Tragic; THE STONE China’s Global Message: We Are Tough but Not Threatening; News analysis Dambisa Moyo Dambisa Moyo: By the Book; By the Book 100 Notable Books of 2017 Letters Letters to the Editor Editors' Choice | Staff Picks From the Book Review 9 New Books We Recommend This Week China's World Corrections Giving China A Void to Fill North Korea and the new unthinkable A Guide to Xi Jinping’s Cultural Shout-Outs in Seattle Resetting U.S.-China Relations Obama and Xi Must Think Broadly to Avoid a Classic Trap The Obama Doctrine The ThucydidesTrap; Schott's Vocab Superpower and Upstart: Sometimes It Ends Well"
wsj_title = "Streetwise: Time to Wake Up to the Realities of a U.S.-China Split Global Power Shifting East A Sino-Russian Entente Again Threatens America; The U.S. must revise its policy toward Moscow if it is to meet the threat from a rising China. Who Read What in 2018: Business and Economics; Howard Marks on Factfulness, Mary Barra on The Hate U Give, and more. REVIEW --- Books of the Year: 12 Months of Reading --- Avid readers -- from Gisele Bundchen and Susan Orlean to Ben Sasse and David Solomon -- tell us what they loved in 2018 Imperialism Will Be Dangerous for China Ray Dalio's Rapidly Changing Views on China; The hedge fund founder now sees a chance of outright war An Uneasy Unpeace Behold the New Emperor of China Behold the New Emperor of China; Xi Jinping is the most powerful leader since Mao, and he is set to hold power for as long as he wants. REVIEW --- China Takes On The Tycoons --- Xi Jinping has tightened his grip on the party and the military; Now he is determined to prevent the rise of Russia-style oligarchs From Cicero to Trump, They're All in Plutarch's 'Lives' Playing Chicken With China World News -- China's World: Historic 'Trap' Makes Setting Odds of China-U.S. War Tough World News -- China's World: What Are the Chances of a U.S.-China War? Books: Collision Course Collision Course China, the U.S. and the ‘ThucydidesTrap:’ Q&A with Professor Harry Harding"

def words_frequency_zh(inputfile, outputfile1, outputfile2, stopwords_, file_result):
    # 获得词频
    print ("1、开始计算词频...")
    wordlist = inputfile.split()
    counted_words = []
    words_count = {}
    for i in range(len(wordlist)):
        if wordlist[i] not in counted_words:
            counted_words.append(wordlist[i])
            words_count[wordlist[i]] = 1
            for j in range(i+1, len(wordlist)):
                if wordlist[i] == wordlist[j]:
                    words_count[wordlist[i]] += 1
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

def words_frequency_en(inputfile, outputfile1, outputfile2, stopwords_, file_result):
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

rmrb_title = thuseg.cut(rmrb_title, text=True)
gt_title = thuseg.cut(gt_title, text=True)

words_frequency_zh(rmrb_title, 'words_frequency_original', 'words_frequency_no_stopwords', stopwords_zh, basic_path + 'pictures_news')
words_frequency_zh(gt_title, 'words_frequency_original', 'words_frequency_no_stopwords', stopwords_zh, basic_path + 'pictures_news')
words_frequency_en(nyt_title, 'words_frequency_original', 'words_frequency_no_stopwords', stopwords_en, basic_path + 'pictures_news')
words_frequency_en(rwsj_title, 'words_frequency_original', 'words_frequency_no_stopwords', stopwords_en, basic_path + 'pictures_news')

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