class StreakMaintenance:
    def __init__(self):
        self.streaks = {}

    def add_streak(self, user_id, streak):
        self.streaks[user_id] = streak

    def update_streak(self, user_id, days):
        if user_id in self.streaks:
            self.streaks[user_id] += days
        else:
            self.add_streak(user_id, days)

    def check_streak(self, user_id):
        return self.streaks.get(user_id, 0)

    def maintain_streaks(self):
        for user_id, streak in self.streaks.items():
            if streak > 0:
                self.streaks[user_id] -= 1

def main():
    streak_maintenance = StreakMaintenance()
    streak_maintenance.add_streak(1, 10)
    streak_maintenance.update_streak(1, 5)
    print(streak_maintenance.check_streak(1))
    streak_maintenance.maintain_streaks()
    print(streak_maintenance.check_streak(1))

if __name__ == "__main__":
    main()