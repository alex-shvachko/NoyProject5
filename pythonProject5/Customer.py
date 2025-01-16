import time

class Customer:
    def __init__(self, name, mood, personality, initial_patience=100, arrive_time=None):
        self.__name = name
        self.__mood = mood
        self.__personality = personality
        self.__patience = initial_patience
        self.__initial_patience = initial_patience
        self.__arrive_time = arrive_time if arrive_time else int(time.time())

    def get_mood(self):
        return self.__mood

    def get_personality(self):
        return self.__personality

     # def get_initial_patience(self):
     #     return self.__initial_patience

    def get_arrive_time(self):
        return self.__arrive_time

    def get_waiting_time(self, current_time=None):
        current_time = current_time if current_time else int(time.time())
        return current_time - self.__arrive_time

    def get_patience(self):
        return round(self.__patience, 2)

    def update(self, waiting_time=None):
        if waiting_time is None:
            waiting_time = self.get_waiting_time()
        #patience_factor = self.get_mood().get_patience_factor(waiting_time)
        # self.__patience = max(self.get_initial_patience() - patience_factor, 0)
        self.__patience = self.__initial_patience - self.__mood.get_patience_factor(waiting_time)
        self.__mood = self.get_personality().adjust_mood(self.__mood, waiting_time)

    def __repr__(self):
        rows = [
            f"* name: {self.__name}",
            f"* mood: {self.__mood}",
            f"* personality: {self.__personality}",
            f"* patience: {self.__patience}"]
        max_row = max(len(row) for row in rows)
        border = "*" * (max_row+2)
        frame = [border] +[row.ljust(max_row+1) + "*" for row in rows] + [border]
        return "\n".join(frame)



