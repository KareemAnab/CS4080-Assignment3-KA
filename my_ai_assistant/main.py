import re
from datetime import datetime
from random import choice
from data_types import UserProfile, Request, CommandType
from ai_assistants import MusicAssistant, FitnessAssistant

def parse_command(text: str) -> CommandType:
    t = text.lower()
    if re.search(r"\b(play|song|music)\b", t):
        return CommandType.PLAY_MUSIC
    if re.search(r"\b(workout|exercise|strength|endurance)\b", t):
        return CommandType.SUGGEST_WORKOUT
    if re.search(r"\b(study|learn|explain)\b", t):
        return CommandType.SCHEDULE_STUDY
    return CommandType.UNKNOWN

def select_assistant(user: UserProfile, cmd: CommandType):
    if cmd == CommandType.PLAY_MUSIC:
        return MusicAssistant(user)
    if cmd == CommandType.SUGGEST_WORKOUT:
        return FitnessAssistant(user)
    return MusicAssistant(user)

def simulate():
    users = [
        UserProfile("Alice", 30, {"genre":"jazz",      "goal":"strength"},    True),
        UserProfile("Bob",   22, {"genre":"rock",      "goal":"endurance"},   False),
        UserProfile("Cara",  27, {"genre":"classical", "goal":"flexibility"}, True),
    ]
    utterances = [
        "Hey, play some music for me",
        "I want a strength workout",
        "Give me a pop playlist",
        "Suggest an endurance routine",
        "Play jazz songs",
        "What’s a flexibility plan?",
    ]

    for user in users:
        print(f"=== Session for {user.name} ===")
        bot = None
        print(user.name, "→", MusicAssistant(user).greet_user())
        for _ in range(3):
            text = choice(utterances)
            cmd  = parse_command(text)
            bot  = select_assistant(user, cmd)
            req  = Request(text, datetime.now(), cmd)
            res  = bot.handle_request(req)
            print(f"  [{cmd.name}] {res.message}  (conf={res.confidence:.2f})")
        print()

if __name__ == "__main__":
    simulate()
