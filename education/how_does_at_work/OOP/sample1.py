class SoccerPlayer():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goals=1):
        self.goals += goals

    def make_assist(self, assists=1):
        self.assists += assists

    def statistics(self):
        print(f'{self.name} {self.surname} - голы: {self.goals}, передачи: {self.assists}')


footballer = SoccerPlayer('Leo', 'Messi')
footballer.score(3)
footballer.make_assist(4)
footballer.statistics()
