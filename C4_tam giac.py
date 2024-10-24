# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:36:22 2024

@author: Huỳnh Như Ngọc
"""

#Nhập vào 3 số a, b, c. Sau đó, kiểm tra xem a, b, c có phải là 3 
#cạnh của tam giác.
# Biết a, b, c là 3 cạnh tam gác. Kiểm tra xem là tam giá gì 
#(vuông, cân, đều, thường…)?


a=int(input("nhap canh a:"))
b=int(input("nhap canh :"))
c=int(input("nhap canh c:"))
if a>0 and b>0 and c>0:
    if a+b>c and a+c>b and b+c>a:
        print("la tam giac")
        if a==b==c:
            print("deu")
        elif a==b or a==c or b==c:
            print("can")
        elif a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
            print("vuong")
        else:
            print("thuong")
    else:
        print("ko phai tam giac ")
else:
 print("vui long nhap lai")        
            
                
    