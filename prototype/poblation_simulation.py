"""
Simulation of population growth system.
"""
import math
from typing import List


def statistic_function(k, population, r, time_interval):
    """Function to calculate new population after a defined time interval."""
    e = 2.71828
    new_population = (k * population * e ** (r * time_interval)) / (
        k + population * (e ** (r * time_interval) - 1)
    )
    return new_population


class Species:
    """Base Species Class"""

    name: str
    r: float
    k_coeficient: int
    k: int
    impact_over_previous_species: float
    population: int

    def __init__(
        self,
        name,
        r_base,
        k_coeficient,
        impact_over_previous_species,
        population_base=2,
    ):
        self.name = name
        self.r = r_base
        self.k_coeficient = k_coeficient
        self.impact_over_previous_species = impact_over_previous_species
        self.population = population_base

    def r_reduction(self, rate_modification):
        self.r = self.r - rate_modification

    def r_addition(self, rate_modification):
        self.r = self.r + rate_modification

    def calculate_new_population(self, k, time_interval):
        self.population = statistic_function(k, self.population, self.r, time_interval)

    def update_k(self, dependant_species_population):
        print(dependant_species_population)
        print(self.k_coeficient)
        self.k = dependant_species_population * self.k_coeficient


class Tile:
    """Base Tile Class"""

    k_base: int
    r_base: float
    species: List[Species]

    def __init__(self, k_base, r_base):
        self.k_base = k_base
        self.r_base = r_base
        self.species = []

    def add_species(self, new_species):
        if self.species:
            try:
                for s in self.species:
                    s.r_reduction(new_species.impact_over_previous_species)
            except Exception as e:
                print(e)
        if not new_species.impact_over_previous_species:
            new_species.k = self.k_base
        self.species.append(new_species)

    def update_tile_population(self, time_interval):
        dependant_species_population = self.k_base
        for s in self.species:
            if s.impact_over_previous_species:
                s.update_k(dependant_species_population)
            dependant_species_population = s.calculate_new_population(
                s.k, time_interval
            )


def test():
    red_algae = Species("red_algae", 0.09, 1, 0)
    mollusks = Species("mollusks", 0.002, 0.5, 0.07)
    fishes = Species("fishes", 0.001, 0.25, 0.03)
    reef = Tile(100, 0.6)
    reef.add_species(red_algae)
    for t in range(1, 1200):
        reef.update_tile_population(1)
        if t % 50 == 0:
            for species in reef.species:
                print(
                    f"{species.name} population after {t} seconds is {math.floor(species.population)}"
                )
        if t == 800:
            reef.add_species(mollusks)
        if t == 850:
            reef.add_species(fishes)


if __name__ == "__main__":
    test()
