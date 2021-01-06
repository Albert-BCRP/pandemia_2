from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Welcome(Page):
    """Welcome page"""
    def is_displayed(self):
        return self.round_number == 1

class Introduction(Page):
    """Description of the game"""
    def is_displayed(self):
        return self.round_number == 1
    pass


class Game(Page):
    """How to play and returns expected"""
    def is_displayed(self):
        return self.round_number == 1
    pass

class Probab(Page):
    """How affect the prevention level"""
    def is_displayed(self):
        return self.round_number == 1
    pass

class Contribute(Page):
    """Player: Choose how much to contribute"""

    form_model = 'player'
    form_fields = ['precaution']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    body_text = "Waiting for other participants to decide."


class Results(Page):
    """Players payoff: How much each has earned"""

    def vars_for_template(self):
        return dict(costo_contagiado=self.player.prob_intrinseca)

class Treatment_1(Page):
    """Just for treated group 1"""
    def is_displayed(self):
        return self.player.tratado_1 == 1 and self.round_number == 1
        #return self.round_number == 1


class Treatment_2(Page):
    """"Just for treated group 2"""
    def is_displayed(self):
        return self.player.tratado_1 == 2 and self.round_number == 1
        #return self.round_number == 1



page_sequence = [Welcome, Introduction, Game, Probab, Contribute, ResultsWaitPage, Results, Treatment_1, Treatment_2]