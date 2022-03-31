"""
JSON_2_dict - JSON
操作系统: windows、iOS、Android、macOS、Linux、Unix
编程语言：python、Java、PHP、Go、C++

1. 两个异构的系统之间交换数据最好的选择是交换纯文本（可以屏蔽系统和编程语言的差异）
2. 纯文本应该是结构化或者半结构化的纯文本（有一定格式）
    - XML ---> extensible markup language --->可扩展标记语言
    - JSON ---> JavaScript Object Notation --->大多数网站和数据接口服务使用的数据格式
    - YAML ---> Yet another markup language
3. 如何将JSON格式转换成python程序中的字典
    json.loads
Author : wangyiwen03
Date : 2022/3/10
"""
import json

data = """{
  "code": 200,
  "msg": "success",
  "newslist": [
    {
      "id": "4045d520d5cb2d16418d7ae581fc9d26",
      "ctime": "2022-03-10 12:01",
      "title": "佳达隆邀您开学季春日晒晒征稿",
      "description": "为了让全国院校的莘莘学子们学习之余，不乏兴趣爱好的新天地，开学季，佳达隆邀您一起分享步入校园的独家故事，投稿美拍，晒精美独家风景。",
      "source": "新浪电竞",
      "picUrl": "//n.sinaimg.cn/games/transform/639/w400h239/20220310/232a-1ce620b32a753a2191ba7ccda25fe7d8.png",
      "url": "//dj.sina.com.cn/article/mcwiwss5217866.shtml"
    },
    {
      "id": "2e237df31babc989bdadad45d1cb87d4",
      "ctime": "2022-03-10 12:01",
      "title": "EPL S15：旗开得胜 G2横扫LFO",
      "description": "ESLProLeagueS15首日，小组循环赛第一场比赛由G2对阵LookingForOrg，G2指挥Aleksib不久前不...",
      "source": "新浪电竞",
      "picUrl": "//n.sinaimg.cn/games/transform/639/w400h239/20220310/5755-44d1fb9da15757b37b56003f304756e5.jpg",
      "url": "//dj.sina.com.cn/article/mcwipih7666758.shtml"
    },
    {
      "id": "2ce35da2c91058fdf8910f03fef54aee",
      "ctime": "2022-03-10 12:01",
      "title": "EPL S15：Forester与REZ的通天带！",
      "description": "EPLS15第一日：第二场比赛Entropiq对阵MOUZ，Forester爆炸火力稳定连杀是取胜MOUZ2-0的关键。第三场比赛...",
      "source": "新浪电竞",
      "picUrl": "//n.sinaimg.cn/games/transform/639/w400h239/20220310/4a9a-5843beac8aa76648ab77f0e9361b4887.jpg",
      "url": "//dj.sina.com.cn/article/mcwipih7667120.shtml"
    },
    {
      "id": "21041dc117eb574277fb2d28081f1f8c",
      "ctime": "2022-03-10 12:01",
      "title": "FalleN秀剃须新容，老f0称欲效仿",
      "description": "巴西教父FalleN昨日进行了“改头换面”，在基地展现出一副刮干净胡子的形象。",
      "source": "新浪电竞",
      "picUrl": "//n.sinaimg.cn/games/639/w400h239/20220310/239b-bbf97116c9278b2b0338c305d98e284f.jpg",
      "url": "//dj.sina.com.cn/article/mcwiwss5222728.shtml"
    },
    {
      "id": "7b6827cf11a788cb749a5853f9d474e3",
      "ctime": "2022-03-10 12:01",
      "title": "Thorin：G2应未雨绸缪，招揽device",
      "description": "分析师Thorin在他的推特上发布个人观点，他认为在当前国际形势下，如果m0NESY因签证问题无法继续为G2效力，那么管理层应该把de...",
      "source": "新浪电竞",
      "picUrl": "//n.sinaimg.cn/games/639/w400h239/20220310/fbeb-0ec99b4fae965b32e1d518de05b2dacf.jpg",
      "url": "//dj.sina.com.cn/article/mcwipih7667531.shtml"
    },
    {
      "id": "d298f6e27e73cc74424e4c359a60bd07",
      "ctime": "2022-03-10 12:01",
      "title": "Hooch：此前的Entropiq自我感觉过于良好",
      "description": "Entropiq教练Hooch在队伍2：0复仇MOUZ后接受了ESL的采访。",
      "source": "新浪电竞",
      "picUrl": "//n.sinaimg.cn/games/639/w400h239/20220310/71ae-566ae1a61c6ba4730bd36a7ed25fffd8.jpg",
      "url": "//dj.sina.com.cn/article/mcwiwss5223251.shtml"
    },
    {
      "id": "aa5157699d1198340de2c7cccb1e8780",
      "ctime": "2022-03-10 11:00",
      "title": "云顶之弈S6双城之战攻略：赌卡牌",
      "description": "11月4号云顶之弈S6赛季双城之战正式上线，这个版本可谓是百花齐放百家争鸣，任何阵容只要你大成那都是制霸王者，今天给大家介绍一个阵容—...",
      "source": "新浪电竞",
      "picUrl": "//n.sinaimg.cn/games/transform/639/w400h239/20211117/cf53-e5f9b8f078bb5bd3c328b5798d7a0fd5.png",
      "url": "//dj.sina.com.cn/article/mcwipih7656689.shtml"
    },
    {
      "id": "8e6fb30ba085b2fc743bf1a63337a48f",
      "ctime": "2022-03-09 18:00",
      "title": "瑞典数据分析组织公布全球假赛数据报告",
      "description": "疑似假赛的电竞比赛数据的领头羊地区是欧洲，占总数据的57%，其次是亚洲（19%），而北美则以17%的数据排在第三，南美洲和大洋洲各有不...",
      "source": "新浪电竞",
      "picUrl": "//n.sinaimg.cn/games/639/w400h239/20220309/7c0a-de0a32f86473e7bdedc0d2be0f69edc5.png",
      "url": "//dj.sina.com.cn/article/mcwipih7527040.shtml"
    },
    {
      "id": "1b4705a2b4de9c1e7d129048aba1840b",
      "ctime": "2022-03-09 18:00",
      "title": "Twistzz：2022年会是竞争最激烈的一年",
      "description": "近日，ropz和Twistzz两位选手来到了HLTVconfirmed节目做客，围绕ropz加入FaZe，IEM卡托维茨赛事回答了相关问题",
      "source": "新浪电竞",
      "picUrl": "//n.sinaimg.cn/games/639/w400h239/20220309/8314-7122fb6ff7fa553fb1b6380e14b51c16.jpg",
      "url": "//dj.sina.com.cn/article/mcwipih7527600.shtml"
    },
    {
      "id": "ce2d2f8c244d920a998ebf4d0e03fa0d",
      "ctime": "2022-03-09 18:00",
      "title": "ESL副总监：唯有线下才能体会CS的全部魅力",
      "description": "近日，ESL的产品发展副总裁MichalBlicharz接受了外媒的采访，在本次采访中他围绕IEM卡托维茨以及ESL未来的发展回答了...",
      "source": "新浪电竞",
      "picUrl": "//n.sinaimg.cn/games/transform/639/w400h239/20220309/0057-15c82b0faecbf0105dc5f339d7c2fd52.jpg",
      "url": "//dj.sina.com.cn/article/mcwipih7527601.shtml"
    }
  ]
}"""

#json.loads()将JSON格式的数据转换成python中的字典格式
news_dict = json.loads(data)
news_list = news_dict["newslist"]

for news in news_list:
    print(news['title'])
    print(news['url'])

