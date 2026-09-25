from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

from typing_extensions import override

import rule_builder.rules
from BaseClasses import CollectionState
from NetUtils import JSONMessagePart
from rule_builder.rules import CanReachLocation, Has, Rule

from .Items import skills_table
from .Names import AspirationNames, CareerNames, EventNames, SkillNames
from .Names.DLC import ExpansionNames, GamePackNames, StuffNames
from .Options import AspirationGoal, Sims4Options

if TYPE_CHECKING:
    from . import Sims4World

def has_skill(skill: str, skill_level: int) -> Has:
    """
    Design Decision:
    Skill items in the pool represent progression milestones beyond level 2.
    Therefore, level N requires (N - 2) skill items.
    Example: Level 3 requires 1 item, Level 10 requires 8 items.
    """
    # determines how many skill items are required based on the skill level passed into the function
    skills_required: int = skill_level - 2
    return Has(skill, skills_required)

def has_multiple_skills(skills_and_levels: dict[str, int]) -> rule_builder.rules.And:
    skills = list(skills_and_levels.items())
    return rule_builder.rules.And(*(has_skill(skill, level) for skill, level in skills))


@dataclasses.dataclass()
class JackOfNTradesRule(Rule, game="The Sims 4"):
    skill_threshold: int
    skill_count: int

    @override
    def _instantiate(self, world: rule_builder.rules.World) -> Rule.Resolved:
        return self.Resolved(skill_threshold=self.skill_threshold, skill_count=self.skill_count, player=world.player)

    class Resolved(Rule.Resolved):
        skill_threshold: int
        skill_count: int

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            count = 0
            for skill in skills_table.values():
                if state.has(skill["name"], self.player, self.skill_threshold):
                    count += 1
            return count >= self.skill_count

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            text: list[JSONMessagePart] = [
                {"type": "text", "text": "Have at least "},
                {"type": "text", "text": str(self.skill_count)},
                {"type": "text", "text": " skills at level "},
                {"type": "text", "text": str(self.skill_threshold)},
                {"type": "text", "text": "."},
            ]
            if state is not None:
                count = 0
                for skill in skills_table.values():
                    if state.has(skill["name"], self.player, self.skill_threshold):
                        count += 1
                text.append({"type": "text", "text": f" (Currently have {count})",
                             "color": "green" if count >= self.skill_count else "red"})
            return text


def set_rules(world: Sims4World, player: int, options: Sims4Options) -> None:
    # TODO: Part Time Jobs?
    set_career_rules(world, options)
    set_aspiration_rules(world, player, options)
    set_skill_rules(world, options)
    set_completion_condition(world, player, options)

# TODO: use events for the completion condition in order to facilitate easier goal stuff, and presence in spoiler (also permits future goals to be more dynamic)
def set_completion_condition(world: Sims4World, player: int, options: Sims4Options):
    goal = options.goal
    goal_value = goal.value

    if goal_value == goal.option_bodybuilder:
        world.set_completion_rule(Has(EventNames.bodybuilder_item))
    elif goal_value == goal.option_painter_extraordinaire:
        world.set_completion_rule(Has(EventNames.painter_extraordinaire_item))
    elif goal_value == goal.option_bestselling_author:
        world.set_completion_rule(Has(EventNames.bestselling_author_item))
    elif goal_value == goal.option_musical_genius:
        world.set_completion_rule(Has(EventNames.musical_genius_item))
    elif goal_value == goal.option_public_enemy:
        world.set_completion_rule(Has(EventNames.public_enemy_item))
    elif goal_value == goal.option_chief_of_mischief:
        world.set_completion_rule(Has(EventNames.chief_of_mischief_item))
    elif goal_value == goal.option_master_chef:
        world.set_completion_rule(Has(EventNames.master_chef_item))
    elif goal_value == goal.option_master_mixologist:
        world.set_completion_rule(Has(EventNames.master_mixologist_item))
    elif goal_value == goal.option_renaissance_sim:
        world.set_completion_rule(Has(EventNames.renaissance_sim_item))
    elif goal_value == goal.option_nerd_brain:
        world.set_completion_rule(Has(EventNames.nerd_brain_item))
    elif goal_value == goal.option_computer_whiz:
        world.set_completion_rule(Has(EventNames.computer_whiz_item))
    elif goal_value == goal.option_serial_romantic:
        world.set_completion_rule(Has(EventNames.serial_romantic_item))
    elif goal_value == goal.option_freelance_botanist:
        world.set_completion_rule(Has(EventNames.freelance_botanist_item))
    elif goal_value == goal.option_the_curator:
        world.set_completion_rule(Has(EventNames.the_curator_item))
    elif goal_value == goal.option_angling_ace:
        world.set_completion_rule(Has(EventNames.angling_ace_item))
    elif goal_value == goal.option_joke_star:
        world.set_completion_rule(Has(EventNames.joke_star_item))
    elif goal_value == goal.option_friend_of_the_world:
        world.set_completion_rule(Has(EventNames.friend_of_the_world_item))
    elif goal_value == goal.option_neighborly_advisor:
        world.set_completion_rule(Has(EventNames.neighborly_advisor_item))

def set_skill_rules(world: Sims4World, options: Sims4Options):
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

    eps = options.expansion_packs.value
    gps = options.game_packs.value
    sps = options.stuff_packs.value

    if ExpansionNames.get_to_work in eps:
        skills[SkillNames.gtw_baking_skill] = (3, 11)
    if ExpansionNames.get_together in eps:
        skills[SkillNames.gt_dancing_skill] = (3, 6)
        skills[SkillNames.gt_djmixing_skill] = (3, 11)
    if ExpansionNames.city_living in eps:
        skills[SkillNames.cl_singing_skill] = (3, 11)
    if ExpansionNames.cats_and_dogs in eps:
        skills[SkillNames.cnd_pettraining_skill] = (3, 6)
        skills[SkillNames.cnd_veterinarian_skill] = (3, 11)
    if ExpansionNames.seasons in eps:
        skills[SkillNames.se_flowerarranging_skill] = (3, 11)
    if ExpansionNames.get_famous in eps:
        skills[SkillNames.gf_acting_skill] = (3, 11)
        skills[SkillNames.gf_mediaproduction_skill] = (3, 6)
    if ExpansionNames.discover_university in eps:
        skills[SkillNames.du_robotics_skill] = (3, 11)
        skills[SkillNames.du_researchanddebate_skill] = (3, 11)
    if ExpansionNames.eco_lifestyle in eps:
        skills[SkillNames.el_fabrication_skill] = (3, 11)
        skills[SkillNames.el_juicefizzing_skill] = (3, 6)
    if ExpansionNames.snowy_escape in eps:
        skills[SkillNames.sy_rock_climbing_skill] = (3, 11)
        skills[SkillNames.sy_skiing_skill] = (3, 11)
        skills[SkillNames.sy_snowboarding_skill] = (3, 11)
    if ExpansionNames.cottage_living in eps:
        skills[SkillNames.cgl_cross_stitch_skill] = (3, 6)
    if ExpansionNames.high_school_years in eps:
        skills[SkillNames.hsy_entrepreneur_skill] = (3, 6)
    if ExpansionNames.horse_ranch in eps:
        skills[SkillNames.hr_horse_riding_skill] = (3, 11)
        skills[SkillNames.hr_nectar_making_skill] = (3, 6)
    if ExpansionNames.lovestruck in eps:
        skills[SkillNames.lv_romance_skill] = (3, 11)
    if ExpansionNames.life_and_death in eps:
        skills[SkillNames.lnd_thanatology_skill] = (3, 6)
    if ExpansionNames.business_and_hobbies in eps:
        skills[SkillNames.bnh_pottery_skill] = (3, 11)
        skills[SkillNames.bnh_tattooing_skill] = (3, 11)
    if ExpansionNames.enchanted_by_nature in eps:
        skills[SkillNames.ebn_apothecary_skill] = (3, 11)
        skills[SkillNames.ebn_natural_living_skill] = (3, 11)
    if GamePackNames.outdoor_retreat in gps:
        skills[SkillNames.or_herbalism_skill] = (3, 11)
    if GamePackNames.spa_day in gps:
        skills[SkillNames.sd_wellness_skill] = (3, 11)
    if GamePackNames.vampires in gps:
        skills[SkillNames.vamp_pipeorgan_skill] = (3, 11)
        skills[SkillNames.vamp_vampirelore_skill] = (3, 16)
    if GamePackNames.parenthood in gps:
        skills[SkillNames.ph_parenting_skill] = (3, 11)
    if GamePackNames.jungle_adventure in gps:
        skills[SkillNames.ja_archaeology_skill] = (3, 11)
        skills[SkillNames.ja_sevadoradianculture_skill] = (3, 6)
    if StuffNames.bowling_night in sps:
        skills[SkillNames.bns_bowling_skill] = (3, 6)
    if StuffNames.nifty_knitting in sps:
        skills[SkillNames.nk_knitting_skill] = (3, 11)
    if StuffNames.paranormal in sps:
        skills[SkillNames.pa_medium_skill] = (3, 6)
    if StuffNames.crystal_creations in sps:
        skills[SkillNames.cc_gemology_skill] = (3, 11)

    for skill, (low, high) in skills.items():
        for level in range(low, high):
            # print(skill, level)
            world.set_rule(world.get_location(f"{skill} {level}"), has_skill(skill, level))

def _bodybuilder(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_exercise_demon),
             has_skill(SkillNames.base_skill_fitness, 4))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_fit_to_a_t),
             has_skill(SkillNames.base_skill_fitness, 6))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_bodybuilder),
             has_skill(SkillNames.base_skill_fitness, 10))
    world.set_rule(world.get_location(EventNames.bodybuilder),
             CanReachLocation(AspirationNames.base_aspiration_bodybuilder))

def _painter_extraordinaire(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_fine_artist),
             has_skill(SkillNames.base_skill_painting, 4))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_brushing_with_greatness),
             has_skill(SkillNames.base_skill_painting, 6))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_painter_extraordinaire),
             has_skill(SkillNames.base_skill_painting, 10))
    world.set_rule(world.get_location(EventNames.painter_extraordinaire),
             CanReachLocation(AspirationNames.base_aspiration_painter_extraordinaire))

def _bestselling_author(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_competent_wordsmith),
             has_skill(SkillNames.base_skill_writing, 4))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_novelest_novelist),
             has_skill(SkillNames.base_skill_writing, 6))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_bestselling_author),
             has_skill(SkillNames.base_skill_writing, 10))
    world.set_rule(world.get_location(EventNames.bestselling_author),
             CanReachLocation(AspirationNames.base_aspiration_bestselling_author))

def _musical_genius(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_fine_tuned),
             has_skill(SkillNames.base_skill_guitar, 4)
                           | has_skill(SkillNames.base_skill_violin, 4)
                           | has_skill(SkillNames.base_skill_piano, 4))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_harmonious),
             has_skill(SkillNames.base_skill_guitar, 8)
                           | has_skill(SkillNames.base_skill_violin, 8)
                           | has_skill(SkillNames.base_skill_piano, 8))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_musical_genius),
             has_skill(SkillNames.base_skill_guitar, 10)
                           | has_skill(SkillNames.base_skill_violin, 10)
                           | has_skill(SkillNames.base_skill_piano, 10))
    world.set_rule(world.get_location(EventNames.musical_genius),
             CanReachLocation(AspirationNames.base_aspiration_musical_genius))

def _public_enemy(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_criminal_mind),
             has_skill(SkillNames.base_skill_mischief, 3))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_public_enemy),
             has_skill(SkillNames.base_skill_mischief, 8)
                           & has_skill(SkillNames.base_skill_programming, 4))
    world.set_rule(world.get_location(EventNames.public_enemy),
             CanReachLocation(AspirationNames.base_aspiration_public_enemy))

def _chief_of_mischief(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_artful_trickster),
             has_skill(SkillNames.base_skill_mischief, 3))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_professional_prankster),
             has_skill(SkillNames.base_skill_mischief, 6))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_chief_of_mischief),
             has_skill(SkillNames.base_skill_mischief, 10))
    world.set_rule(world.get_location(EventNames.chief_of_mischief),
             CanReachLocation(AspirationNames.base_aspiration_chief_of_mischief))

def _master_chef(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_captain_cook),
             has_skill(SkillNames.base_skill_cooking, 5))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_culinary_artist),
             has_skill(SkillNames.base_skill_cooking, 5))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_master_chef),
             (has_skill(SkillNames.base_skill_gourmet, 6)
                            & has_skill(SkillNames.base_skill_cooking, 8))
                           | (has_skill(SkillNames.base_skill_gourmet, 5)
                               & has_skill(SkillNames.base_skill_mixology, 7)
                               & has_skill(SkillNames.base_skill_charisma, 4)))
    world.set_rule(world.get_location(EventNames.master_chef),
             CanReachLocation(AspirationNames.base_aspiration_master_chef))

def _master_mixologist(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_electric_mixer),
             has_skill(SkillNames.base_skill_mixology, 4))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_beverage_boss),
             has_skill(SkillNames.base_skill_mixology, 7)
                           & has_skill(SkillNames.base_skill_cooking, 4))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_master_mixologist),
             has_skill(SkillNames.base_skill_mixology, 10)
                           & has_skill(SkillNames.base_skill_cooking, 4))
    world.set_rule(world.get_location(EventNames.master_mixologist),
             CanReachLocation(AspirationNames.base_aspiration_master_mixologist))


def _renaissance_sim(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_prudent_student),
             has_skill(SkillNames.base_skill_logic, 1))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_jack_of_some_trades),
             JackOfNTradesRule(2, 4))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_pantologist),
             JackOfNTradesRule(3, 5))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_renaissance_sim),
             JackOfNTradesRule(6, 6))
    world.set_rule(world.get_location(EventNames.renaissance_sim),
             CanReachLocation(AspirationNames.base_aspiration_renaissance_sim))

def _nerd_brain(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_prudent_student),
             has_skill(SkillNames.base_skill_logic, 3))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_erudite),
             has_skill(SkillNames.base_skill_logic, 6))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_rocket_scientist),
             has_skill(SkillNames.base_skill_handiness, 5))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_nerd_brain),
             has_skill(SkillNames.base_skill_logic, 10)
                           & has_skill(SkillNames.base_skill_handiness, 5))
    world.set_rule(world.get_location(EventNames.nerd_brain),
             CanReachLocation(AspirationNames.base_aspiration_nerd_brain))

def _computer_whiz(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_technically_adept),
             has_skill(SkillNames.base_skill_programming, 3))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_computer_geek),
             has_skill(SkillNames.base_skill_programming, 7))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_computer_whiz),
             has_skill(SkillNames.base_skill_programming, 7)
                           & has_skill(SkillNames.base_skill_video_gaming, 4))
    world.set_rule(world.get_location(EventNames.computer_whiz),
             CanReachLocation(AspirationNames.base_aspiration_computer_whiz))

def _serial_romantic(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_up_to_date),
             has_skill(SkillNames.base_skill_charisma, 4))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_romance_juggler),
             has_skill(SkillNames.base_skill_charisma, 6))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_serial_romantic),
             has_skill(SkillNames.base_skill_charisma, 6))
    world.set_rule(world.get_location(EventNames.serial_romantic),
             CanReachLocation(AspirationNames.base_aspiration_serial_romantic))

def _freelance_botanist(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_garden_variety),
             has_skill(SkillNames.base_skill_gardening, 4))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_nature_nurturer),
             has_skill(SkillNames.base_skill_gardening, 6))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_freelance_botanist),
             has_skill(SkillNames.base_skill_gardening, 10))
    world.set_rule(world.get_location(EventNames.freelance_botanist),
             CanReachLocation(AspirationNames.base_aspiration_freelance_botanist))

def _angling_ace(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_hooked),
             has_skill(SkillNames.base_skill_fishing, 4))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_reel_smart),
             has_skill(SkillNames.base_skill_fishing, 6))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_angling_ace),
             has_skill(SkillNames.base_skill_fishing, 10))
    world.set_rule(world.get_location(EventNames.angling_ace),
             CanReachLocation(AspirationNames.base_aspiration_angling_ace))

def _joke_star(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_practical_joker),
             has_skill(SkillNames.base_skill_comedy, 3))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_standup_startup),
             has_skill(SkillNames.base_skill_comedy, 3))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_funny),
             has_skill(SkillNames.base_skill_comedy, 6) &
             (has_skill(SkillNames.base_skill_guitar, 3) | has_skill(SkillNames.base_skill_violin, 3)))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_joke_star),
             has_skill(SkillNames.base_skill_comedy, 10) &
             (has_skill(SkillNames.base_skill_guitar, 3)
              | has_skill(SkillNames.base_skill_violin, 3)))
    world.set_rule(world.get_location(EventNames.joke_star),
             CanReachLocation(AspirationNames.base_aspiration_joke_star))

def _friend_of_the_world(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_well_liked),
             has_skill(SkillNames.base_skill_charisma, 4))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_super_friend),
             has_skill(SkillNames.base_skill_charisma, 6))
    world.set_rule(world.get_location(AspirationNames.base_aspiration_friend_of_the_world),
             has_skill(SkillNames.base_skill_charisma, 10))
    world.set_rule(world.get_location(EventNames.friend_of_the_world),
             CanReachLocation(AspirationNames.base_aspiration_friend_of_the_world))

def _neighborly_advisor(world: Sims4World, player: int):
    world.set_rule(world.get_location(AspirationNames.base_aspiration_neighborly_advisor),
             has_skill(SkillNames.base_skill_charisma, 7))
    world.set_rule(world.get_location(EventNames.neighborly_advisor),
             CanReachLocation(AspirationNames.base_aspiration_neighborly_advisor))

ASPIRATION_RULES = {
        AspirationGoal.option_bodybuilder: _bodybuilder,
        AspirationGoal.option_painter_extraordinaire: _painter_extraordinaire,
        AspirationGoal.option_bestselling_author: _bestselling_author,
        AspirationGoal.option_musical_genius: _musical_genius,
        AspirationGoal.option_public_enemy: _public_enemy,
        AspirationGoal.option_chief_of_mischief: _chief_of_mischief,
        AspirationGoal.option_master_chef: _master_chef,
        AspirationGoal.option_master_mixologist: _master_mixologist,
        AspirationGoal.option_renaissance_sim: _renaissance_sim,
        AspirationGoal.option_nerd_brain: _nerd_brain,
        AspirationGoal.option_computer_whiz: _computer_whiz,
        AspirationGoal.option_serial_romantic: _serial_romantic,
        AspirationGoal.option_freelance_botanist: _freelance_botanist,
        AspirationGoal.option_angling_ace: _angling_ace,
        AspirationGoal.option_joke_star: _joke_star,
        AspirationGoal.option_friend_of_the_world: _friend_of_the_world,
        AspirationGoal.option_neighborly_advisor: _neighborly_advisor,
    }

def set_aspiration_rules(world: Sims4World, player: int, options: Sims4Options):
    handler = ASPIRATION_RULES.get(options.goal)
    if handler:
        handler(world, player)


_career_athlete = {
    CareerNames.base_career_athlete_3: {
        SkillNames.base_skill_charisma: 2,
        SkillNames.base_skill_fitness: 2,
    },
    CareerNames.base_career_athlete_4: {
        SkillNames.base_skill_charisma: 3,
        SkillNames.base_skill_fitness: 3,
    },
    CareerNames.base_career_athlete_5A: {
        SkillNames.base_skill_charisma: 4,
        SkillNames.base_skill_fitness: 4,
    },
    CareerNames.base_career_athlete_6A: {
        SkillNames.base_skill_charisma: 4,
        SkillNames.base_skill_fitness: 5,
    },
    CareerNames.base_career_athlete_7A: {
        SkillNames.base_skill_charisma: 4,
        SkillNames.base_skill_fitness: 6,
    },
    CareerNames.base_career_athlete_8A: {
        SkillNames.base_skill_charisma: 5,
        SkillNames.base_skill_fitness: 8,
    },
    CareerNames.base_career_athlete_9A: {
        SkillNames.base_skill_charisma: 6,
        SkillNames.base_skill_fitness: 9,
    },
    CareerNames.base_career_athlete_10A: {
        SkillNames.base_skill_charisma: 8,
        SkillNames.base_skill_fitness: 10,
    },
    CareerNames.base_career_athlete_5B: {
        SkillNames.base_skill_charisma: 4,
        SkillNames.base_skill_fitness: 4,
    },
    CareerNames.base_career_athlete_6B: {
        SkillNames.base_skill_charisma: 5,
        SkillNames.base_skill_fitness: 8,
    },
    CareerNames.base_career_athlete_7B: {
        SkillNames.base_skill_charisma: 5,
        SkillNames.base_skill_fitness: 9,
    },
    CareerNames.base_career_athlete_8B: {
        SkillNames.base_skill_charisma: 6,
        SkillNames.base_skill_fitness: 10,
    },
    CareerNames.base_career_athlete_9B: {
        SkillNames.base_skill_charisma: 7,
        SkillNames.base_skill_fitness: 10,
    },
    CareerNames.base_career_athlete_10B: {
        SkillNames.base_skill_charisma: 8,
        SkillNames.base_skill_fitness: 10,
    },
}

_career_astronaut = {
    CareerNames.base_career_astronaut_4:{
             SkillNames.base_skill_logic: 3,
            SkillNames.base_skill_fitness: 2,
    },
    CareerNames.base_career_astronaut_5: {
        SkillNames.base_skill_logic: 4,
        SkillNames.base_skill_fitness: 3,
    },
    CareerNames.base_career_astronaut_6: {
        SkillNames.base_skill_logic: 5,
        SkillNames.base_skill_fitness: 4,
    },
    CareerNames.base_career_astronaut_7: {
        SkillNames.base_skill_logic: 5,
        SkillNames.base_skill_fitness: 6,
    },
    CareerNames.base_career_astronaut_8A: {
        SkillNames.base_skill_logic: 6,
        SkillNames.base_skill_fitness: 7,
    },
    CareerNames.base_career_astronaut_8B: {
        SkillNames.base_skill_logic: 6,
        SkillNames.base_skill_fitness: 7,
    },
    CareerNames.base_career_astronaut_9A: {
        SkillNames.base_skill_rocket_science: 2,
        SkillNames.base_skill_fitness: 8,
    },
    CareerNames.base_career_astronaut_10A: {
        SkillNames.base_skill_rocket_science: 4,
        SkillNames.base_skill_fitness: 10,
    },
    CareerNames.base_career_astronaut_9B: {
        SkillNames.base_skill_rocket_science: 2,
        SkillNames.base_skill_fitness: 8,
    },
    CareerNames.base_career_astronaut_10B: {
        SkillNames.base_skill_rocket_science: 4,
        SkillNames.base_skill_fitness: 10,
    },
}

_career_business = {
    CareerNames.base_career_business_3: {
        SkillNames.base_skill_charisma: 2,
    },
    CareerNames.base_career_business_4: {
        SkillNames.base_skill_charisma: 2,
        SkillNames.base_skill_logic: 2,
    },
    CareerNames.base_career_business_5: {
        SkillNames.base_skill_charisma: 3,
        SkillNames.base_skill_logic: 2,
    },
    CareerNames.base_career_business_6: {
        SkillNames.base_skill_charisma: 4,
        SkillNames.base_skill_logic: 2,
    },
    CareerNames.base_career_business_7A: {
        SkillNames.base_skill_charisma: 4,
        SkillNames.base_skill_logic: 4,
    },
    CareerNames.base_career_business_7B: {
        SkillNames.base_skill_charisma: 4,
        SkillNames.base_skill_logic: 4,
    },
    CareerNames.base_career_business_8A: {
        SkillNames.base_skill_charisma: 6,
        SkillNames.base_skill_logic: 5,
    },
    CareerNames.base_career_business_9A: {
        SkillNames.base_skill_charisma: 8,
        SkillNames.base_skill_logic: 6,
    },
    CareerNames.base_career_business_10A: {
        SkillNames.base_skill_charisma: 10,
        SkillNames.base_skill_logic: 8,
    },
    CareerNames.base_career_business_8B: {
        SkillNames.base_skill_charisma: 5,
        SkillNames.base_skill_logic: 6,
    },
    CareerNames.base_career_business_9B: {
        SkillNames.base_skill_charisma: 6,
        SkillNames.base_skill_logic: 8,
    },
    CareerNames.base_career_business_10B: {
        SkillNames.base_skill_charisma: 8,
        SkillNames.base_skill_logic: 10,
    },
}

_career_criminal = {
    CareerNames.base_career_criminal_3: {
        SkillNames.base_skill_mischief: 2,
    },
    CareerNames.base_career_criminal_4: {
        SkillNames.base_skill_mischief: 3,
    },
    CareerNames.base_career_criminal_5: {
        SkillNames.base_skill_mischief: 5,
    },
    CareerNames.base_career_criminal_6A: {
        SkillNames.base_skill_mischief: 6,
    },
    CareerNames.base_career_criminal_6B: {
        SkillNames.base_skill_mischief: 6,
    },
    CareerNames.base_career_criminal_7A: {
        SkillNames.base_skill_mischief: 7,
    },
    CareerNames.base_career_criminal_8A: {
        SkillNames.base_skill_mischief: 8,
        SkillNames.base_skill_handiness: 2,
    },
    CareerNames.base_career_criminal_9A: {
        SkillNames.base_skill_mischief: 9,
        SkillNames.base_skill_handiness: 4,
    },
    CareerNames.base_career_criminal_10A: {
        SkillNames.base_skill_mischief: 10,
        SkillNames.base_skill_handiness: 6,
    },
    CareerNames.base_career_criminal_7B: {
        SkillNames.base_skill_mischief: 7,
        SkillNames.base_skill_programming: 2,
    },
    CareerNames.base_career_criminal_8B: {
        SkillNames.base_skill_mischief: 8,
        SkillNames.base_skill_programming: 4,
    },
    CareerNames.base_career_criminal_9B: {
        SkillNames.base_skill_mischief: 9,
        SkillNames.base_skill_programming: 6,
    },
    CareerNames.base_career_criminal_10B: {
        SkillNames.base_skill_mischief: 10,
        SkillNames.base_skill_programming: 8,
    },
}

_career_culinary = {
    CareerNames.base_career_culinary_3: {
        SkillNames.base_skill_cooking: 2,
    },
    CareerNames.base_career_culinary_4: {
        SkillNames.base_skill_cooking: 2,
        SkillNames.base_skill_mixology: 2,
    },
    CareerNames.base_career_culinary_5: {
        SkillNames.base_skill_cooking: 3,
        SkillNames.base_skill_mixology: 3,
    },
    CareerNames.base_career_culinary_6A: {
        SkillNames.base_skill_cooking: 4,
        SkillNames.base_skill_mixology: 4,
    },
    CareerNames.base_career_culinary_6B: {
        SkillNames.base_skill_cooking: 4,
        SkillNames.base_skill_mixology: 4,
    },
    CareerNames.base_career_culinary_7A: {
        SkillNames.base_skill_mixology: 4,
        SkillNames.base_skill_cooking: 5,
        SkillNames.base_skill_gourmet: 2,
    },
    CareerNames.base_career_culinary_8A: {
        SkillNames.base_skill_mixology: 4,
        SkillNames.base_skill_cooking: 7,
        SkillNames.base_skill_gourmet: 4,
    },
    CareerNames.base_career_culinary_9A: {
        SkillNames.base_skill_mixology: 4,
        SkillNames.base_skill_cooking: 8,
        SkillNames.base_skill_gourmet: 6,
    },
    CareerNames.base_career_culinary_10A: {
        SkillNames.base_skill_mixology: 4,
        SkillNames.base_skill_cooking: 10,
        SkillNames.base_skill_gourmet: 8,
    },
    CareerNames.base_career_culinary_7B: {
        SkillNames.base_skill_cooking: 4,
        SkillNames.base_skill_mixology: 5,
        SkillNames.base_skill_charisma: 2,
    },
    CareerNames.base_career_culinary_8B: {
        SkillNames.base_skill_cooking: 4,
        SkillNames.base_skill_mixology: 7,
        SkillNames.base_skill_charisma: 4,
    },
    CareerNames.base_career_culinary_9B: {
        SkillNames.base_skill_cooking: 4,
        SkillNames.base_skill_mixology: 8,
        SkillNames.base_skill_charisma: 6,
    },
    CareerNames.base_career_culinary_10B: {
        SkillNames.base_skill_cooking: 4,
        SkillNames.base_skill_mixology: 10,
        SkillNames.base_skill_charisma: 8,
    },
}

_career_entertainer = {
    CareerNames.base_career_entertainer_5A:
        (has_skill(SkillNames.base_skill_guitar, 3) | has_skill(SkillNames.base_skill_violin, 3))
        & has_skill(SkillNames.base_skill_comedy, 3),
    CareerNames.base_career_entertainer_5B:
        (has_skill(SkillNames.base_skill_guitar, 3) | has_skill(SkillNames.base_skill_violin, 3))
        & has_skill(SkillNames.base_skill_comedy, 3),
    CareerNames.base_career_entertainer_6A:
        (has_skill(SkillNames.base_skill_guitar, 4) | has_skill(SkillNames.base_skill_violin, 4))
        & has_skill(SkillNames.base_skill_piano, 2)
        & has_skill(SkillNames.base_skill_comedy, 3),
    CareerNames.base_career_entertainer_7A:
        (has_skill(SkillNames.base_skill_guitar, 5) | has_skill(SkillNames.base_skill_violin, 5))
        & has_skill(SkillNames.base_skill_piano, 4)
        & has_skill(SkillNames.base_skill_comedy, 3),
    CareerNames.base_career_entertainer_8A:
        (has_skill(SkillNames.base_skill_guitar, 6) | has_skill(SkillNames.base_skill_violin, 6))
        & has_skill(SkillNames.base_skill_piano, 6)
        & has_skill(SkillNames.base_skill_comedy, 3),
    CareerNames.base_career_entertainer_9A:
        (has_skill(SkillNames.base_skill_guitar, 7) | has_skill(SkillNames.base_skill_violin, 7))
        & has_skill(SkillNames.base_skill_piano, 8)
        & has_skill(SkillNames.base_skill_comedy, 3),
    CareerNames.base_career_entertainer_10A:
        (has_skill(SkillNames.base_skill_guitar, 8) | has_skill(SkillNames.base_skill_violin, 8))
        & has_skill(SkillNames.base_skill_piano, 10)
        & has_skill(SkillNames.base_skill_comedy, 3),
    CareerNames.base_career_entertainer_6B:
        (has_skill(SkillNames.base_skill_guitar, 3) | has_skill(SkillNames.base_skill_violin, 3))
        & has_skill(SkillNames.base_skill_comedy, 6),
    CareerNames.base_career_entertainer_7B:
        (has_skill(SkillNames.base_skill_guitar, 3) | has_skill(SkillNames.base_skill_violin, 3))
        & has_skill(SkillNames.base_skill_comedy, 7)
        & has_skill(SkillNames.base_skill_charisma, 2),
    CareerNames.base_career_entertainer_8B:
        (has_skill(SkillNames.base_skill_guitar, 3) | has_skill(SkillNames.base_skill_violin, 3))
        & has_skill(SkillNames.base_skill_comedy, 8)
        & has_skill(SkillNames.base_skill_charisma, 4),
    CareerNames.base_career_entertainer_9B:
        (has_skill(SkillNames.base_skill_guitar, 3) | has_skill(SkillNames.base_skill_violin, 3))
        & has_skill(SkillNames.base_skill_comedy, 9)
        & has_skill(SkillNames.base_skill_charisma, 6),
    CareerNames.base_career_entertainer_10B:
        (has_skill(SkillNames.base_skill_guitar, 3) | has_skill(SkillNames.base_skill_violin, 3))
        & has_skill(SkillNames.base_skill_comedy, 10)
        & has_skill(SkillNames.base_skill_charisma, 8),
}

_career_painter = {
    CareerNames.base_career_painter_4: {SkillNames.base_skill_painting: 4},
    CareerNames.base_career_painter_5: {SkillNames.base_skill_painting: 5},
    CareerNames.base_career_painter_6: {SkillNames.base_skill_painting: 6},
    CareerNames.base_career_painter_7A: {SkillNames.base_skill_painting: 7},
    CareerNames.base_career_painter_7B: {SkillNames.base_skill_painting: 7},
    CareerNames.base_career_painter_8A: {SkillNames.base_skill_painting: 8, SkillNames.base_skill_logic: 2},
    CareerNames.base_career_painter_9A: {SkillNames.base_skill_painting: 9, SkillNames.base_skill_logic: 4},
    CareerNames.base_career_painter_10A: {SkillNames.base_skill_painting: 10, SkillNames.base_skill_logic: 6},
    CareerNames.base_career_painter_8B: {SkillNames.base_skill_painting: 8, SkillNames.base_skill_charisma: 2},
    CareerNames.base_career_painter_9B: {SkillNames.base_skill_painting: 9, SkillNames.base_skill_charisma: 4},
    CareerNames.base_career_painter_10B: {SkillNames.base_skill_painting: 10, SkillNames.base_skill_charisma: 6},
}

_career_secret_agent = {
    CareerNames.base_career_secret_agent_4: {SkillNames.base_skill_logic: 2, SkillNames.base_skill_charisma: 2},
    CareerNames.base_career_secret_agent_5: {SkillNames.base_skill_logic: 3, SkillNames.base_skill_charisma: 3},
    CareerNames.base_career_secret_agent_6: {SkillNames.base_skill_logic: 5, SkillNames.base_skill_charisma: 5},
    CareerNames.base_career_secret_agent_7: {SkillNames.base_skill_logic: 5, SkillNames.base_skill_charisma: 5},
    CareerNames.base_career_secret_agent_8A: {SkillNames.base_skill_logic: 6, SkillNames.base_skill_charisma: 6},
    CareerNames.base_career_secret_agent_8B: {SkillNames.base_skill_logic: 6, SkillNames.base_skill_charisma: 6},
    CareerNames.base_career_secret_agent_9A: {SkillNames.base_skill_logic: 8, SkillNames.base_skill_charisma: 7},
    CareerNames.base_career_secret_agent_10A: {SkillNames.base_skill_logic: 10, SkillNames.base_skill_charisma: 8},
    CareerNames.base_career_secret_agent_9B: {SkillNames.base_skill_logic: 8, SkillNames.base_skill_charisma: 7},
    CareerNames.base_career_secret_agent_10B: {
        SkillNames.base_skill_logic: 10,
        SkillNames.base_skill_charisma: 8,
        SkillNames.base_skill_mischief: 4,
        },
}

_career_style_influencer = {
    CareerNames.base_career_style_influencer_3: {SkillNames.base_skill_writing: 2},
    CareerNames.base_career_style_influencer_4: {SkillNames.base_skill_writing: 3, SkillNames.base_skill_charisma: 2},
    CareerNames.base_career_style_influencer_5: {SkillNames.base_skill_writing: 4, SkillNames.base_skill_photography: 2},
    CareerNames.base_career_style_influencer_6A: {
        SkillNames.base_skill_writing: 5,
        SkillNames.base_skill_charisma: 3,
        SkillNames.base_skill_painting: 3
    },
    CareerNames.base_career_style_influencer_6B: {
            SkillNames.base_skill_writing: 5,
            SkillNames.base_skill_charisma: 3,
            SkillNames.base_skill_painting: 3
    },
    CareerNames.base_career_style_influencer_7A: {
        SkillNames.base_skill_writing: 6,
        SkillNames.base_skill_charisma: 5,
        SkillNames.base_skill_painting: 4,
        SkillNames.base_skill_photography: 3,
    },
    CareerNames.base_career_style_influencer_8A: {
        SkillNames.base_skill_writing: 7,
        SkillNames.base_skill_charisma: 6,
        SkillNames.base_skill_painting: 5,
        SkillNames.base_skill_photography: 3,
    },
    CareerNames.base_career_style_influencer_9A: {
        SkillNames.base_skill_writing: 8,
        SkillNames.base_skill_charisma: 7,
        SkillNames.base_skill_painting: 6,
        SkillNames.base_skill_photography: 3,
    },
    CareerNames.base_career_style_influencer_10A: {
        SkillNames.base_skill_writing: 9,
        SkillNames.base_skill_charisma: 8,
        SkillNames.base_skill_painting: 7,
        SkillNames.base_skill_photography: 3,
    },
    CareerNames.base_career_style_influencer_7B: {
            SkillNames.base_skill_writing: 6,
            SkillNames.base_skill_charisma: 5,
            SkillNames.base_skill_painting: 4,
            SkillNames.base_skill_photography: 3
    },
    CareerNames.base_career_style_influencer_8B: {
            SkillNames.base_skill_writing: 7,
            SkillNames.base_skill_charisma: 6,
            SkillNames.base_skill_painting: 5,
            SkillNames.base_skill_photography: 3
    },
    CareerNames.base_career_style_influencer_9B: {
            SkillNames.base_skill_writing: 8,
            SkillNames.base_skill_charisma: 7,
            SkillNames.base_skill_painting: 6,
            SkillNames.base_skill_photography: 3
    },
    CareerNames.base_career_style_influencer_10B: {
            SkillNames.base_skill_writing: 9,
            SkillNames.base_skill_charisma: 8,
            SkillNames.base_skill_painting: 7,
            SkillNames.base_skill_photography: 3
    },
}

_career_tech_guru = {
    CareerNames.base_career_tech_guru_3: {
        SkillNames.base_skill_programming: 2
    },
    CareerNames.base_career_tech_guru_4: {
        SkillNames.base_skill_programming: 3
    },
    CareerNames.base_career_tech_guru_5: {
        SkillNames.base_skill_programming: 4,
        SkillNames.base_skill_video_gaming: 3
    },
    CareerNames.base_career_tech_guru_6: {
        SkillNames.base_skill_programming: 5,
        SkillNames.base_skill_video_gaming: 4
    },
    CareerNames.base_career_tech_guru_7A: {
        SkillNames.base_skill_programming: 6,
        SkillNames.base_skill_video_gaming: 5
    },
    CareerNames.base_career_tech_guru_7B: {
        SkillNames.base_skill_programming: 6,
        SkillNames.base_skill_video_gaming: 5,
    },
    CareerNames.base_career_tech_guru_8A: {
        SkillNames.base_skill_programming: 6,
        SkillNames.base_skill_video_gaming: 6,
    },
    CareerNames.base_career_tech_guru_9A: {
        SkillNames.base_skill_programming: 7,
        SkillNames.base_skill_video_gaming: 8
    },
    CareerNames.base_career_tech_guru_10A: {
        SkillNames.base_skill_programming: 8,
        SkillNames.base_skill_video_gaming: 10
    },
    CareerNames.base_career_tech_guru_8B: {
        SkillNames.base_skill_programming: 8,
        SkillNames.base_skill_video_gaming: 5,
        SkillNames.base_skill_charisma: 2
    },
    CareerNames.base_career_tech_guru_9B: {
        SkillNames.base_skill_programming: 9,
        SkillNames.base_skill_video_gaming: 5,
        SkillNames.base_skill_charisma: 4
    },
    CareerNames.base_career_tech_guru_10B: {
        SkillNames.base_skill_programming: 10,
        SkillNames.base_skill_video_gaming: 5,
        SkillNames.base_skill_charisma: 6
    },
}

_career_writer = {
    CareerNames.base_career_writer_4: {
        SkillNames.base_skill_writing: 3,
    },
    CareerNames.base_career_writer_5: {
        SkillNames.base_skill_writing: 4,
    },
    CareerNames.base_career_writer_6A: {
        SkillNames.base_skill_writing: 5,
    },
    CareerNames.base_career_writer_6B: {
        SkillNames.base_skill_writing: 5,
    },
    CareerNames.base_career_writer_7A: {
        SkillNames.base_skill_writing: 6,
        SkillNames.base_skill_logic: 2,
    },
    CareerNames.base_career_writer_8A: {
        SkillNames.base_skill_writing: 8,
        SkillNames.base_skill_logic: 3,
    },
    CareerNames.base_career_writer_9A: {
        SkillNames.base_skill_writing: 9,
        SkillNames.base_skill_logic: 4,
    },
    CareerNames.base_career_writer_10A: {
        SkillNames.base_skill_writing: 10,
        SkillNames.base_skill_logic: 5,
    },
    CareerNames.base_career_writer_7B: {
        SkillNames.base_skill_writing: 7,
        SkillNames.base_skill_charisma: 2,
    },
    CareerNames.base_career_writer_8B: {
        SkillNames.base_skill_writing: 8,
        SkillNames.base_skill_charisma: 3,
    },
    CareerNames.base_career_writer_9B: {
        SkillNames.base_skill_writing: 9,
        SkillNames.base_skill_charisma: 4,
    },
    CareerNames.base_career_writer_10B: {
        SkillNames.base_skill_writing: 10,
        SkillNames.base_skill_charisma: 5,
    },
}

CAREER_RULES: dict[str, dict[str, dict[str, int]] | dict[str, Rule]] = {
    CareerNames.base_career_athlete: _career_athlete,
    CareerNames.base_career_astronaut: _career_astronaut,
    CareerNames.base_career_business: _career_business,
    CareerNames.base_career_criminal: _career_criminal,
    CareerNames.base_career_culinary: _career_culinary,
    CareerNames.base_career_entertainer: _career_entertainer,
    CareerNames.base_career_painter: _career_painter,
    CareerNames.base_career_secret_agent: _career_secret_agent,
    CareerNames.base_career_style_influencer: _career_style_influencer,
    CareerNames.base_career_tech_guru: _career_tech_guru,
    CareerNames.base_career_writer: _career_writer,
}

def set_career_rules(world: Sims4World, options: Sims4Options):
    """
        Career locations are sent by the mod once per promotion in game (see the mod's
        career_event_dispatcher.py). The level in the location name is the level promoted to,
        so a check's rule must use the skill levels the game requires for that promotion.
        Example: base_career_writer_4 (Advice Columnist (Writer 4)) is sent upon being promoted
        from Freelance Article Writer (Writer 3) to Advice Columnist.
    """
    # TODO relearn how the career locations send, and then refactor this to use has_skill
    selected_careers = options.career

    for career_name, career_data in CAREER_RULES.items():
        if career_name in selected_careers:
            for loc_name, rule in career_data.items():
                if isinstance(rule, dict):
                    world.set_rule(world.get_location(loc_name), has_multiple_skills(rule))
                elif isinstance(rule, Rule):
                    world.set_rule(world.get_location(loc_name), rule)
                else:
                    raise ValueError(f"Unsupported type for {loc_name} rule: {type(rule)}")
