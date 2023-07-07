from DrawWindow import DWindow

w = DWindow()       # window 클래스 객체 생성

w.WinSize(2, 3)     # window 사이즈 조절
w.WinFlame(" ")     # window 구성 문자 변경
w.WinDraw()         # window 출력
w.WinPrint()        # 현재 window 상태 출력