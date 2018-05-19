from solve import *

patternList = {
                  ('action', '肌肉'): 0,  # 卧推锻炼哪些肌肉
                  ('action', 'muscle'): 1,  # 俯卧撑除了练腹肌
                  ('action'): 2,  # Q1怎样做俯卧撑 Q2俯卧撑
                  ('练', 'muscle'): 3,  # 怎么样可以锻炼腹肌
                  ('action', '要', '器'): 4,  # 平板支撑需要什么器械/道具/设备/条件 #4

                  ('action', '动作'): 5,  # 跟仰卧起坐差不多的动作有什么
                  ('muscle', '练'): 6,  # 腹肌怎么练
                  ('muscle', '炼'): 7,  # 腹肌怎么锻炼
                  ('action', '炼'): 8,  # 卧推怎么锻炼
                  ('action', '练'): 9,  # 卧推怎么练 #9

                  ('action', '肌肉'):10,  # 卧推锻炼哪些肌肉
                  ('action', 'muscle'):11,  # 俯卧撑除了练腹肌
                  ('action'):12,  # Q1怎样做俯卧撑 Q2俯卧撑
                  ('练', 'muscle'):13,  # 怎么样可以锻炼腹肌
                  ('action', '器'):14,  # 平板支撑需要什么器械/道具/设备/条件 #4

                  ('machine', 'action', 'muscle'): 15,  # 哑铃卧推怎样锻炼到胸中束  #14  5.17号解决以上pattern

                    ('action', '注意'): 16,  # 卧推要有什么特别注意事项
                    ('machine', 'muscle', 'special'): 17,  # 哑铃练肱二头肌有效果吗
                    ('muscle', '拉伸'):18,  # 背阔肌怎样拉伸
                    ('machine', '动作'):19,  # 哑铃主要可以做哪些动作
                    ('machine', 'action', 'muscle'):20,  # 哑铃卧推怎样锻炼到胸中束  #14 5.17号解决以上pattern

                    # （因为这些关键词只要有一个较为完整的回答基本就够了，问的比较频繁）##更新于5.18
                    ('了解', '健身'):21,  # 你好，我想了解一些健身健身方面的知识（返回问候语和一些鼓励的话）#15
                    ('谢谢'):22,  # 对我很有帮助，谢谢啦（返回励志的话）
                    ('炼', '补充水'):23,  # 锻炼怎样补充水
                    ('炼', '补水'):24,  # 锻炼怎样补充水
                    ('炼', '补充能量'):25,  # 锻炼能量怎样补充

                    ('action', '保护'):26,  # 深蹲怎样保护自己   #20
                    ('action', '避免'):27,  # 深度怎么避免受伤
                    ('健身', '保护'):28,  # 健身中怎么保护自己
                    ('健身', '避免'):29,  # 健身中怎么避免受伤

                    ('增肌', '动作'):30,  # 增肌该做些什么动作  # 24
                    ('增肌'):31,  # 增肌该怎么做     #25
                    ('减脂'):32,  # 减脂该怎么做
                    ('减肥'):33,  # 减肥该怎么做
                    ('增重'):34,  # 增重该怎么做
                    ('减重'):35,  # 减重该怎么做

                    ('健身', '休息'):36,  # 健身后如何合理休息  #30
                    ('健身', '注意', '饮食'):37,  # 健身期间如何注意饮食搭配
                    ('健身', '饮食'):38,  # 健身中的饮食搭配 健身后的饮食搭配 健身如何进行饮食搭配
                    ('规划'):39  # 能给我提点简单的训练时间规划吗（主要是不同训练阶段的频次安排，每周几练，时间间隔等）


# ('machine', 'action', 'muscle'),  # 哑铃卧推怎样锻炼到胸中束
# ('machine', 'muscle', 'special'),  # 杠铃怎样练二头有效果
# ('machine', 'action', 'muscle', 'special'),  # 哑铃卧推对二头效果好吗
# ('健身','服饰'),  # 去健身房穿什么运动服饰比较好
# ('健身','礼仪'),  # 健身礼仪是什么
# ('户外', '健身房', 'special'),  # 户外健身和健身房相比效果好吗
#  ('action','防具'),# 深蹲防具该准备哪些
# ('有氧训练'),  # 有氧训练怎样进行
# ('muscle','热身'),# 背阔肌怎样热身
# ('练','水'),# 锻炼怎样补充水
# ('练','能量'),# 锻炼能量怎样补充
# ('极限','action','保护'),# 极限重量深蹲怎样保护避免受伤
# ('服饰'),# 去健身房穿什么运动服饰比较好
# ('machine', 'action', 'special'),  # 哑铃卧推比杠铃卧推效果好吗
# ('machine', 'action', '重量'),  # 杠铃卧推重量该怎么选择
# ('machine', 'action', '重量'),  # 杠铃卧推重量该怎么选择
# ('machine', 'action', 'special'),  # 哑铃卧推比杠铃卧推效果好吗
}

def pattern_match(pattern, sentence):
    # print(pattern)
    # print(sentence)
    # 1 split sentence
    # 2 find out focus word  eg muscle/special/action
    # 3
    if len(pattern) != len(sentence):
        return False
    l = len(sentence)
    # print(l)
    for i in range(l):
        # print(pattern[i])
        # print(sentence[i])
        if pattern[i] == 'action':
            if sentence[i][0] == 'action':
                continue
            return False
        if pattern[i] == 'muscle':
            if sentence[i][0] == 'muscle':
                continue
            return False
        if sentence[i][1] == pattern[i]:
            continue
        return False
    return True


def pattern(sentence):
    for p in patternList:
        # print(index)
        index = patternList[p]

        if pattern_match(p, sentence):
            print(sentence)
            if index == 0:
                return get_muscle_of_action(sentence[0][1])
            if index == 1:
                return get_muscleGroup_action(sentence[1][1])
            if index == 2:
                if sentence[0][2] != 0:
                    return get_details_of_action(sentence[0][1])
                else:
                    return get_describe_of_action(sentence[0][1])
            if index == 3:
                return get_details_of_action(sentence[0][1])
            if index == 4:
                return get_equipment_of_action(sentence[0][1])
            if index == 5:
                return get_muscleGroup_action(sentence[0][1])
            if index == 6 or index == 7:
                return get_muscleGroup_action(sentence[0][1])
            if index == 8 or index == 9 or index == 10:
                return get_details_of_action(sentence[0][1])
            if index == 11:
                return get_muscle_of_equipments(sentence[0][1])
            if index == 12:
                return get_muscleGroup_action(sentence[0][1])
            if index == 13:
                return get_action_of_euqipments(sentence[0][1])
            if index == 14:
                return get_muscleGroup_action(sentence[1][1])
            if index == 15:
                print_welcoming()
            if index == 16:
                print_goodbye()
            if index == 17 or index == 18:
                water_replenishing()
            if index == 19:
                energy_replenishing()
            if index == 20 or index == 21 or index == 22 or index == 23:
                fitness_protection()
            if index == 24 or index == 25:
                musculus_muscle()
            if index == 26 or index == 27 or index == 29:
                lose_weight()
            if index == 28:
                increase_weight()
            if index == 30:
                relax()
            if index == 31 or index == 32:
                energy_replenishing()
            if index == 33:
                fitness_planing()

    return 'unknown'


if __name__ == '__main__':
    # print(pattern([('action', '平板支撑'), ('special', '肌肉')]))
    # print(pattern([('action', '平板支撑'), ('muscle', '腹肌')]))
    print(pattern([('action', '平板支撑', 0)]))
    # print(pattern([('action', '平板支撑'), ('special','有效')]))
    # print(pattern([('special', '可以'), ('muscle', '腹肌')]))
    # print(pattern([('action', '平板支撑'), ('special', '器材')]))
    # print(pattern([('action', '平板支撑'), ('special', '动作')]))#unsovle
    pass
