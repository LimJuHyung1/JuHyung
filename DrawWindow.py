class DWindow:

    def __init__(self):
        self.__wid = 1
        self.__hei = 1
        self.__flame = "*"

    # window 그리기
    def WinDraw(self):
        for a in range(self.__hei * 2 + 1):    # 3, 5, 7, ... -> 행의 길이 설정
            print(self.__flame, end='')

            for b in range(self.__wid):        # 현재 행에 따라 다른 문자 출력
                if a % 2 == 0:
                    print(self.__flame * 2, end='')
                else:
                    print(" " + self.__flame, end='')
            print()

        print('-' * (self.__wid * 2 + 1))  # 구분 라인 생성

    # window 크기 설정
    def WinSize(self, weight: int, height: int):
        self.__wid = weight
        self.__hei = height

    # window 구성 문자 설정
    def WinFlame(self, Flame: str):
        # 공백으로 시작할 경우 에러 메세지 출력
        if Flame.startswith(' ') == True:
            print("\n잘못된 문자입니다.\n")
        else:
            self.__flame = Flame[0:1]

    # window 상태 출력
    def WinPrint(self):
        print("현재 window 는 {} 문자로 이루어진\n{} * {} 크기의 window 입니다"
              .format(self.__flame, self.__wid, self.__hei))



