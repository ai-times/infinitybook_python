import webbrowser

text = input("문장 입력 : ")
url = "https://translate.google.co.kr/#ko/en/" + text 
webbrowser.open( url )

url = "https://translate.google.co.kr/#ko/ja/" + text 
webbrowser.open_new( url )

url = "https://translate.google.co.kr/#ko/zh-CN/" + text 
webbrowser.open_new( url )

