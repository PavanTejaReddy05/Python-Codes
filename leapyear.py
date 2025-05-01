yr=int(input())
Divi_by_4=((yr//4)*4)==yr
Divi_by_100=((yr//100)*100)==yr
Divi_by_400=((yr//400)*400)==yr
if Divi_by_4:
    if Divi_by_100:
        is_leap=Divi_by_400
    else:
        is_leap=True
else:
    is_leap=False
print(f"Given Year: {yr} is a {is_leap}")