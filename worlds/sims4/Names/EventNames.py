from enum import StrEnum

class Aspiration(StrEnum):
    BODYBUILDER = ("Completed Bodybuilder Aspiration", "Completed Bodybuilder")
    PAINTER_EXTRAORDINAIRE = ("Completed Painter Extraordinaire Aspiration", "Completed Painter Extraordinaire")
    BESTSELLING_AUTHOR = ("Completed Bestselling Author Aspiration", "Completed Bestselling Author")
    MUSICAL_GENIUS = ("Completed Musical Genius Aspiration", "Completed Musical Genius")
    CHIEF_OF_MISCHIEF = ("Completed Chief of Mischief Aspiration", "Completed Chief of Mischief")
    PUBLIC_ENEMY = ("Completed Public Enemy Aspiration", "Completed Public Enemy")
    MASTER_CHEF = ("Completed Master Chef Aspiration", "Completed Master Chef")
    MASTER_MIXOLOGIST = ("Completed Master Mixologist Aspiration", "Completed Master Mixologist")
    RENAISSANCE_SIM = ("Completed Renaissance Sim Aspiration", "Completed Renaissance Sim")
    NERD_BRAIN = ("Completed Nerd Brain Aspiration", "Completed Nerd Brain")
    COMPUTER_WHIZ = ("Completed Computer Whiz Aspiration", "Completed Computer Whiz")
    SERIAL_ROMANTIC = ("Completed Serial Romantic Aspiration", "Completed Serial Romantic")
    FREELANCE_BOTANIST = ("Completed Freelance Botanist Aspiration", "Completed Freelance Botanist")
    THE_CURATOR = ("Completed The Curator Aspiration", "Completed The Curator")
    ANGLING_ACE = ("Completed Angling Ace Aspiration", "Completed Angling Ace")
    JOKE_STAR = ("Completed Joke Star Aspiration", "Completed Joke Star")
    FRIEND_OF_THE_WORLD = ("Completed Friend of the World Aspiration", "Completed Friend of the World")
    NEIGHBORLY_ADVISOR = ("Completed Neighborly Advisor Aspiration", "Completed Neighborly Advisor")

    @property
    def aspiration_name(self):
        return self.value[0]

    @property
    def item_name(self):
        return self.value[1]