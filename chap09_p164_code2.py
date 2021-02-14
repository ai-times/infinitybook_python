print("한국시간을 입력하세요.")
korHour = int(input("시간 : "))
korMin = int(input("분 : "))

vieHour = korHour - 2
vieMin = korMin
if vieHour < 0 :
    vieHour += 24 

print("\n계산 결과")
print("한국 : {0:d}시 {1:d}분".format(korHour, korMin) )
print("베트남 : {0:d}시 {1:d}분".format(vieHour, vieMin) )
