# -*- coding: utf-8 -*-
"""生成 卜卜岛 PONYO · 剧场岛镜 78 张塔罗独立剧情页。"""
import os

OUT = "/data/workspace/ponyo-divination-skill/modules/theatre"
os.makedirs(OUT, exist_ok=True)

MAJOR = [
    ("00","愚者","风","启程","莽撞"),
    ("01","魔术师","水星","创造","空谈"),
    ("02","女祭司","月亮","直觉","封闭"),
    ("03","皇后","金星","丰盛","匮乏"),
    ("04","皇帝","白羊","秩序","专制"),
    ("05","教皇","金牛","传承","盲从"),
    ("06","恋人","双子","选择","分裂"),
    ("07","战车","巨蟹","意志","失控"),
    ("08","力量","狮子","柔韧","压抑"),
    ("09","隐者","处女","内省","孤僻"),
    ("10","命运之轮","木星","转变","固执"),
    ("11","正义","天秤","平衡","偏私"),
    ("12","吊人","水","换位思考","牺牲"),
    ("13","死神","天蝎","终结","抗拒"),
    ("14","节制","射手","调和","失衡"),
    ("15","恶魔","摩羯","束缚","执念"),
    ("16","高塔","火星","崩塌","逃避"),
    ("17","星星","水瓶","希望","失望"),
    ("18","月亮","双鱼","潜意识","迷惘"),
    ("19","太阳","太阳","活力","过度"),
    ("20","审判","冥王","觉醒","自责"),
    ("21","世界","土星","圆满","停滞"),
]

MINOR = {
    "权杖":("火","行动"),
    "圣杯":("水","情感"),
    "宝剑":("风","思维"),
    "星币":("土","物质"),
}

def card_line(suit, num, elem, domain):
    if num == "ACE":
        n = "ace"; rank="ACE"
    elif num == "侍从":
        n = "侍从"; rank="侍从"
    elif num == "骑士":
        n = "骑士"; rank="骑士"
    elif num == "王后":
        n = "王后"; rank="王后"
    elif num == "国王":
        n = "国王"; rank="国王"
    else:
        n = num; rank=num
    return (n, rank, elem, f"{domain}·开启" if rank=="ACE" else f"{domain}·{rank}",
            f"{domain}·阻塞" if rank=="ACE" else f"{domain}·失衡")

cards = []
for code, name, elem, up, rev in MAJOR:
    cards.append((f"{code}_{name}", name, elem, up, rev, "大阿尔卡纳"))

# 小阿尔卡纳编号 22~77
idx = 22
for suit, (elem, domain) in MINOR.items():
    nums = ["ACE"] + [str(i) for i in range(2,11)] + ["侍从","骑士","王后","国王"]
    for num in nums:
        n, rank, el, up, rev = card_line(suit, num, elem, domain)
        code = f"{idx:02d}"
        cards.append((f"{code}_{suit}{num}", f"{suit}{num}", el, up, rev, "小阿尔卡纳"))
        idx += 1

assert len(cards) == 78, len(cards)

TEMPLATE = """# 剧场 · {name}（{arcana}）

- 编号：{code}
- 牌名：{name}
- 元素：{elem}
- 关键词 正位：{up}
- 关键词 逆位：{rev}

## 正位剧情
**图像象征**：（一句话，画面中的核心意象）

**对应处境**：这张牌落在你当前问题上，通常表示——{up}。
它不是预言，而是提醒你此刻已具备／需要调动这个能量。

## 逆位剧情
**图像象征**：（一句话，牌面颠倒后的核心意象）

**对应处境**：逆位不是「坏」，而是能量的卡点或方向偏差——{rev}。
提醒你注意哪里被堵住、哪里在过度或不足。

## 能量提醒
> 此刻你最需要的一句话：……

## 最小行动（明天就能做）
- 一个微小、具体、不费力的动作（如「给一个人发一条消息」「把桌面清一遍」）。

---
🫧 卜卜岛 PONYO · 剧场岛镜｜模拟抽牌，非实体牌
"""

for ident, name, elem, up, rev, arcana in cards:
    path = os.path.join(OUT, f"08_theatre_{ident}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(code=ident.split("_")[0], name=name,
                                elem=elem, up=up, rev=rev, arcana=arcana))

print("generated:", len(cards))
print("dir:", OUT)
