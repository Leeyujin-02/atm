# balance : 통장에 들어있는 기본 금액을 담는 변수
# 1.입금 2.출금 3.영수증 보기 4.종료 

balance = 3000

while True:
    num = input("사용하실 기능의 번호를 입력해 주세요. (1.입금, 2.출금, 3.영수증 보기, 4.종료)")

    if num == "1":
        print("입금기능입니다.")

    if num == "2":
        pass
    
    if num == "3":
        pass
    
    if num =="4":
        print("서비스를 종료합니다")
        break # 종료하는 명령