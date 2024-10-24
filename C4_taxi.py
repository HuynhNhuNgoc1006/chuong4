# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 22:01:12 2024

@author: Huỳnh Như Ngọc
"""

#Tính tiền taxi theo số km quãng đường đi được. Cho biết:
#• 1 km đầu tiên: 20k
#• 3 km đầu tiên: 13k/km
#• Từ km thứ 4 đến km thứ 8: 12k/km
#• Còn lại giá 10k/km
#• Nếu đi hơn 100k thì giảm thêm 8% cho tổng tiền

duong=float(input("nhap quang duong:"))
if duong==1:
    x=20
    print("tien taxi:",x)
elif 1<duong<=3:
    x=duong*13
    print("tien taxi:",x)
elif 4<=duong<=8:
 x=3*13+(duong-3)*12 
 print("tien taxi:",x)
else:
    x=duong*10
    if x>100:
        print("tien taxi:",x)
    else:
        print("tien taxi:",x)
        