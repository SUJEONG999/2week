f = open("live_ansi.txt", "wt")  # encoding을 안주었더니 자동으로 cp949(기본값) 해줌. (window 운영체제 때문)
print(f, type(f))  # 파이썬에서 파일 열면 한글 깨져서 나옴..
f.write("""삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니""")
f.close()