#ادخال النقاط 
point=int (input("Enter point :"))
#فحص النقاط وتنفيذ الامر  
if point <50:
    point+=10
elif point<=80:
    point+=5
else:
    point+=2   
    #تحديد الحالة 
if point >=100:
    statu="Winner"
    
elif point >50:
 statu="On his way to win"
else:
    status = "Loser"
#طباعة النتيجة 
print ("Point:",point )    
print ("Player status:", statu ) 