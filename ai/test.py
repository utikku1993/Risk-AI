from ai import AI
import random
import collections
import math
from recorder import Recorder
from decision_engine import Decision_Engine

class TestAI(AI):
    """
    TestAI is basically a wrapper for an AI agent with intent recognition system and a
    model-based non-deceptive decision engine.
    """
    

    def __init__(self, player, game, world, **kwargs):
        self.recorder = Recorder('TestAI')
        self.decision_engine = Decision_Engine(5, world)
        super(TestAI, self).__init__( player, game, world, **kwargs)
    
    def start(self):
        self.saveGamestate()
        self.area_priority = self.decision_engine.area_priority_gen(self.world, self.player)

    def priority(self):
        return self.decision_engine.priority(self.world, self.player)

    def initial_placement(self, empty, available):
        self.saveGamestate()
        if empty:
            for x,y,z in self.decision_engine.area_centrality:
                for t in z:
                    for t_1 in empty:
                        if t_1.name == t[1]:
                            return t_1
        else:
            return random.choice(self.priority())

    def saveGamestate(self):
        self.recorder.recordGamestate(self.world, self.game)

    def reinforce(self, available):
        self.saveGamestate()
        return self.decision_engine.reinforce(available, self.world, self.player, self.recorder.intents, self.recorder.predictions)

    def attack(self):
        self.saveGamestate()
        return self.decision_engine.attack(self.world, self.player, self.recorder.intents, self.recorder.predictions)
    
    def freemove(self):
        self.saveGamestate()
        return self.decision_engine.freemove(self.world, self.player, self.recorder.intents, self.recorder.predictions)