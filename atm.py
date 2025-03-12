# balance : 통장에 들어있는 기본 금액을 담는 변수
# 1.입금 2.출금 3.영수증 보기 4.종료
# deposit_amount > 예금금액이라는 변수명

balance = 3000

while True:
    num = input("사용하실 기능의 번호를 입력해 주세요. (1.입금, 2.출금, 3.영수증 보기, 4.종료)")

    if num == "1":
        deposit_amount = input("입금할 금액을 입력해주세요 : ")
        if deposit_amount.isdigit() and int(deposit_amount) > 0:
            # 문자가 들어가 있진 않은지 확인 / 0 보다 큰지 확인
            balance += int(deposit_amount)
            print(f"고객님이 입금하신 금액은 {deposit_amount}원 이며, 현재 잔액은 {balance}입니다.")
        else:
            print("정신차리고, 제대로된 숫자형태로 입금액을 작성해줘!!!")
    if num == "2":
        pass
    
    if num == "3":
        pass
    
    if num =="4":
        print("서비스를 종료합니다")
        break # 종료하는 명령