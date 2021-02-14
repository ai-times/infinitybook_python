letter = "HELLO Python"
encodeLetter ="" 

for ch in letter :
    num = ord(ch)
    encodeLetter += chr(num+1)

print( "원문 : ", letter) 
print( "암호 : ", encodeLetter )

input() 
