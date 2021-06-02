#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：植产9班王皓楠
日期：6/1/2021
累死了 搞了一晚上
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(choice_name):
	if choice_name == "石头":
		return 0
	elif choice_name == "史波克":
		return 1
	elif choice_name == "纸":
		return 2
	elif choice_name == "蜥蜴":
		name_to_number(choice_name)==3
		return 3
	elif choice_name == "剪刀":
		name_to_number(choice_name)==4
		return 4
	else:
		return 'Error: No Correct Name'
def number_to_name(comp_number):
	if comp_number == 0:
		return "石头"
	elif comp_number == 1:
		return "史波克"
	elif comp_number == 2:
		return "纸"
	elif comp_number == 3:
		return "蜥蜴"
	elif comp_number == 4:
		return "剪刀"
	else:
		print('wrong')
def rpsls(player_choice_number,comp_number):
	if player_choice_number==0:
		if comp_number==3 or 4:
			print('您赢了')
		elif comp_number==player_choice_number:
			print('选择相同')
		else:
			print('计算机赢了')
	elif player_choice_number==1:
		if comp_number==0 or 4:
			print('您赢了')
		elif comp_number==player_choice_number:
			return '选择相同'
		else:
			return '计算机赢了'
	elif player_choice_number==2:
		if comp_number==0 or 1:
			print('您赢了')
		elif comp_number==player_choice_number:
			return '选择相同'
		else:
			return '计算机赢了'
	elif player_choice_number==3:
		if comp_number==1 or 2:
			return '您赢了'
		elif comp_number==player_choice_number:
			return '选择相同'
		else:
			return '计算机赢了'
	elif player_choice_number==4:
		if comp_number==3 or 2:
			print('您赢了')
		elif comp_number==player_choice_number:
			return '选择相同'
		else:
			return '计算机赢了'
	else:
		print('wrong')


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=str(input())
print('您的选择为',choice_name)
player_choice_number=name_to_number(choice_name)
comp_number=random.randrange(0,5)
print('计算机的选择为',number_to_name(comp_number))
rpsls(player_choice_number,comp_number)

