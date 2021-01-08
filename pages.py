from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Welcome(Page):
    """Welcome page"""
    def is_displayed(self):
        return self.round_number == 1
    def vars_for_template(self):
        return dict(participant_id = self.participant.label)

class Introduction(Page):
    """Description of the game"""
    def is_displayed(self):
        return self.round_number == 1
    def vars_for_template(self):
        return dict(participant_id = self.participant.label)
    pass


class Game(Page):
    """How to play and returns expected"""
    def is_displayed(self):
        return self.round_number == 1
    def vars_for_template(self):
        return dict(participant_id = self.participant.label)
    pass

class Probab(Page):
    """How affect the prevention level"""
    def is_displayed(self):
        return self.round_number == 1
    def vars_for_template(self):
        return dict(participant_id = self.participant.label)
    pass

class Contribute(Page):
    """Player: Choose how much to contribute"""

    form_model = 'player'
    form_fields = ['precaution']
    def vars_for_template(self):
        return dict(participant_id = self.participant.label)

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

    body_text = "Waiting for other participants to decide."
    def vars_for_template(self):
        return dict(participant_id = self.participant.label)


class Results(Page):
    """Players payoff: How much each has earned"""

    def vars_for_template(self):
        return dict(costo_contagiado=self.player.prob_intrinseca ,
                    participant_id = self.participant.label)

class R_Final(Page):
    def is_displayed(self):
        return self.round_number == 10
    def vars_for_template(self):
        return dict(pago_real = self.player.pago_acumulado.to_real_world_currency(self.session) ,
               participant_id = self.participant.label)

class Treatment_1(Page):
    """Just for treated group 1"""
    def is_displayed(self):
        return self.player.tratado_1 == 1 and self.round_number == 1

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

class Treatment_2(Page):
    """"Just for treated group 2"""
    def is_displayed(self):
        return self.player.tratado_1 == 2 and self.round_number == 1

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)
        #return self.round_number == 1

class Last(Page):
    def is_displayed(self):
        return self.round_number == 10
    def vars_for_template(self):
        return dict(participant_id = self.participant.label)

page_sequence = [Welcome, Introduction, Game, Probab, Contribute, ResultsWaitPage, Results, Treatment_1, Treatment_2, R_Final, Last]