from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.AutoWorld import LogicMixin
from .Names.DLC import ExpansionNames, GamePackNames, StuffNames
from ..generic.Rules import set_rule

from .Names import SkillNames, CareerNames, AspirationNames
from .Options import Sims4Options

if TYPE_CHECKING:
    from . import Sims4World


class Sims4Logic(LogicMixin):
    def _sims4_rule(self, player: int):
        return True


def set_rules(sims4_world: Sims4World):
    world = sims4_world.multiworld
    player = sims4_world.player
    options: Sims4Options = sims4_world.options

    # Career Rules
    # TODO relearn how the career locations send, and then refactor this to use has_skill

    # Athlete
    if CareerNames.base_career_athlete in options.career:
        set_rule(world.get_location(CareerNames.base_career_athlete_4, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=1)
                               and state.has(SkillNames.base_skill_fitness, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_athlete_5A, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=2)
                               and state.has(SkillNames.base_skill_fitness, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_athlete_5B, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=2)
                               and state.has(SkillNames.base_skill_fitness, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_athlete_6A, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=2)
                               and state.has(SkillNames.base_skill_fitness, player, count=3))
        set_rule(world.get_location(CareerNames.base_career_athlete_7A, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=2)
                               and state.has(SkillNames.base_skill_fitness, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_athlete_8A, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=3)
                               and state.has(SkillNames.base_skill_fitness, player, count=6))
        set_rule(world.get_location(CareerNames.base_career_athlete_9A, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=4)
                               and state.has(SkillNames.base_skill_fitness, player, count=7))
        set_rule(world.get_location(CareerNames.base_career_athlete_10A, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=6)
                               and state.has(SkillNames.base_skill_fitness, player, count=8))
        set_rule(world.get_location(CareerNames.base_career_athlete_6B, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=3)
                               and state.has(SkillNames.base_skill_fitness, player, count=6))
        set_rule(world.get_location(CareerNames.base_career_athlete_7B, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=3)
                               and state.has(SkillNames.base_skill_fitness, player, count=7))
        set_rule(world.get_location(CareerNames.base_career_athlete_8B, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=4)
                               and state.has(SkillNames.base_skill_fitness, player, count=8))
        set_rule(world.get_location(CareerNames.base_career_athlete_9B, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=5)
                               and state.has(SkillNames.base_skill_fitness, player, count=8))
        set_rule(world.get_location(CareerNames.base_career_athlete_10B, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=6)
                               and state.has(SkillNames.base_skill_fitness, player, count=8))
    # Astronaut
    if CareerNames.base_career_astronaut in options.career:
        set_rule(world.get_location(CareerNames.base_career_astronaut_4, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_astronaut_5, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=2)
                               and state.has(SkillNames.base_skill_fitness, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_astronaut_6, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=3)
                               and state.has(SkillNames.base_skill_fitness, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_astronaut_7, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=3)
                               and state.has(SkillNames.base_skill_fitness, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_astronaut_8A, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=4)
                               and state.has(SkillNames.base_skill_fitness, player, count=5))
        set_rule(world.get_location(CareerNames.base_career_astronaut_8B, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=4)
                               and state.has(SkillNames.base_skill_fitness, player, count=5))
        set_rule(world.get_location(CareerNames.base_career_astronaut_9A, player),
                 lambda state: state.has(SkillNames.base_skill_fitness, player, count=6))
        set_rule(world.get_location(CareerNames.base_career_astronaut_10A, player),
                 lambda state: state.has(SkillNames.base_skill_rocket_science, player, count=2)
                               and state.has(SkillNames.base_skill_fitness, player, count=8))
        set_rule(world.get_location(CareerNames.base_career_astronaut_9B, player),
                 lambda state: state.has(SkillNames.base_skill_fitness, player, count=6))
        set_rule(world.get_location(CareerNames.base_career_astronaut_10B, player),
                 lambda state: state.has(SkillNames.base_skill_rocket_science, player, count=2)
                               and state.has(SkillNames.base_skill_fitness, player, count=8))
    # Business
    if CareerNames.base_career_business in options.career:
        set_rule(world.get_location(CareerNames.base_career_business_5, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_business_6, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_business_7A, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=2)
                               and state.has(SkillNames.base_skill_logic, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_business_7B, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=2)
                               and state.has(SkillNames.base_skill_logic, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_business_8A, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=4)
                               and state.has(SkillNames.base_skill_logic, player, count=3))
        set_rule(world.get_location(CareerNames.base_career_business_9A, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=6)
                               and state.has(SkillNames.base_skill_logic, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_business_10A, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=8)
                               and state.has(SkillNames.base_skill_logic, player, count=6))
        set_rule(world.get_location(CareerNames.base_career_business_8B, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=3)
                               and state.has(SkillNames.base_skill_logic, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_business_9B, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=4)
                               and state.has(SkillNames.base_skill_logic, player, count=6))
        set_rule(world.get_location(CareerNames.base_career_business_10B, player),
                 lambda state: state.has(SkillNames.base_skill_charisma, player, count=6)
                               and state.has(SkillNames.base_skill_logic, player, count=8))
    # Criminal
    if CareerNames.base_career_criminal in options.career:
        set_rule(world.get_location(CareerNames.base_career_criminal_4, player),
                 lambda state: state.has(SkillNames.base_skill_mischief, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_criminal_5, player),
                 lambda state: state.has(SkillNames.base_skill_mischief, player, count=3))
        set_rule(world.get_location(CareerNames.base_career_criminal_6A, player),
                 lambda state: state.has(SkillNames.base_skill_mischief, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_criminal_6B, player),
                 lambda state: state.has(SkillNames.base_skill_mischief, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_criminal_7A, player),
                 lambda state: state.has(SkillNames.base_skill_mischief, player, count=5))
        set_rule(world.get_location(CareerNames.base_career_criminal_8A, player),
                 lambda state: state.has(SkillNames.base_skill_mischief, player, count=6))
        set_rule(world.get_location(CareerNames.base_career_criminal_9A, player),
                 lambda state: state.has(SkillNames.base_skill_mischief, player, count=7)
                               and state.has(SkillNames.base_skill_handiness, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_criminal_10A, player),
                 lambda state: state.has(SkillNames.base_skill_mischief, player, count=8)
                               and state.has(SkillNames.base_skill_handiness, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_criminal_7B, player),
                 lambda state: state.has(SkillNames.base_skill_mischief, player, count=5)
                               and state.has(SkillNames.base_skill_programming, player, count=0))
        set_rule(world.get_location(CareerNames.base_career_criminal_8B, player),
                 lambda state: state.has(SkillNames.base_skill_mischief, player, count=6)
                               and state.has(SkillNames.base_skill_programming, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_criminal_9B, player),
                 lambda state: state.has(SkillNames.base_skill_mischief, player, count=7)
                               and state.has(SkillNames.base_skill_programming, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_criminal_10B, player),
                 lambda state: state.has(SkillNames.base_skill_mischief, player, count=8)
                               and state.has(SkillNames.base_skill_programming, player, count=6))
    # Culinary
    if CareerNames.base_career_culinary in options.career:
        set_rule(world.get_location(CareerNames.base_career_culinary_5, player),
                 lambda state: state.has(SkillNames.base_skill_cooking, player, count=1)
                               and state.has(SkillNames.base_skill_mixology, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_culinary_6A, player),
                 lambda state: state.has(SkillNames.base_skill_cooking, player, count=2)
                               and state.has(SkillNames.base_skill_mixology, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_culinary_6B, player),
                 lambda state: state.has(SkillNames.base_skill_cooking, player, count=2)
                               and state.has(SkillNames.base_skill_mixology, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_culinary_7A, player),
                 lambda state: state.has(SkillNames.base_skill_cooking, player, count=4)
                               and state.has(SkillNames.base_skill_gourmet, player, count=0)
                               and state.has(SkillNames.base_skill_mixology, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_culinary_8A, player),
                 lambda state: state.has(SkillNames.base_skill_cooking, player, count=6)
                               and state.has(SkillNames.base_skill_gourmet, player, count=4)
                               and state.has(SkillNames.base_skill_mixology, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_culinary_9A, player),
                 lambda state: state.has(SkillNames.base_skill_cooking, player, count=6)
                               and state.has(SkillNames.base_skill_gourmet, player, count=4)
                               and state.has(SkillNames.base_skill_mixology, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_culinary_10A, player),
                 lambda state: state.has(SkillNames.base_skill_cooking, player, count=8)
                               and state.has(SkillNames.base_skill_gourmet, player, count=6)
                               and state.has(SkillNames.base_skill_mixology, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_culinary_7B, player),
                 lambda state: state.has(SkillNames.base_skill_mixology, player, count=3)
                               and state.has(SkillNames.base_skill_charisma, player, count=0)
                               and state.has(SkillNames.base_skill_cooking, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_culinary_8B, player),
                 lambda state: state.has(SkillNames.base_skill_mixology, player, count=5)
                               and state.has(SkillNames.base_skill_charisma, player, count=2)
                               and state.has(SkillNames.base_skill_cooking, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_culinary_9B, player),
                 lambda state: state.has(SkillNames.base_skill_mixology, player, count=6)
                               and state.has(SkillNames.base_skill_charisma, player, count=4)
                               and state.has(SkillNames.base_skill_cooking, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_culinary_10B, player),
                 lambda state: state.has(SkillNames.base_skill_mixology, player, count=8)
                               and state.has(SkillNames.base_skill_charisma, player, count=6)
                               and state.has(SkillNames.base_skill_cooking, player, count=2))
    # Entertainer
    if CareerNames.base_career_entertainer in options.career:
        set_rule(world.get_location(CareerNames.base_career_entertainer_5A, player),
                 lambda state: (state.has(SkillNames.base_skill_guitar, player, count=1)
                                or state.has(SkillNames.base_skill_violin, player, count=1))
                               and state.has(SkillNames.base_skill_comedy, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_entertainer_5B, player),
                 lambda state: (state.has(SkillNames.base_skill_guitar, player, count=1)
                                or state.has(SkillNames.base_skill_violin, player, count=1))
                               and state.has(SkillNames.base_skill_comedy, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_entertainer_6A, player),
                 lambda state: state.has(SkillNames.base_skill_violin, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_entertainer_7A, player),
                 lambda state: (state.has(SkillNames.base_skill_guitar, player, count=3)
                                or state.has(SkillNames.base_skill_violin, player, count=3))
                               and state.has(SkillNames.base_skill_piano, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_entertainer_8A, player),
                 lambda state: (state.has(SkillNames.base_skill_guitar, player, count=4)
                                or state.has(SkillNames.base_skill_violin, player, count=4))
                               and state.has(SkillNames.base_skill_piano, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_entertainer_9A, player),
                 lambda state: (state.has(SkillNames.base_skill_guitar, player, count=5)
                                or state.has(SkillNames.base_skill_violin, player, count=5))
                               and state.has(SkillNames.base_skill_piano, player, count=6))
        set_rule(world.get_location(CareerNames.base_career_entertainer_10A, player),
                 lambda state: (state.has(SkillNames.base_skill_guitar, player, count=6)
                                or state.has(SkillNames.base_skill_violin, player, count=6))
                               and state.has(SkillNames.base_skill_piano, player, count=8))
        set_rule(world.get_location(CareerNames.base_career_entertainer_6B, player),
                 lambda state: state.has(SkillNames.base_skill_comedy, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_entertainer_7B, player),
                 lambda state: state.has(SkillNames.base_skill_comedy, player, count=5))
        set_rule(world.get_location(CareerNames.base_career_entertainer_8B, player),
                 lambda state: state.has(SkillNames.base_skill_comedy, player, count=6)
                               and state.has(SkillNames.base_skill_charisma, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_entertainer_9B, player),
                 lambda state: state.has(SkillNames.base_skill_comedy, player, count=7)
                               and state.has(SkillNames.base_skill_charisma, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_entertainer_10B, player),
                 lambda state: state.has(SkillNames.base_skill_comedy, player, count=8)
                               and state.has(SkillNames.base_skill_charisma, player, count=6))
    # Painter
    if CareerNames.base_career_painter in options.career:
        set_rule(world.get_location(CareerNames.base_career_painter_4, player),
                 lambda state: state.has(SkillNames.base_skill_painting, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_painter_5, player),
                 lambda state: state.has(SkillNames.base_skill_painting, player, count=3))
        set_rule(world.get_location(CareerNames.base_career_painter_6, player),
                 lambda state: state.has(SkillNames.base_skill_painting, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_painter_7A, player),
                 lambda state: state.has(SkillNames.base_skill_painting, player, count=5))
        set_rule(world.get_location(CareerNames.base_career_painter_7B, player),
                 lambda state: state.has(SkillNames.base_skill_painting, player, count=5))
        set_rule(world.get_location(CareerNames.base_career_painter_8A, player),
                 lambda state: state.has(SkillNames.base_skill_painting, player, count=6))
        set_rule(world.get_location(CareerNames.base_career_painter_9A, player),
                 lambda state: state.has(SkillNames.base_skill_painting, player, count=7)
                               and state.has(SkillNames.base_skill_logic, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_painter_10A, player),
                 lambda state: state.has(SkillNames.base_skill_painting, player, count=8)
                               and state.has(SkillNames.base_skill_logic, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_painter_8B, player),
                 lambda state: state.has(SkillNames.base_skill_painting, player, count=6))
        set_rule(world.get_location(CareerNames.base_career_painter_9B, player),
                 lambda state: state.has(SkillNames.base_skill_painting, player, count=7)
                               and state.has(SkillNames.base_skill_charisma, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_painter_10B, player),
                 lambda state: state.has(SkillNames.base_skill_painting, player, count=8)
                               and state.has(SkillNames.base_skill_charisma, player, count=4))
    # Secret Agent
    if CareerNames.base_career_secret_agent in options.career:
        set_rule(world.get_location(CareerNames.base_career_secret_agent_4, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=1)
                               and state.has(SkillNames.base_skill_charisma, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_secret_agent_5, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=1)
                               and state.has(SkillNames.base_skill_charisma, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_secret_agent_6, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=3)
                               and state.has(SkillNames.base_skill_charisma, player, count=3))
        set_rule(world.get_location(CareerNames.base_career_secret_agent_7, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=3)
                               and state.has(SkillNames.base_skill_charisma, player, count=3))
        set_rule(world.get_location(CareerNames.base_career_secret_agent_8A, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=4)
                               and state.has(SkillNames.base_skill_charisma, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_secret_agent_8B, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=4)
                               and state.has(SkillNames.base_skill_charisma, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_secret_agent_9A, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=6)
                               and state.has(SkillNames.base_skill_charisma, player, count=5))
        set_rule(world.get_location(CareerNames.base_career_secret_agent_10A, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=8)
                               and state.has(SkillNames.base_skill_charisma, player, count=6))
        set_rule(world.get_location(CareerNames.base_career_secret_agent_9B, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=6))
        set_rule(world.get_location(CareerNames.base_career_secret_agent_10B, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=8)
                               and state.has(SkillNames.base_skill_mischief, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_secret_agent_11B, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=8)
                               and state.has(SkillNames.base_skill_mischief, player, count=4))
    # Style Influencer
    if CareerNames.base_career_style_influencer in options.career:
        set_rule(world.get_location(CareerNames.base_career_style_influencer_4, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_style_influencer_5, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_style_influencer_6A, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=3)
                               and state.has(SkillNames.base_skill_charisma, player, count=1)
                               and state.has(SkillNames.base_skill_painting, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_style_influencer_7A, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=4)
                               and state.has(SkillNames.base_skill_charisma, player, count=3)
                               and state.has(SkillNames.base_skill_painting, player, count=2)
                               and state.has(SkillNames.base_skill_photography, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_style_influencer_8A, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=5)
                               and state.has(SkillNames.base_skill_charisma, player, count=4)
                               and state.has(SkillNames.base_skill_painting, player, count=3))
        set_rule(world.get_location(CareerNames.base_career_style_influencer_9A, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=6)
                               and state.has(SkillNames.base_skill_charisma, player, count=5)
                               and state.has(SkillNames.base_skill_painting, player, count=6))
        set_rule(world.get_location(CareerNames.base_career_style_influencer_10A, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=7)
                               and state.has(SkillNames.base_skill_charisma, player, count=6)
                               and state.has(SkillNames.base_skill_painting, player, count=5))
        set_rule(world.get_location(CareerNames.base_career_style_influencer_6B, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=3)
                               and state.has(SkillNames.base_skill_charisma, player, count=1)
                               and state.has(SkillNames.base_skill_painting, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_style_influencer_7B, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=4)
                               and state.has(SkillNames.base_skill_charisma, player, count=3)
                               and state.has(SkillNames.base_skill_painting, player, count=2)
                               and state.has(SkillNames.base_skill_photography, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_style_influencer_8B, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=5)
                               and state.has(SkillNames.base_skill_charisma, player, count=4)
                               and state.has(SkillNames.base_skill_painting, player, count=3))
        set_rule(world.get_location(CareerNames.base_career_style_influencer_9B, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=6)
                               and state.has(SkillNames.base_skill_charisma, player, count=5)
                               and state.has(SkillNames.base_skill_painting, player, count=6))
        set_rule(world.get_location(CareerNames.base_career_style_influencer_10B, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=7)
                               and state.has(SkillNames.base_skill_charisma, player, count=6)
                               and state.has(SkillNames.base_skill_painting, player, count=5))
    # Tech Guru
    # TODO check project manager career logic https://discord.com/channels/731205301247803413/1079002955262480424/1403764728177758252
    if CareerNames.base_career_tech_guru in options.career:
        set_rule(world.get_location(CareerNames.base_career_tech_guru_4, player),
                 lambda state: state.has(SkillNames.base_skill_programming, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_tech_guru_5, player),
                 lambda state: state.has(SkillNames.base_skill_programming, player, count=2)
                               and state.has(SkillNames.base_skill_video_gaming, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_tech_guru_6, player),
                 lambda state: state.has(SkillNames.base_skill_programming, player, count=3)
                               and state.has(SkillNames.base_skill_video_gaming, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_tech_guru_7A, player),
                 lambda state: state.has(SkillNames.base_skill_programming, player, count=4)
                               and state.has(SkillNames.base_skill_video_gaming, player, count=3))
        set_rule(world.get_location(CareerNames.base_career_tech_guru_7B, player),
                 lambda state: state.has(SkillNames.base_skill_programming, player, count=4)
                               and state.has(SkillNames.base_skill_video_gaming, player, count=3))
        set_rule(world.get_location(CareerNames.base_career_tech_guru_8A, player),
                 lambda state: state.has(SkillNames.base_skill_programming, player, count=4)
                               and state.has(SkillNames.base_skill_video_gaming, player, count=4))
        set_rule(world.get_location(CareerNames.base_career_tech_guru_9A, player),
                 lambda state: state.has(SkillNames.base_skill_programming, player, count=5)
                               and state.has(SkillNames.base_skill_video_gaming, player, count=6))
        set_rule(world.get_location(CareerNames.base_career_tech_guru_10A, player),
                 lambda state: state.has(SkillNames.base_skill_programming, player, count=6)
                               and state.has(SkillNames.base_skill_video_gaming, player, count=8))
        set_rule(world.get_location(CareerNames.base_career_tech_guru_8B, player),
                 lambda state: state.has(SkillNames.base_skill_programming, player, count=6)
                               and state.has(SkillNames.base_skill_charisma, player, count=0))
        set_rule(world.get_location(CareerNames.base_career_tech_guru_9B, player),
                 lambda state: state.has(SkillNames.base_skill_programming, player, count=7)
                               and state.has(SkillNames.base_skill_charisma, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_tech_guru_10B, player),
                 lambda state: state.has(SkillNames.base_skill_programming, player, count=8)
                               and state.has(SkillNames.base_skill_charisma, player, count=4))
    # Writer
    if CareerNames.base_career_writer in options.career:
        set_rule(world.get_location(CareerNames.base_career_writer_4, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_writer_5, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_writer_6A, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=3))
        set_rule(world.get_location(CareerNames.base_career_writer_6B, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=3))
        set_rule(world.get_location(CareerNames.base_career_writer_7A, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=5))
        set_rule(world.get_location(CareerNames.base_career_writer_8A, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=6)
                               and state.has(SkillNames.base_skill_logic, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_writer_9A, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=7)
                               and state.has(SkillNames.base_skill_logic, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_writer_10A, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=8)
                               and state.has(SkillNames.base_skill_logic, player, count=3))
        set_rule(world.get_location(CareerNames.base_career_writer_7B, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=5))
        set_rule(world.get_location(CareerNames.base_career_writer_8B, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=6)
                               and state.has(SkillNames.base_skill_charisma, player, count=1))
        set_rule(world.get_location(CareerNames.base_career_writer_9B, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=7)
                               and state.has(SkillNames.base_skill_charisma, player, count=2))
        set_rule(world.get_location(CareerNames.base_career_writer_10B, player),
                 lambda state: state.has(SkillNames.base_skill_writing, player, count=8)
                               and state.has(SkillNames.base_skill_charisma, player, count=3))
    # Part Time Jobs

    # Aspirations
    if options.goal.value == options.goal.option_bodybuilder:
        set_rule(world.get_location(AspirationNames.base_aspiration_exercise_demon, player),
                 lambda state: has_skill(state, SkillNames.base_skill_fitness, player, 4))
        set_rule(world.get_location(AspirationNames.base_aspiration_fit_to_a_t, player),
                 lambda state: has_skill(state, SkillNames.base_skill_fitness, player, 6))
        set_rule(world.get_location(AspirationNames.base_aspiration_bodybuilder, player),
                 lambda state: has_skill(state, SkillNames.base_skill_fitness, player, 10))
    elif options.goal.value == options.goal.option_painter_extraordinaire:
        set_rule(world.get_location(AspirationNames.base_aspiration_fine_artist, player),
                 lambda state: has_skill(state, SkillNames.base_skill_painting, player, 4))
        set_rule(world.get_location(AspirationNames.base_aspiration_brushing_with_greatness, player),
                 lambda state: has_skill(state, SkillNames.base_skill_painting, player, 6))
        set_rule(world.get_location(AspirationNames.base_aspiration_painter_extraordinaire, player),
                 lambda state: has_skill(state, SkillNames.base_skill_painting, player, 10))
    elif options.goal.value == options.goal.option_bestselling_author:
        set_rule(world.get_location(AspirationNames.base_aspiration_competent_wordsmith, player),
                 lambda state: has_skill(state, SkillNames.base_skill_writing, player, 4))
        set_rule(world.get_location(AspirationNames.base_aspiration_novelest_novelist, player),
                 lambda state: has_skill(state, SkillNames.base_skill_writing, player, 6))
        set_rule(world.get_location(AspirationNames.base_aspiration_bestselling_author, player),
                 lambda state: has_skill(state, SkillNames.base_skill_writing, player, 10))
    elif options.goal.value == options.goal.option_musical_genius:
        set_rule(world.get_location(AspirationNames.base_aspiration_fine_tuned, player),
                 lambda state: has_skill(state, SkillNames.base_skill_guitar, player, 4)
                               or has_skill(state, SkillNames.base_skill_violin, player, 4)
                               or has_skill(state, SkillNames.base_skill_piano, player, 4))
        set_rule(world.get_location(AspirationNames.base_aspiration_harmonious, player),
                 lambda state: has_skill(state, SkillNames.base_skill_guitar, player, 8)
                               or has_skill(state, SkillNames.base_skill_violin, player, 8)
                               or has_skill(state, SkillNames.base_skill_piano, player, 8))
        set_rule(world.get_location(AspirationNames.base_aspiration_musical_genius, player),
                 lambda state: has_skill(state, SkillNames.base_skill_guitar, player, 10)
                               or has_skill(state, SkillNames.base_skill_violin, player, 10)
                               or has_skill(state, SkillNames.base_skill_piano, player, 10))
    elif options.goal.value == options.goal.option_public_enemy:
        set_rule(world.get_location(AspirationNames.base_aspiration_criminal_mind, player),
                 lambda state: has_skill(state, SkillNames.base_skill_mischief, player, 3))
        set_rule(world.get_location(AspirationNames.base_aspiration_public_enemy, player),
                 lambda state: has_skill(state, SkillNames.base_skill_mischief, player, 8)
                               and has_skill(state, SkillNames.base_skill_programming, player, 4))

    elif options.goal.value == options.goal.option_chief_of_mischief:
        set_rule(world.get_location(AspirationNames.base_aspiration_artful_trickster, player),
                 lambda state: has_skill(state, SkillNames.base_skill_mischief, player, 3))
        set_rule(world.get_location(AspirationNames.base_aspiration_professional_prankster, player),
                 lambda state: has_skill(state, SkillNames.base_skill_mischief, player, 6))
        set_rule(world.get_location(AspirationNames.base_aspiration_chief_of_mischief, player),
                 lambda state: has_skill(state, SkillNames.base_skill_mischief, player, 10))
    elif options.goal.value == options.goal.option_master_chef:
        set_rule(world.get_location(AspirationNames.base_aspiration_captain_cook, player),
                 lambda state: has_skill(state, SkillNames.base_skill_cooking, player, 5))
        set_rule(world.get_location(AspirationNames.base_aspiration_culinary_artist, player),
                 lambda state: has_skill(state, SkillNames.base_skill_cooking, player, 5))
        set_rule(world.get_location(AspirationNames.base_aspiration_master_chef, player),
                 lambda state: (has_skill(state, SkillNames.base_skill_gourmet, player, 6)
                                and has_skill(state, SkillNames.base_skill_cooking, player, 8))
                               or (has_skill(state, SkillNames.base_skill_gourmet, player, 5)
                                   and has_skill(state, SkillNames.base_skill_mixology, player, 7)
                                   and has_skill(state, SkillNames.base_skill_charisma, player, 4)))
    elif options.goal.value == options.goal.option_master_mixologist:
        set_rule(world.get_location(AspirationNames.base_aspiration_electric_mixer, player),
                 lambda state: has_skill(state, SkillNames.base_skill_mixology, player, 4))
        set_rule(world.get_location(AspirationNames.base_aspiration_beverage_boss, player),
                 lambda state: has_skill(state, SkillNames.base_skill_mixology, player, 7)
                               and has_skill(state, SkillNames.base_skill_cooking, player, 4))
        set_rule(world.get_location(AspirationNames.base_aspiration_master_mixologist, player),
                 lambda state: has_skill(state, SkillNames.base_skill_mixology, player, 10)
                               and has_skill(state, SkillNames.base_skill_cooking, player, 4))
    elif options.goal.value == options.goal.option_renaissance_sim:
        set_rule(world.get_location(AspirationNames.base_aspiration_prudent_student, player),
                 lambda state: state.has(SkillNames.base_skill_logic, player, count=1))
        set_rule(world.get_location(AspirationNames.base_aspiration_jack_of_some_trades, player),
                 lambda state: count_skills_over(2, state, player) >= 4)
        set_rule(world.get_location(AspirationNames.base_aspiration_pantologist, player),
                 lambda state: count_skills_over(3, state, player) >= 5)
        set_rule(world.get_location(AspirationNames.base_aspiration_renaissance_sim, player),
                 lambda state: count_skills_over(6, state, player) >= 6)
    elif options.goal.value == options.goal.option_nerd_brain:
        set_rule(world.get_location(AspirationNames.base_aspiration_prudent_student, player),
                 lambda state: has_skill(state, SkillNames.base_skill_logic, player, 3))
        set_rule(world.get_location(AspirationNames.base_aspiration_erudite, player),
                 lambda state: has_skill(state, SkillNames.base_skill_logic, player, 6))
        set_rule(world.get_location(AspirationNames.base_aspiration_rocket_scientist, player),
                 lambda state: has_skill(state, SkillNames.base_skill_handiness, player, 5))
        set_rule(world.get_location(AspirationNames.base_aspiration_nerd_brain, player),
                 lambda state: has_skill(state, SkillNames.base_skill_logic, player, 10)
                               and has_skill(state, SkillNames.base_skill_handiness, player, 5))
    elif options.goal.value == options.goal.option_computer_whiz:
        set_rule(world.get_location(AspirationNames.base_aspiration_technically_adept, player),
                 lambda state: has_skill(state, SkillNames.base_skill_programming, player, 3))
        set_rule(world.get_location(AspirationNames.base_aspiration_computer_geek, player),
                 lambda state: has_skill(state, SkillNames.base_skill_programming, player, 7))
        set_rule(world.get_location(AspirationNames.base_aspiration_computer_whiz, player),
                 lambda state: has_skill(state, SkillNames.base_skill_programming, player, 7)
                               and has_skill(state, SkillNames.base_skill_video_gaming, player, 4))
    elif options.goal.value == options.goal.option_serial_romantic:
        set_rule(world.get_location(AspirationNames.base_aspiration_up_to_date, player),
                 lambda state: has_skill(state, SkillNames.base_skill_charisma, player, 4))
        set_rule(world.get_location(AspirationNames.base_aspiration_romance_juggler, player),
                 lambda state: has_skill(state, SkillNames.base_skill_charisma, player, 6))
        set_rule(world.get_location(AspirationNames.base_aspiration_serial_romantic, player),
                 lambda state: has_skill(state, SkillNames.base_skill_charisma, player, 6))
    elif options.goal.value == options.goal.option_freelance_botanist:
        set_rule(world.get_location(AspirationNames.base_aspiration_garden_variety, player),
                 lambda state: has_skill(state, SkillNames.base_skill_gardening, player, 4))
        set_rule(world.get_location(AspirationNames.base_aspiration_nature_nurturer, player),
                 lambda state: has_skill(state, SkillNames.base_skill_gardening, player, 6))
        set_rule(world.get_location(AspirationNames.base_aspiration_freelance_botanist, player),
                 lambda state: has_skill(state, SkillNames.base_skill_gardening, player, 10))
    elif options.goal.value == options.goal.option_angling_ace:
        set_rule(world.get_location(AspirationNames.base_aspiration_hooked, player),
                 lambda state: has_skill(state, SkillNames.base_skill_fishing, player, 4))
        set_rule(world.get_location(AspirationNames.base_aspiration_reel_smart, player),
                 lambda state: has_skill(state, SkillNames.base_skill_fishing, player, 6))
        set_rule(world.get_location(AspirationNames.base_aspiration_angling_ace, player),
                 lambda state: has_skill(state, SkillNames.base_skill_fishing, player, 10))
    elif options.goal.value == options.goal.option_joke_star:
        set_rule(world.get_location(AspirationNames.base_aspiration_practical_joker, player),
                 lambda state: has_skill(state, SkillNames.base_skill_comedy, player, 3))
        set_rule(world.get_location(AspirationNames.base_aspiration_standup_startup, player),
                 lambda state: has_skill(state, SkillNames.base_skill_comedy, player, 3))
        set_rule(world.get_location(AspirationNames.base_aspiration_funny, player),
                 lambda state: has_skill(state, SkillNames.base_skill_comedy, player, 6)
                               and (has_skill(state, SkillNames.base_skill_guitar, player, 3)
                                    or has_skill(state, SkillNames.base_skill_violin, player, 3)))
        set_rule(world.get_location(AspirationNames.base_aspiration_joke_star, player),
                 lambda state: has_skill(state, SkillNames.base_skill_comedy, player, 10)
                               and (has_skill(state, SkillNames.base_skill_guitar, player, 3)
                                    or has_skill(state, SkillNames.base_skill_violin, player, 3)))
    elif options.goal.value == options.goal.option_friend_of_the_world:
        set_rule(world.get_location(AspirationNames.base_aspiration_well_liked, player),
                 lambda state: has_skill(state, SkillNames.base_skill_charisma, player, 4))
        set_rule(world.get_location(AspirationNames.base_aspiration_super_friend, player),
                 lambda state: has_skill(state, SkillNames.base_skill_charisma, player, 6))
        set_rule(world.get_location(AspirationNames.base_aspiration_friend_of_the_world, player),
                 lambda state: has_skill(state, SkillNames.base_skill_charisma, player, 10))
    elif options.goal.value == options.goal.option_neighborly_advisor:
        set_rule(world.get_location(AspirationNames.base_aspiration_neighborly_advisor, player),
                 lambda state: has_skill(state, SkillNames.base_skill_charisma, player, 7))

    # Skillchecks

    skills = {
        SkillNames.base_skill_comedy: (3, 11),
        SkillNames.base_skill_charisma: (3, 11),
        SkillNames.base_skill_logic: (3, 11),
        SkillNames.base_skill_fitness: (3, 11),
        SkillNames.base_skill_writing: (3, 11),
        SkillNames.base_skill_fishing: (3, 11),
        SkillNames.base_skill_gardening: (3, 11),
        SkillNames.base_skill_video_gaming: (3, 11),
        SkillNames.base_skill_programming: (3, 11),
        SkillNames.base_skill_handiness: (3, 11),
        SkillNames.base_skill_cooking: (3, 11),
        SkillNames.base_skill_mixology: (3, 11),
        SkillNames.base_skill_gourmet: (3, 11),
        SkillNames.base_skill_mischief: (3, 11),
        SkillNames.base_skill_piano: (3, 11),
        SkillNames.base_skill_violin: (3, 11),
        SkillNames.base_skill_guitar: (3, 11),
        SkillNames.base_skill_painting: (3, 11),
        SkillNames.base_skill_photography: (3, 6),
        SkillNames.base_skill_rocket_science: (3, 11),
    }

    if ExpansionNames.get_to_work in options.expansion_packs.value:
        skills[SkillNames.gtw_baking_skill] = (3, 11)
    if ExpansionNames.get_together in options.expansion_packs.value:
        skills[SkillNames.gt_dancing_skill] = (3, 6)
        skills[SkillNames.gt_djmixing_skill] = (3, 11)
    if ExpansionNames.city_living in options.expansion_packs.value:
        skills[SkillNames.cl_singing_skill] = (3, 11)
    if ExpansionNames.cats_and_dogs in options.expansion_packs.value:
        skills[SkillNames.cnd_pettraining_skill] = (3, 6)
        skills[SkillNames.cnd_veterinarian_skill] = (3,11)
    if ExpansionNames.seasons in options.expansion_packs.value:
        skills[SkillNames.se_flowerarranging_skill] = (3, 11)
    if ExpansionNames.get_famous in options.expansion_packs.value:
        skills[SkillNames.gf_acting_skill] = (3, 11)
        skills[SkillNames.gf_mediaproduction_skill] = (3, 6)
    if ExpansionNames.discover_university in options.expansion_packs.value:
        skills[SkillNames.du_robotics_skill] = (3, 11)
        skills[SkillNames.du_researchanddebate_skill] = (3, 11)
    if ExpansionNames.eco_lifestyle in options.expansion_packs.value:
        skills[SkillNames.el_fabrication_skill] = (3, 11)
        skills[SkillNames.el_juicefizzing_skill] = (3, 6)
    if ExpansionNames.snowy_escape in options.expansion_packs.value:
        skills[SkillNames.sy_rock_climbing_skill] = (3, 11)
        skills[SkillNames.sy_skiing_skill] = (3, 11)
        skills[SkillNames.sy_snowboarding_skill] = (3, 11)
    if ExpansionNames.cottage_living in options.expansion_packs.value:
        skills[SkillNames.cgl_cross_stitch_skill] = (3, 6)
    if ExpansionNames.high_school_years in options.expansion_packs.value:
        skills[SkillNames.hsy_entrepreneur_skill] = (3, 6)
    if ExpansionNames.horse_ranch in options.expansion_packs.value:
        skills[SkillNames.hr_horse_riding_skill] = (3, 11)
        skills[SkillNames.hr_nectar_making_skill] = (3, 6)
    if ExpansionNames.lovestruck in options.expansion_packs.value:
        skills[SkillNames.lv_romance_skill] = (3, 11)
    if ExpansionNames.life_and_death in options.expansion_packs.value:
        skills[SkillNames.lnd_thanatology_skill] = (3, 6)
    if ExpansionNames.business_and_hobbies in options.expansion_packs.value:
        skills[SkillNames.bnh_pottery_skill] = (3, 11)
        skills[SkillNames.bnh_tattooing_skill] = (3, 11)
    if ExpansionNames.enchanted_by_nature in options.expansion_packs.value:
        skills[SkillNames.ebn_apothecary_skill] = (3, 11)
        skills[SkillNames.ebn_natural_living_skill] = (3, 11)
    if GamePackNames.outdoor_retreat in options.game_packs.value:
        skills[SkillNames.or_herbalism_skill] = (3, 11)
    if GamePackNames.spa_day in options.game_packs.value:
        skills[SkillNames.sd_wellness_skill] = (3, 11)
    if GamePackNames.vampires in options.game_packs.value:
        skills[SkillNames.vamp_pipeorgan_skill] = (3, 11)
        skills[SkillNames.vamp_vampirelore_skill] = (3, 16)
    if GamePackNames.parenthood in options.game_packs.value:
        skills[SkillNames.ph_parenting_skill] = (3, 11)
    if GamePackNames.jungle_adventure in options.game_packs.value:
        skills[SkillNames.ja_archaeology_skill] = (3, 11)
        skills[SkillNames.ja_sevadoradianculture_skill] = (3, 6)
    if StuffNames.bowling_night in options.stuff_packs.value:
        skills[SkillNames.bns_bowling_skill] = (3, 6)
    if StuffNames.nifty_knitting in options.stuff_packs.value:
        skills[SkillNames.nk_knitting_skill] = (3, 11)
    if StuffNames.paranormal in options.stuff_packs.value:
        skills[SkillNames.pa_medium_skill] = (3, 6)
    if StuffNames.crystal_creations in options.stuff_packs.value:
        skills[SkillNames.cc_gemology_skill] = (3, 11)

    for skill, (low, high) in skills.items():
        for level in range(low, high):
            # print(skill, level)
            set_rule(world.get_location(f"{skill} {level}", player),
                     lambda state, s=skill, l=level: has_skill(state, s, player, l))

    if options.goal.value == options.goal.option_bodybuilder:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_bodybuilder, player), player=player)
    elif options.goal.value == options.goal.option_painter_extraordinaire:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_painter_extraordinaire, player), player=player)
    elif options.goal.value == options.goal.option_bestselling_author:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_bestselling_author, player), player=player)
    elif options.goal.value == options.goal.option_musical_genius:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_musical_genius, player), player=player)
    elif options.goal.value == options.goal.option_public_enemy:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_public_enemy, player), player=player)
    elif options.goal.value == options.goal.option_chief_of_mischief:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_chief_of_mischief, player), player=player)
    elif options.goal.value == options.goal.option_master_chef:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_master_chef, player), player=player)
    elif options.goal.value == options.goal.option_master_mixologist:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_master_mixologist, player), player=player)
    elif options.goal.value == options.goal.option_renaissance_sim:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_renaissance_sim, player), player=player)
    elif options.goal.value == options.goal.option_nerd_brain:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_nerd_brain, player), player=player)
    elif options.goal.value == options.goal.option_computer_whiz:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_computer_whiz, player), player=player)
    elif options.goal.value == options.goal.option_serial_romantic:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_serial_romantic, player), player=player)
    elif options.goal.value == options.goal.option_freelance_botanist:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_freelance_botanist, player), player=player)
    elif options.goal.value == options.goal.option_the_curator:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_the_curator, player), player=player)
    elif options.goal.value == options.goal.option_angling_ace:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_angling_ace, player), player=player)
    elif options.goal.value == options.goal.option_joke_star:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_joke_star, player), player=player)
    elif options.goal.value == options.goal.option_friend_of_the_world:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_friend_of_the_world, player), player=player)
    elif options.goal.value == options.goal.option_neighborly_advisor:
        world.completion_condition[player] = lambda state: state.can_reach(
            world.get_location(AspirationNames.base_aspiration_neighborly_advisor, player), player=player)


def count_skills_over(threshold: int, state, player) -> int:
    total_count = 0

    if state.has(SkillNames.base_skill_charisma, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_fitness, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_mischief, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_logic, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_cooking, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_mixology, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_comedy, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_writing, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_fishing, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_gardening, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_video_gaming, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_programming, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_photography, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_handiness, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_piano, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_violin, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_guitar, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_painting, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_rocket_science, player, count=threshold):
        total_count += 1
    if state.has(SkillNames.base_skill_gourmet, player, count=threshold):
        total_count += 1

    return total_count

def has_skill(state: CollectionState, skill: str, player: int, skill_level: int) -> bool:
    # determines how many skill items are required based on the skill level passed into the function
    skills_required: int = skill_level - 2
    return state.has(skill, player, skills_required)
