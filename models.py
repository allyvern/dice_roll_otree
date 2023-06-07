from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random

#code without otree

def comp_dice_roll():
    i = 0
    dice_roll = random.randint(1,6)
    i += 1
    if i <= 6:
        return dice_roll



# def main():
#     rolling = True
#     while rolling:
#         answer = input("To throw the dice press Y if you want to stop press any key")
#         if answer.lower() == "Y" or answer.lower() == "y":
#             number_of_die = int(input("How many dice do you want to throw? "))
#             roll(number_of_die)
#         else:
#             print("Thank you for playing!")
#             break


doc = """
This is a practice for creating a dice roll game
"""


class Constants(BaseConstants):
    name_in_url = 'dice_roll'
    players_per_group = None
    num_rounds = 6


class Subsession(BaseSubsession):
    comp_dice_roll = models.IntegerField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    player_dice_roll = models.IntegerField(min=1, max=6)

    points = models.IntegerField()
