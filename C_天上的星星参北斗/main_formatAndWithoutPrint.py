import os
import re
import jieba
import numpy as np
import networkx as nx
from snownlp import SnowNLP
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter, defaultdict


# -------------------------- 1. 文本预处理与章节分割 --------------------------
def load_and_split_chapters(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'<!\[CDATA\[|\]\]>', '', content)
    content = re.sub(r'\s+', ' ', content)
    chapter_pattern = re.compile(r'(第[一二三四五六七八九十百]+回.*?)(?=第[一二三四五六七八九十百]+回|$)', re.DOTALL)
    chapters = chapter_pattern.findall(content)
    chapter_list = []
    for chap in chapters:
        title_match = re.match(r'第[一二三四五六七八九十百]+回(.*?)[。！？；]?\s', chap)
        title = title_match.group(1).strip() if title_match else f"第{len(chapter_list)+1}回"
        content = chap[title_match.end():].strip() if title_match else chap.strip()
        if content and len(content) > 50:
            chapter_list.append({'title': title, 'content': content})
    return chapter_list


# -------------------------- 2. 分词与词频统计 --------------------------
def load_stopwords():
    return {
        '的', '了', '是', '在', '和', '与', '及', '等', '有', '无', '不', '没', '也', '又',
        '还', '就', '便', '只', '却', '要', '想', '能', '会', '可', '应', '着', '过', '道',
        '说', '说道', '问', '答', '曰', '云'
    }


def split_word_and_count(chapter_list, stopwords):
    all_words = []
    for chap in chapter_list:
        content = chap['content']
        content = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9\s]', ' ', content)
        words = jieba.lcut(content, cut_all=False)
        words += jieba.lcut_for_search(content)
        filtered_words = [
            word for word in words if word not in stopwords and len(word) >= 2
            and not (word.isdigit() or re.match(r'^[一二三四五六七八九十百千万亿]+$', word))
        ]
        all_words.extend(filtered_words)

    word_freq = Counter(all_words)
    meaningful_freq = {word: freq for word, freq in word_freq.items() if freq >= 2}
    if len(meaningful_freq) < 30:
        meaningful_freq = {word: freq for word, freq in word_freq.items() if freq >= 1}

    return meaningful_freq, all_words


# -------------------------- 3. 词云图生成 --------------------------
def get_windows_default_font():
    font_paths = [r'C:\Windows\Fonts\msyh.ttc', r"/System/Library/Fonts/STHeiti Medium.ttc"]
    for font_path in font_paths:
        if os.path.exists(font_path):
            return font_path
    return None


def generate_wordcloud(word_freq, output_path='shuihu_wordcloud.png'):
    if not word_freq:
        return
    word_text = ''
    for word, freq in word_freq.items():
        repeat = min(freq, 60)
        word_text += (word + ' ') * repeat
    if len(word_text) < 1000:
        word_text = word_text * 2

    font_path = get_windows_default_font()

    wc = WordCloud(font_path=font_path, width=1200, height=800, background_color='white',
                   max_words=300, min_font_size=8, max_font_size=100, random_state=42, collocations=False,
                   relative_scaling=0.9, font_step=1, prefer_horizontal=0.7, margin=10)

    try:
        wc.generate(word_text)
        plt.figure(figsize=(14, 10))
        plt.imshow(wc, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white', edgecolor='none')
        plt.close()
    except Exception as e:
        try:
            wc.to_file(output_path)
        except:
            pass


# -------------------------- 4. 章节情感走向分析 --------------------------
def get_emotion_dict():
    return {
        "喜": ["喜", "笑", "欢", "喜悦", "高兴", "乐", "快活", "自在", "爽", "乐呵", "欣喜", "欢喜", "欣慰"],
        "怒": ["怒", "恨", "骂", "愤", "火", "恼", "嗔", "怨", "忿怒", "大怒", "怒骂", "怒气"],
        "哀": ["哭", "悲", "哀", "伤心", "忧", "愁", "惨", "怜", "悲痛", "哀伤", "忧愁", "苦恼"],
        "乐": ["乐", "快活", "自在", "爽", "乐呵", "愉悦", "安乐", "欢乐", "乐趣", "享乐"]
    }


def analyze_chapter_emotion(chapter_list):
    emotion_dict = get_emotion_dict()
    emotion_results = []
    for idx, chap in enumerate(chapter_list, 1):
        content = chap['content'].strip()
        emotion_score = {"喜": 0, "怒": 0, "哀": 0, "乐": 0}
        for emo, words in emotion_dict.items():
            for word in words:
                emotion_score[emo] += content.count(word)
        emotion_results.append({
            'chapter': idx,
            'title': chap['title'],
            'emotion_score': emotion_score,
            'main_emotion': max(emotion_score, key=emotion_score.get)
        })
    return emotion_results


def plot_emotion_trend(emotion_results, output_path='emotion_trend.png'):
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'SimSun']
    plt.rcParams['axes.unicode_minus'] = False

    chapters = [res['chapter'] for res in emotion_results]

    joy_scores = [res['emotion_score']['喜'] for res in emotion_results]
    anger_scores = [res['emotion_score']['怒'] for res in emotion_results]
    sorrow_scores = [res['emotion_score']['哀'] for res in emotion_results]
    pleasure_scores = [res['emotion_score']['乐'] for res in emotion_results]

    plt.figure(figsize=(15, 6))

    plt.plot(chapters, joy_scores, marker='o', linewidth=2, markersize=4, color='#2ca02c', label='喜', alpha=0.8)
    plt.plot(chapters, anger_scores, marker='s', linewidth=2, markersize=4, color='#d62728', label='怒', alpha=0.8)
    plt.plot(chapters, sorrow_scores, marker='^', linewidth=2, markersize=4, color='#9467bd', label='哀', alpha=0.8)
    plt.plot(chapters, pleasure_scores, marker='d', linewidth=2, markersize=4, color='#ff7f0e', label='乐', alpha=0.8)

    plt.xlabel('章节', fontsize=12)
    plt.ylabel('情感关键词出现次数', fontsize=12)
    plt.title('《水浒传》各章节喜怒哀乐情感趋势分析', fontsize=16, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(loc='upper right', fontsize=10)
    step = max(1, len(chapters) // 12)
    plt.xticks(chapters[::step])
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')


# -------------------------- 5. 人物关系图 --------------------------
def build_person_alias():
    return {
        '鲁达': '鲁智深', '花和尚': '鲁智深', '林冲': '林冲', '豹子头': '林冲', '林教头': '林冲',
        '晁盖': '晁盖', '晁保正': '晁盖', '托塔天王': '晁盖', '吴用': '吴用', '智多星': '吴用',
        '吴学究': '吴用', '公孙胜': '公孙胜', '入云龙': '公孙胜', '刘唐': '刘唐', '赤发鬼': '刘唐',
        '阮小二': '阮小二', '立地太岁': '阮小二', '阮小五': '阮小五', '短命二郎': '阮小五', '阮小七': '阮小七',
        '活阎罗': '阮小七', '杨志': '杨志', '青面兽': '杨志', '杨制使': '杨志', '宋江': '宋江', '及时雨': '宋江',
        '宋押司': '宋江', '黑宋江': '宋江', '孝义黑三郎': '宋江', '武松': '武松', '武二郎': '武松',
        '行者': '武松', '李逵': '李逵', '黑旋风': '李逵', '铁牛': '李逵', '卢俊义': '卢俊义',
        '玉麒麟': '卢俊义', '燕青': '燕青', '浪子': '燕青', '关胜': '关胜', '大刀': '关胜', '秦明': '秦明',
        '霹雳火': '秦明', '呼延灼': '呼延灼', '双鞭': '呼延灼', '花荣': '花荣', '小李广': '花荣',
        '柴进': '柴进', '小旋风': '柴进', '朱仝': '朱仝', '美髯公': '朱仝', '雷横': '雷横','插翅虎': '雷横',
        '白胜': '白胜', '白日鼠': '白胜', '王伦': '王伦', '白衣秀士': '王伦', '郑屠': '郑屠', '镇关西': '郑屠',
        '高衙内': '高衙内', '高俅': '高俅', '高太尉': '高俅', '梁中书': '梁中书'
    }


def extract_persons_from_text(text, person_alias):
    persons = set()
    sorted_aliases = sorted(person_alias.items(), key=lambda x: len(x[0]), reverse=True)
    for alias, real_name in sorted_aliases:
        if alias in text:
            persons.add(real_name)
    return list(persons)


def build_person_cooccurrence(chapter_list, person_alias):
    cooccur = defaultdict(int)
    person_count = defaultdict(int)

    for chap in chapter_list:
        content = chap['content']
        paragraphs = [p.strip() for p in content.split('。') if p.strip() and len(p) > 100]
        for para in paragraphs:
            persons = extract_persons_from_text(para, person_alias)
            if len(persons) >= 2:
                from itertools import combinations
                for p1, p2 in combinations(sorted(persons), 2):
                    cooccur[(p1, p2)] += 1
            for p in persons:
                person_count[p] += 1
    return cooccur, person_count


def plot_person_relation(cooccur, person_count, output_path='person_relation.png'):
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'SimSun']
    plt.rcParams['axes.unicode_minus'] = False
    core_persons = {p for p, cnt in person_count.items() if cnt >= 10}
    core_cooccur = {
        (p1, p2): cnt
        for (p1, p2), cnt in cooccur.items()
        if cnt >= 4 and p1 in core_persons and p2 in core_persons
    }
    if len(core_persons) < 5:
        core_persons = {p for p, cnt in person_count.items() if cnt >= 6}
        core_cooccur = {
            (p1, p2): cnt
            for (p1, p2), cnt in cooccur.items()
            if cnt >= 3 and p1 in core_persons and p2 in core_persons
        }
    
    G = nx.Graph()
    for p in core_persons:
        size = min(person_count[p] * 100, 10000)
        G.add_node(p, size=size)
    for (p1, p2), weight in core_cooccur.items():
        G.add_edge(p1, p2, weight=weight)
    plt.figure(figsize=(20, 14))

    try:
        pos = nx.kamada_kawai_layout(G, weight='weight', scale=8)
    except:
        pos = nx.spring_layout(G, k=6, iterations=200, seed=42, scale=6)
    node_sizes = [G.nodes[p]['size'] for p in G.nodes]
    nx.draw_networkx_nodes(
        G, pos, node_size=node_sizes, node_color='#ecad36', alpha=0.9,
        edgecolors='#1f77b4', linewidths=2.0
    )

    edges = G.edges(data=True)
    edge_weights = [d['weight'] for (u, v, d) in edges]
    edge_widths = [min(w * 1.2, 6) for w in edge_weights]
    nx.draw_networkx_edges(G, pos, width=edge_widths, alpha=0.6, edge_color='#7f7f7f', style='solid')
    nx.draw_networkx_labels(G, pos, font_size=18, font_weight='bold', font_color='black')
    edge_labels = {(u, v): d['weight'] for (u, v, d) in edges if d['weight'] >= 5}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, label_pos=0.3,
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.9)
    )
    
    plt.title('《水浒传》核心人物关系图（节点大小=出现次数，边宽度=共现次数）',
              fontsize=18, fontweight='bold', pad=20)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight', pad_inches=1.0)


# -------------------------- 主函数 --------------------------
def main(file_path='水浒传.txt'):
    chapter_list = load_and_split_chapters(file_path)
    stopwords = load_stopwords()
    meaningful_freq, all_words = split_word_and_count(chapter_list, stopwords)
    generate_wordcloud(meaningful_freq)
    emotion_results = analyze_chapter_emotion(chapter_list)
    plot_emotion_trend(emotion_results)
    person_alias = build_person_alias()
    cooccur, person_count = build_person_cooccurrence(chapter_list, person_alias)
    plot_person_relation(cooccur, person_count)


if __name__ == "__main__":
    main(file_path='./水浒传.txt')
