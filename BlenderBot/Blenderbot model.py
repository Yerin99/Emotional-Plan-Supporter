import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


# 모델 이름
MODEL_NAME = "facebook/blenderbot_small-90M"

# 토크나이저와 모델 로드
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# GPU 또는 CPU 선택
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)


def chat_Blenderbot(user_input):
    # 입력 데이터 생성
    inputs = tokenizer(user_input, return_tensors="pt")
    inputs = {key: value.to(device) for key, value in inputs.items()}

    # 모델을 사용해 응답 생성
    reply_ids = model.generate(**inputs)
    reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)

    return reply


def chat_with_user():
    print("Chatbot: 안녕하세요? 당신의 계획 수립을 도와드릴게요! 당신의 상황(ex: 과제 정보, 마감기한)에 대해 알려주세요.")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! Take care!")
            break

        # Blenderbot와 대화
        response = chat_Blenderbot(user_input)
        print(f"Chatbot: {response} \n[대화를 끝내고 싶다면 'quit' 또는 'exit' 를 입력해주세요.]")


if __name__ == "__main__":
    chat_with_user()
