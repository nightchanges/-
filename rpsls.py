#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�ֲ��9������
���ڣ�6/1/2021
������ ����һ����
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(choice_name):
	if choice_name == "ʯͷ":
		return 0
	elif choice_name == "ʷ����":
		return 1
	elif choice_name == "ֽ":
		return 2
	elif choice_name == "����":
		name_to_number(choice_name)==3
		return 3
	elif choice_name == "����":
		name_to_number(choice_name)==4
		return 4
	else:
		return 'Error: No Correct Name'
def number_to_name(comp_number):
	if comp_number == 0:
		return "ʯͷ"
	elif comp_number == 1:
		return "ʷ����"
	elif comp_number == 2:
		return "ֽ"
	elif comp_number == 3:
		return "����"
	elif comp_number == 4:
		return "����"
	else:
		print('wrong')
def rpsls(player_choice_number,comp_number):
	if player_choice_number==0:
		if comp_number==3 or 4:
			print('��Ӯ��')
		elif comp_number==player_choice_number:
			print('ѡ����ͬ')
		else:
			print('�����Ӯ��')
	elif player_choice_number==1:
		if comp_number==0 or 4:
			print('��Ӯ��')
		elif comp_number==player_choice_number:
			return 'ѡ����ͬ'
		else:
			return '�����Ӯ��'
	elif player_choice_number==2:
		if comp_number==0 or 1:
			print('��Ӯ��')
		elif comp_number==player_choice_number:
			return 'ѡ����ͬ'
		else:
			return '�����Ӯ��'
	elif player_choice_number==3:
		if comp_number==1 or 2:
			return '��Ӯ��'
		elif comp_number==player_choice_number:
			return 'ѡ����ͬ'
		else:
			return '�����Ӯ��'
	elif player_choice_number==4:
		if comp_number==3 or 2:
			print('��Ӯ��')
		elif comp_number==player_choice_number:
			return 'ѡ����ͬ'
		else:
			return '�����Ӯ��'
	else:
		print('wrong')


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=str(input())
print('����ѡ��Ϊ',choice_name)
player_choice_number=name_to_number(choice_name)
comp_number=random.randrange(0,5)
print('�������ѡ��Ϊ',number_to_name(comp_number))
rpsls(player_choice_number,comp_number)

