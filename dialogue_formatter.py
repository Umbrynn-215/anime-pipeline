# dialogue_formatter.py
# Updated to use the emotion resolution system from emotion_library.py

from emotion_library import resolve_emotion

def format_dialogue(dialogue, emotion=None):
    """
    Formats dialogue with an optional emotion tag.
    Uses the emotion resolver to standardize emotion input.
    """
    cleaned_dialogue = dialogue.strip()

    if emotion:
        resolved = resolve_emotion(emotion)
        return f"[{resolved}] {cleaned_dialogue}"
    else:
        return cleaned_dialogue

def main():
    dialogue = input("Enter dialogue: ")
    emotion = input("Emotion (optional): ")

    result = format_dialogue(dialogue, emotion)
    print(result)

if __name__ == "__main__":
    main()
