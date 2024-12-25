from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv() # .env 파일 로드
OpenAI.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()


# 시스템 프롬프트 정의
SYSTEM_PROMPT = (
    "You are an empathetic and highly skilled planning assistant. "
    "Your main task is to help users by creating detailed and actionable plans based on their goals and deadlines. "
    "Provide clear daily, weekly, and monthly tasks while following the SMART framework. "
    "Please make a specific time plan."
    "Favor agile processes over the waterfall method, ensuring the plans are iterative, flexible, and adaptive to changes. "
    "Show empathy and encouragement in your responses, but ensure the focus remains on creating effective plans. "
    "If you determine that you need more information from the user to create a plan, "
    "ask specific follow-up questions to gather the necessary details."
)


# 대화 히스토리 초기화
history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]


# ChatGPT API 호출 함수 (using history)
def chatGPT(user_input):
    global history

    # 사용자 입력 추가
    history.append({"role": "user", "content": user_input})

    # GPT 호출
    response = client.chat.completions.create(
        model="gpt-4o",  # 사용하는 모델명
        messages=history,
        temperature=0.7
    )

    # GPT 응답 저장
    assistant_response = response.choices[0].message.content
    history.append({"role": "assistant", "content": assistant_response})

    return assistant_response


# 사용자와의 대화 함수
def chat_with_user():
    print("Chatbot: 안녕하세요? 당신의 계획 수립을 도와드릴게요! 당신의 상황(ex: 과제 정보, 마감기한)에 대해 알려주세요.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! Take care!")
            break

        # ChatGPT와 대화
        response = chatGPT(user_input)
        print(f"Chatbot: {response} \n[대화를 끝내고 싶다면 'quit' 또는 'exit' 를 입력해주세요.]")


if __name__ == "__main__":
    chat_with_user()
