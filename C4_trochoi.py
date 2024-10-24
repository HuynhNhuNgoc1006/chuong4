# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 23:24:16 2024

@author: Huỳnh Như Ngọc
"""

#Viết chương trình mô phỏng trò chơi Kéo - Búa - Bao giữa người
#và máy

import random

def get_computer_choice():
    choices=['keo','bua','bao']
    return random.choice(choices)

def get_uesr_choice():
    user_input=input("nhap 'keo','bua','bao':")
    while user_input not in ['keo','bua','bao']:
        print("lua chon khong hop le")
        user_input=input("nhap 'keo','bua','bao':")
    return user_input

def determine_winer(user_choice, computer_choice):
    if user_choice==computer_choice:
        return"hoa"
    elif(user_choice=='keo'and computer_choice=='bao') or \
        (user_choice=='bua'and computer_choice=='keo') or \
        (user_choice=='bao'and computer_choice=='bua'):
        return"bn thang!"
    else:
        return"may thang!"
        
def play_game():
    print("chao mung den voi tro choi keo-bua-bao!")
    user_choice=get_uesr_choice()
    computer_choice=get_computer_choice()
    print(f"ban chon: {user_choice}")
    print(f"may chon: {computer_choice}")
    result = determine_winer(user_choice, computer_choice)
    print(result)    
    
if __name__=="__main__":
   play_game()              
