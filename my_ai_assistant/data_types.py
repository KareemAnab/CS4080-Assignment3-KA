from enum import Enum
from datetime import datetime
from typing import Any, Dict

class CommandType(Enum):
    PLAY_MUSIC      = "play_music"
    SUGGEST_WORKOUT = "suggest_workout"
    SCHEDULE_STUDY  = "schedule_study"
    UNKNOWN         = "unknown"  

class UserProfile:
    def __init__(self, name: str, age: int, preferences: Dict[str, Any], is_premium: bool):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("age must be a positive integer")
        if not isinstance(preferences, dict):
            raise ValueError("preferences must be a dict")
        if not isinstance(is_premium, bool):
            raise ValueError("is_premium must be a bool")

        self.name        = name.strip()
        self.age         = age
        self.preferences = preferences
        self.is_premium  = is_premium

    def __repr__(self):
        return f"UserProfile(name={self.name!r}, age={self.age}, is_premium={self.is_premium}, preferences={self.preferences})"

class Request:
    def __init__(self, text: str, timestamp: datetime, command: CommandType):
        if not isinstance(text, str) or not text.strip():
            raise ValueError("text must be a non-empty string")
        if not isinstance(timestamp, datetime):
            raise ValueError("timestamp must be datetime")
        if not isinstance(command, CommandType):
            raise ValueError("command must be a CommandType")

        self.text      = text.strip()
        self.timestamp = timestamp
        self.command   = command

    def __repr__(self):
        return f"Request(text={self.text!r}, timestamp={self.timestamp.isoformat()}, command={self.command})"

class Response:
    def __init__(self, message: str, confidence: float = 1.0, action_performed: bool = True):
        if not isinstance(message, str) or not message.strip():
            raise ValueError("message must be a non-empty string")
        if not isinstance(confidence, (int, float)) or not (0.0 <= confidence <= 1.0):
            raise ValueError("confidence must be between 0.0 and 1.0")
        if not isinstance(action_performed, bool):
            raise ValueError("action_performed must be a bool")

        self.message          = message.strip()
        self.confidence       = float(confidence)
        self.action_performed = action_performed

    def __repr__(self):
        return (f"Response(message={self.message!r}, "
                f"confidence={self.confidence:.2f}, "
                f"action_performed={self.action_performed})")
