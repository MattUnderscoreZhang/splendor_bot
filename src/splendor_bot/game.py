from copy import deepcopy
import random

from splendor_bot.base_deck import decks_by_level, nobles
from splendor_bot.types import Gems, GameState, Player


def new_game(n_players: int) -> GameState:
    # changes for number of players
    assert 2 <= n_players <= 4, "Only 2-4 players are supported."
    n_gems = (
        4 if n_players == 2 else
        5 if n_players == 3 else
        7
    )
    gem_pool = Gems(n_gems, n_gems, n_gems, n_gems, n_gems, 5)
    revealed_nobles = random.sample(nobles, n_players+1)
    first_player_n = random.randint(0, n_players-1)
    # deal cards
    decks_by_level_after_deal = [
        random.sample(deck, len(deck))
        for deck in decks_by_level
    ]
    revealed_cards_by_level = [
        [decks_by_level_after_deal[level].pop() for _ in range(4)]
        for level in range(3)
    ]
    # set up game
    return GameState(
        players=[Player() for _ in range(n_players)],
        decks_by_level=decks_by_level_after_deal,
        revealed_cards_by_level=revealed_cards_by_level,
        nobles=revealed_nobles,
        gem_pool=gem_pool,
        first_player_n=first_player_n,
        current_player_n=first_player_n,
        round=1,
        last_round=False,
    )


def deal_card(game_state: GameState, level: int) -> GameState:
    game_state = deepcopy(game_state)
    card = game_state.decks_by_level[level-1].pop()
    game_state.revealed_cards_by_level[level-1].append(card)
    return game_state


def move_to_next_player(game_state: GameState) -> GameState:
    game_state = deepcopy(game_state)
    game_state.current_player_n = (game_state.current_player_n + 1) % len(game_state.players)
    if game_state.current_player_n == game_state.first_player_n:
        game_state.round += 1
    return game_state


# TODO: return gems


# TODO: win nobles


# TODO: end turn (return gems, win nobles, move to next player)


# TODO: take gems
"""
def take_gems(self, gems: Gems) -> None:
    assert len(gems) <= 3, "Can only take up to 3 gems."
    assert gems <= self.gem_pool, "Not enough gems in the pool."
    assert sum(gems[i] > self.players[self.current_player_n].gems[i] for i in range(6)) <= 1, "Can only take 2 gems of the same color."
    # take the gems
    self.gem_pool -= gems
    self.players[self.current_player_n].gems += gems
"""


# TODO: reserve card (reserve card, deal card, take gold)


# TODO: purchase card (purchase card (increase generation), deal card, return gems)
