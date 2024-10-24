# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:13:42 2024

@author: Huỳnh Như Ngọc
"""

#Nhập vào ngày tháng năm theo định dạng dd/mm/yyyy hoặc ddmm-yyyy. Sau đó, kiểm tra tính hợp lệ của ngày tháng năm nhập
#vào

thang=int(input("nhap thang:"))
nam=int(input("nhap nam:"))
if thang==1 or thang==3 or thang==5 or thang==7 or thang==8 or thang==10 or thang==11 or thang==12:
    print("thang co 31 ngay")
elif thang==4 or thang==6 or thang==9 or thang==11:
    print("thang co 30 ngay")
else:
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 !=0):
        print("thang co 29 ngay")
    else:
        print("thang co 28 ngay")