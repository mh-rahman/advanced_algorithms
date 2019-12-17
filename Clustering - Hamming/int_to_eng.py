
num = 10

map1 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
map2 = ["","Onety", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
map3 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

eng = ""

if num//100 != 0:
    eng = eng + map1[num//100] + " Hundred" + " "
num = num%100
if num//10 != 1:
    eng = eng + map2[num//10]
    num = num%10
    eng = eng + map1[num]
else:
    eng = eng+" "+map3[num%10]

print(eng)