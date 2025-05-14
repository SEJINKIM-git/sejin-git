import random

def generate_number():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

def get_strike_ball(user_input, answer):
    strike = 0
    ball = 0
    for i in range(3):
        if user_input[i] == answer[i]:
            strike += 1
        elif user_input[i] in answer:
            ball += 1
    return strike, ball

def play_baseball():
    answer = generate_number()
    attempts = 0
    print("⚾ 숫자 야구 게임을 시작합니다!")
    print("0~9 사이의 서로 다른 숫자 3개를 맞춰보세요.")

    while True:
        user_input = input("숫자 3자리를 입력하세요 (예: 123): ")

        if not user_input.isdigit() or len(user_input) != 3:
            print("❗ 세 자리 숫자를 입력해주세요.")
            continue

        user_numbers = [int(n) for n in user_input]

        if len(set(user_numbers)) != 3:
            print("❗ 중복되지 않은 숫자를 입력해주세요.")
            continue

        attempts += 1
        strike, ball = get_strike_ball(user_numbers, answer)
        print(f"{strike} 스트라이크, {ball} 볼")

        if strike == 3:
            print(f"🎉 정답입니다! {attempts}번 만에 맞추셨어요.")
            break

# 게임 실행
play_baseball()


