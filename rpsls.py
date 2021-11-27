'''
作者：莫骏逸 目标：通过自定义函数，实现RPSLS游戏
'''

import random


def winer(player_choice_number, comp_number):
    pass
    a = (player_choice_number - comp_number) % 5#使用不同输入结果，导致a的绝对值不同来判断胜负
    if (a == 1) or (a == 2):
        print('您赢了')
    elif (a == 3) or (a == 4):
        print('计算机赢了')
    else:
        print('您和计算机出的一样呢')             #定义出玩家获胜条件


def name_to_number(choice_name):
    if choice_name == '石头':
        return 0
    if choice_name == '史波克':
        return 1
    if choice_name == '纸':
        return 2
    if choice_name == '蜥蜴':
        return 3
    if choice_name == '剪刀':
        return 4
#将玩家输入的汉字转换为易计算的数字


def number_to_name(comp_number):
    if comp_number == 0:
        return '石头'
    if comp_number == 1:
        return '史波克'
    if comp_number == 2:
        return '纸'
    if comp_number == 3:
        return '蜥蜴'
    if comp_number == 4:
        return '剪刀'
#将电脑得到的随机数字转换为汉字


def rpsls(a):
    player_choice_number = name_to_number(choice_name)
    comp_number = random.randint(0, 4)
    computerStr = number_to_name(comp_number)
    print('电脑:', computerStr)
    a = winer(player_choice_number, comp_number)
#将输入的汉字通过name_to_number(choice_name)转换为数字后通过winer(player_choice_number, comp_number)与电脑得出的随机数字进行计算
#并将电脑的随机数字通过number_to_name(comp_number)转换为汉字方便玩家了解电脑的选择结果


print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name = input()                # 对程序进行测试
if choice_name != '石头' or choice_name != '史波克' or choice_name != '纸' or choice_name != '蜥蜴' or choice_name != '剪刀':
        print('Error: No Correct Name')
rpsls(choice_name)
#如果输入汉字不是石头，史波克，纸，蜥蜴，剪刀的任意一个，则报'Error: No Correct Name'
