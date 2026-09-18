def format_dialogue(text, emotion="NEUTRAL"):
    text = text.strip()
    emotion = emotion.upper()
    return f"[{emotion}] {text}"

def main():
    dialogue = input("Enter dialogue: ")
    emotion = input("Emotion (optional): ")

    if emotion.strip() == "":
        emotion = "NEUTRAL"

    formatted = format_dialogue(dialogue, emotion)
    print(formatted)

if __name__ == "__main__":
    main()
