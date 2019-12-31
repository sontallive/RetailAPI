from collections import OrderedDict

'''
all super cats and their children cats
need to be completed first to use all other functions
use the  get_all_lost.py to find the lost cats, and complete it
'''
retail_products = OrderedDict({
    'cigar': [
        '555_A', '555_a',
        # B
        '白沙_A', '白沙_a', 
        # D
        '大重九_a','大重九_A', 
        '钓鱼台_a', 
        '大前门_A',
        # F
        '芙蓉王_A', '芙蓉王_a','芙蓉王_b','芙蓉王_B',
        # G
        '贵烟_a', '贵烟_A','贵烟_b','贵烟_B','贵烟_c',
        '古田_A', 
        # H
        '黄鹤楼_A', '黄鹤楼_a', '黄鹤楼_B', '黄鹤楼_b', '黄鹤楼_C', '黄鹤楼_c', '黄鹤楼_D', '黄鹤楼_d',
        '黄鹤楼_E','黄鹤楼_e','黄鹤楼_F','黄鹤楼_f','黄鹤楼_g', '黄鹤楼_h', '黄鹤楼_i','黄鹤楼_j',
        '哈德门_A', '哈德门_a',
        '黄山_A', '黄山_a', '黄山_B','黄山_C','黄山_D',
        '黄果树_a','黄果树_A',
        '黄金叶_a','黄金叶_B','黄金叶_c','黄金叶_C',
        '和天下_A', '和天下_a', '和天下_B', '和天下_b',
        '荷花_A', '荷花_a',
        '红河_a','红河_A',
        '红塔山_A', '红塔山_a','红塔山_B','红塔山_b',
        '红方印_b',
        # J
        '娇子_A', '娇子_a', '娇子_B', '娇子_b', '娇子_C', '娇子_c', '娇子_D', '娇子_d',
        '娇子_E', '娇子_e', '娇子_F', '娇子_f', '娇子_G', '娇子_g', '娇子_H', '娇子_h',
        '娇子_I', '娇子_i', '娇子_J', '娇子_j', '娇子_K', '娇子_k', '娇子_L','娇子_m',
        '金桥_a',
        # K
        '宽窄_A', '宽窄_a','宽窄_B','宽窄_C','宽窄_d','宽窄_E','宽窄_F','宽窄_f',
        # L
        '利群_A', '利群_a', '利群_B', '利群_b','利群_C',
        '兰州_a','兰州_A','兰州_B',
        # M
        'Mevius_A',
        # N
        '南京_A', '南京_a', '南京_B', '南京_b',
        '牡丹_a',
        # Q
        '七匹狼_a','七匹狼_b',
        # S
        '双喜_a','双喜_A','双喜_B','双喜_C',
        '狮牌_a',
        # T
        '土楼_a',
        '天下秀_A', '天下秀_a', '天下秀_B', '天下秀_b',
        '天子_A', '天子_a','天子_b','天子_B','天子_c', '天子_C','天子_d','天子_E','天子_F',
        # W
        '王冠_A','王冠_a',
        # Y
        '玉溪_A', '玉溪_a', '玉溪_b','玉溪_B','玉溪_c', '玉溪_d','玉溪_e','玉溪_f','玉溪_g','玉溪_h',
        '云烟_A', '云烟_a', '云烟_B', '云烟_b', '云烟_C', '云烟_c','云烟_D','云烟_e','云烟_d','云烟_f','云烟_g',
        '原香_A', '原香_a',
        # Z
        '真龙_A', '真龙_a','真龙_b','真龙_c',
        '中华_A', '中华_a','中华_B','中华_b','中华_c','中华_C',
        '中南海_A', '中南海_a', '中南海_B','中南海_c','中南海_C','中南海_D',
        '招财猫_a',
    ],
    'drink': [
        '元气水', 'MR.SODA', '脉动', '名仁_6个柠檬',
        '乐虎_瓶', '果粒橙', '果粒橙_大',
        '百岁山', '怡宝', '怡宝_大瓶', '农夫山泉', '农夫山泉_大瓶',
        '康师傅红茶_大', '茉莉蜜茶', '冰糖雪梨',
        '米婆婆米酒_瓶', '芬达',
        '可口可乐', '百事可乐', '雪碧', '尖叫',
        '康师傅绿茶', '椰树牌椰汁_瓶',
        '燃茶', '阿萨姆奶茶', '8度', 'AOO2',
        '东方树叶', '乌梅汽水', '星巴克咖啡',
        '雪碧_蓝色',
        '尖叫_蓝色',
        '罐装红牛', '罐装百事可乐',
        '娃哈哈AD钙', 'SODA_紫色',
        '水蜜桃', '康师傅水晶葡萄',
        '茶π', '康师傅奶茶', '乐虎维生素功能饮料',
        '康师傅冰红茶','茉莉花茶','水溶C100',
        '石榴果茶', '真果粒_褐', '爱夸矿泉水','汽泡苏打','午后奶茶','益消_绿瓶',
        '可口可乐_大','沁柠水','AD钙奶','柠檬味果茶','星巴克_红',
        '营养快线', '汽泡苏打_绿', '小茗同学冷泡茶_黄',
        '暖香蜜柚','元气森林无糖气泡水','中原G7三合一速溶咖啡_盒装','汽泡苏打_粉', 
        '佳得乐橙味运动饮料','小茗同学冷泡茶_黄','香飘飘', '永和豆浆','屈臣氏_苏打水',
        '三只松鼠_巴旦木','中原G7三合一速溶咖啡_包装','白兔奶茶研究室',
        '雀巢咖啡_小瓶', '康师傅蜂蜜柚子','康师傅冰红茶_1L', '乌龙茶',
        '沁桃水', 'CAFFE_LATTE','三得利_蜜香暖柚','三得利_三得利蜜香暖苹',
        '统一鲜橙多','三得利_蜜香暖姜','贝纳颂咖啡','统一绿茶','康师傅炼乳奶茶',
        '雀巢咖啡_大盒', '可口可乐_零度','雪碧_大', 'meco牛乳茶', '可口可乐_罐装',
        '昆仑山矿泉水','鲜橙多_大桶','芬达_小','康师傅绿茶_1L','欢乐家_生榨椰子汁','美汁源_果粒奶优',
        '大红袍', '统一绿茶_1L', '统一_冰糖雪梨_1L', '优乐美奶茶','康师傅矿泉水', '美汁源', '可口可乐_小',
        '百事可乐_大','真果粒_箱','咖啡拿铁','健力宝','三得利_蜜香暖橙','统一冰红茶',
    ],
    'alcohol': [
        '雪花勇闯天涯_高罐',
        '条顿啤酒', '雪花啤酒_瓶装',
        '玛翁赤霞珠红葡萄酒', '啤酒', '锐澳鸡尾酒',
        '百威啤酒_白罐', '百威啤酒_红罐',
        '青岛啤酒', '福佳白啤酒', '绵竹大曲',
        '五粮液', '宝龙梅子酒', '青岛纯生啤酒',
        '五粮液敬四方','乌苏啤酒_罐','哈尔滨啤酒',
        '长城干红葡萄酒','小郎酒','五粮春','泸州老窖',
    ],
    'snack': [
        '奥利奥',
        '面包', '面包_片装', '面包_全麦', '铜锣烧',
        '热狗', '火腿肠',
        '亲嘴烧',
        '口水族爱吃鱿鱼',
        '大棒糖', 'BIG_ROLL', '绿箭口香糖',
        '老冰棍', '上好佳_芝士味', '爆米花',
        '乐事_蓝包',
        '旺旺小小酥', '法丽兹曲奇',
        '旺旺碎冰冰', '妙脆角', '重庆怪味胡豆',
        '蓝莓糖', '花生米', '马记锅巴',
        '原味青豌豆', '良品铺子鱼豆腐',
        '上好佳鲜虾条', '好丽友蛋黄派',
        '瓶装小饼干', '上好佳洋葱卷_绿色',
        '母亲牛肉棒_原味', '老程华五香胡豆',
        '趣多多', '真巧酱芯蛋卷', '威化饼干',
        '黑花生', '凤爪', '浪味仙', '巧克力',
        '饼干_芭米', '奶糖_袋装', '起酥面包', '瓜子',
        '好吃点', '益达口香糖_盒装',
        '停不下嘴', '辣条', '葡萄干面包', '熊字饼',
        '醇熟面包', '好多鱼', '绿箭薄荷糖', '芝麻味梳打饼干',
        '太平饼干_海苔味', '小老板海苔卷', '奥利奥巧脆卷',
        '合味道_海鲜风味', '五香味牛肉粒', '公仔碗仔面_海鲜味', '健达奇趣蛋', '山药薄片',
        '欧扎克酸奶果粒坚果麦片','焙软切片面包','猪肉脯','m豆', '威化小方块_咸蛋黄味',
        '士力架','汉堡橡皮糖', '太平饼干_白','不二家袋装糖果_蓝','乐事_红包', '嘉士利威化饼干',
        '碗仔面_红烧牛肉味','芭米_软奶牛轧饼','旺旺仙贝', '太平饼干_黄', '爱豆的面包',
        '食族人酸辣粉','鸡蛋香松包', '豆沙面包','唐记锅巴','口水族爱吃鱿鱼_绿',
        '黄桃干','阿尔卑斯_粉','阿尔卑斯_橙','抹茶风味麻薯','洽洽香瓜子',
        '康师傅藤椒牛肉面','益达口香糖_瓶装', '棉花棒棒糖',
        '旺旺雪饼', '小猪佩奇厚片海苔', '不二家水果棒棒糖_红', 
        '农心石锅牛肉拉面', '不二家牛奶仔饼干','奥赛山楂','溜溜梅_绿',
        '康辉雪梅', '康辉杨梅','乐事_黄包','香香嘴串烧','香香嘴手工豆干',
        '天马达利雪梅','可比克薯片', '臻芯挞','脆美司蔬菜味棒饼干',
        '老程华_香辣蚕豆', '牛乳味大饼干','亲嘴豆皮', '法式牛油曲奇',
        '小猪佩奇草莓味注心饼干','鸡蛋丸子拉面糖果','真巧酱芯曲奇',
        '良品铺子牛板筋', '鲜引力_芒果果干','魔芋爽_香辣素毛肚','有友竹笋',
        '奇多玉米棒','妙可蓝多奶酪棒混合水果味', '徽记生瓜子','德芙_袋装', 
        '上好佳鲜虾片_大包', '果丹皮', '上好佳咸蛋黄味薯片', '上好佳薯条_绿',
        '佩奇棒棒饼干','上好佳_薄荷味硬糖','大白兔奶糖','良品铺子_裙带菜',
        '牛轧1991_牛轧糖','超级飞侠饼干','力诚火腿肠','怡达好吃山楂', '水煮花生',
        '旺旺大米饼','友臣肉松饼','星球杯','菲律宾香蕉片','百奇_绿','牛轧味大饼干',
        '好巴食_南溪豆干','乐事_绿包','绿箭_脆皮软心薄荷糖','mini蛋卷',
    ],
    'milk': [
        '伊利纯牛奶_箱', '伊利高钙奶_盒',
        '纯甄_盒',
        '安慕希_盒',
        '熟酸奶_白瓶',
        '益消_绿杯',
        '活润_蓝杯', '活润_白瓶', '活润_纸盒',
        '每益添_蓝瓶',
        '优酸乳_绿',
        '畅轻_草莓味',
        '特仑苏_盒',
        '袋装纯牛奶', 
        '旺仔牛奶', 
        '老酸奶', '活菌','菊乐酸奶',
        '金典牛奶_盒','草莓袋装酸奶',
        '伊利高钙低脂奶_盒','蒙牛纯牛奶_盒',
        '啵乐乐乳酸菌','光明_莫斯利安',
        '唯怡_紫标核桃花生奶', '伊利红枣酸奶',
        '银鹭花生牛奶','杨森双岐酸牛奶_袋装','酸乐奶_箱',
        '伊利舒化奶_低脂','畅轻_橙','蒙牛畅轻酸奶', '莫斯利安_箱','安慕希_箱','伊利高钙奶_箱',
        '金典_箱','伊利纯牛奶_盒','蒙牛纯牛奶_箱',
    ],
    'stationery': [
        '甄潮液晶写字板', '铅笔',
    ],
    'daily_supplies': [
        '千唯抽纸_箱', 'CEO_保鲜袋', '黑人牙膏', 
        '洗衣液', '卫生巾_七度空间', '美涛', '充电器', 
        '清扬男士洗发水', '海飞丝','蓝月亮洗衣液',
        '苏菲极薄卫生巾_粉','红玫瑰洗洁精',
        '久大精纯盐', '舒肤佳沐浴露','云南白药牙膏',
        'Oral-B电动牙刷','米客牙刷','维达湿巾','护舒宝',
        '维达抽纸_箱','裸感S','臻雪抽纸_箱', '金纺洗衣液',
        '苏菲_超熟睡420','奥妙', '舒客牙膏',
    ],
    'food': [
        '北大荒大米', '月饼',
        '康师傅泡椒牛肉面_绿', '康师傅红烧牛肉面_红', '康师傅麻辣牛肉面_粉',
        '汤达人海鲜面', '公鸡（GALLO）直条型意面', '好丽友派','太平饼干_蓝',
        '银鹭好粥道','统一老坛酸菜面','砂锅香菇鸡面', '盼盼法式小面包',
        'tipo面包干','巧乐角面包','碗仔面','肥肠味粉','桃李_天然酵_面包',
        '思念灌汤水饺','仙餐菜籽油','麻辣笋子牛肉面','辣白菜拉面','康师傅红烧牛肉面_袋',
        '巧面馆_老坛酸菜牛肉面','大西南_特制一等小麦粉',
    ],
    'plaything': [
        '玩具_动物生球', '玩具_绝地求生', '玩具_机器人', 
        '玩具_糖玩新世界', '玩具_环太平洋','玩具_小花仙',
        '玩具_奥特曼','玩具_趣味小昆虫','玩具_海底小纵队',
        '玩具_特种车', '玩具_HPD_乐高','玩具_巧玩蘑菇头', 
        '玩具_kikilove','玩具_大冒险',
    ],
})


def print_cats_from_str(product_dict):
    """
    :return: split long str to cat sub_str
    """
    for super_cat, cats in product_dict.items():
        print(super_cat)
        cats = cats.split(',')
        for cat in cats:
            print("'%s'" % cat.strip(), end=',')
        print('\n')


def save_cats_to_str(product_dict, file_path):
    """
    :return: cat sub_str ==> long str for DataTurks
    """
    with open(file_path, 'w', encoding='UTF-8') as f:
        long_str = ''
        for _, cats in product_dict.items():
            for cat in cats:
                long_str += cat.strip() + ', '
        f.write(long_str[:-2])  # 去掉最后的 ,


def total_cats(product_dict):
    """
    :return: retail database total cats
    """
    return sum([len(cats) for k, cats in product_dict.items()])


if __name__ == '__main__':
    print(total_cats(retail_products))
    save_cats_to_str(retail_products, file_path='product_cats.txt')
