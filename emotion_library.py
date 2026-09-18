# emotion_library.py
# A centralized emotion mapping system for your anime/manga pipeline.

EMOTION_MAP = {
    "angry": {
        "tag": "ANGRY",
        "intensity": 3,
        "synonyms": ["mad", "furious", "irate", "enraged", "heated"]
    },
    "sad": {
        "tag": "SAD",
        "intensity": 2,
        "synonyms": ["down", "blue", "depressed", "melancholy"]
    },
    "happy": {
        "tag": "HAPPY",
        "intensity": 3,
        "synonyms": ["joyful", "glad", "content", "cheerful"]
    },
    "determined": {
        "tag": "DETERMINED",
        "intensity": 4,
        "synonyms": ["resolved", "focused", "driven", "steadfast"]
    },
    "fear": {
        "tag": "AFRAID",
        "intensity": 3,
        "synonyms": ["scared", "terrified", "nervous", "anxious"]
    },
    "surprised": {
        "tag": "SURPRISED",
        "intensity": 2,
        "synonyms": ["shocked", "astonished", "taken aback"]
    },
    "neutral": {
        "tag": "NEUTRAL",
        "intensity": 1,
        "synonyms": ["calm", "unmoved", "stoic"]
    }
}

def resolve_emotion(user_input):
    """
    Takes the user's emotion input and resolves it to a standardized tag.
    Handles synonyms and unknown emotions gracefully.
    """
    if not user_input:
        return None

    cleaned = user_input.strip().lower()

    # Direct match
    if cleaned in EMOTION_MAP:
        return EMOTION_MAP[cleaned]["tag"]

    # Synonym match
    for emotion, data in EMOTION_MAP.items():
        if cleaned in data["synonyms"]:
            return data["tag"]

    # Unknown emotion fallback
    return cleaned.upper()
