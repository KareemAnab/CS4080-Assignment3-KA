from abc import ABC, abstractmethod
import re
from typing import List
from data_types import UserProfile, Request, Response, CommandType

class AIAssistant(ABC):
    def __init__(self, user: UserProfile):
        self.user = user

    def greet_user(self) -> str:
        return f"Hello, {self.user.name}! What can I do for you today?"

    @abstractmethod
    def handle_request(self, req: Request) -> Response:
        ...

    @abstractmethod
    def generate_response(self, req: Request) -> Response:
        ...

class MusicAssistant(AIAssistant):
    def __init__(self, user: UserProfile):
        super().__init__(user)
        self.playlists = {
            "pop":       ["Blinding Lights – The Weeknd", "Levitating – Dua Lipa"],
            "rock":      ["Hotel California – Eagles", "Back in Black – AC/DC"],
            "jazz":      ["So What – Miles Davis", "Take Five – Dave Brubeck"],
            "classical": ["Moonlight Sonata – Beethoven", "Clair de Lune – Debussy"],
        }

    def recommend_playlist(self, genre: str) -> List[str]:
        return self.playlists.get(genre.lower(), self.playlists["pop"])

    def handle_request(self, req: Request) -> Response:
        if req.command != CommandType.PLAY_MUSIC:
            return Response("I can only handle music requests right now.", 0.0, False)
        return self.generate_response(req)

    def generate_response(self, req: Request) -> Response:
        # parse genre keyword if present
        match = re.search(r"\b(pop|rock|jazz|classical)\b", req.text, re.IGNORECASE)
        genre = match.group(1) if match else self.user.preferences.get("genre", "pop")
        playlist = self.recommend_playlist(genre)
        msg = f"Here’s your {genre.title()} playlist:\n" + "\n".join(f" - {s}" for s in playlist)
        confidence = 0.9 if match else 0.6
        return Response(msg, confidence, True)

class FitnessAssistant(AIAssistant):
    def __init__(self, user: UserProfile):
        super().__init__(user)
        self.workouts = {
            "strength":    "3×5 squats, 3×5 bench press, 3×5 deadlift",
            "endurance":   "30 min run + 15 min bike",
            "flexibility": "20 min yoga + 10 min stretching",
        }

    def suggest_workout(self, goal: str) -> str:
        return self.workouts.get(goal.lower(), self.workouts["endurance"])

    def handle_request(self, req: Request) -> Response:
        if req.command != CommandType.SUGGEST_WORKOUT:
            return Response("I can only handle workout requests right now.", 0.0, False)
        return self.generate_response(req)

    def generate_response(self, req: Request) -> Response:
        match = re.search(r"\b(strength|endurance|flexibility)\b", req.text, re.IGNORECASE)
        goal = match.group(1) if match else self.user.preferences.get("goal", "endurance")
        routine = self.suggest_workout(goal)
        msg = f"Here’s a {goal.title()} routine for you:\n{routine}"
        confidence = 0.85 if match else 0.5
        return Response(msg, confidence, True)
