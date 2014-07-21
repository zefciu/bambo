#!/usr/bin/env python3
import random as rnd


A = 'A'
a = 'a'

class Population(object):

    def __init__(
        self,
        number,
        init_fraction_recess,
        weight_recess,
        dominant_addition_per_generation,
    ):
        self.number = number
        self.init_fraction_recess = init_fraction_recess
        self.dominant = self.heterozyg = self.recess = 0
        self.weight_recess = weight_recess
        self.dominant_addition_per_generation =\
            dominant_addition_per_generation
        for i in range(self.number):
            new_spec = self._draw_new()
            if new_spec == ('A', 'A'):
                self.dominant += 1
            elif new_spec == ('A', 'a'):
                self.heterozyg += 1
            else:
                self.recess += 1
        self.compute_weighted_sum()
            

    def __str__(self):
        return 'AA: {}, Aa: {}, aa: {}'.format(
            self.dominant,
            self.heterozyg,
            self.recess,
        )

    def compute_weighted_sum(self):
        """Computes the weighted sum of all specimens and the thresholds."""
        self.weighted_sum = (
            self.dominant +
            self.heterozyg +
            self.recess#  * self.weight_recess
        )
        self.dominant_threshold = self.dominant / self.weighted_sum
        self.heterozyg_threshold = (
            self.dominant_threshold + self.heterozyg / self.weighted_sum
        )

    def get_next_generation(self):
        next_dominant = next_heterozyg = next_recess = 0
        for i in range(self.number):
            new_spec = self._mate(
                self._draw_spec_with_preference(), 
                self._draw_spec_with_preference(),
            )
            if new_spec == ('A', 'A'):
                next_dominant += 1
            elif new_spec == ('A', 'a'):
                next_heterozyg += 1
            else:
                next_recess += 1
        next_generation = Population.__new__(Population)
        next_generation.number = self.number
        next_generation.init_fraction_recess= self.init_fraction_recess
        next_generation.weight_recess = self.weight_recess
        next_generation.dominant_addition_per_generation =\
            self.dominant_addition_per_generation
        next_generation.dominant = next_dominant
        next_generation.heterozyg = next_heterozyg
        next_generation.recess = next_recess
        next_generation.compute_weighted_sum()
        return next_generation


    def _draw_new(self):
        """Returns a new specimen for initial population."""
        def get_allele():
            return A if rnd.random() > self.init_fraction_recess else a
        return tuple(sorted([get_allele(), get_allele()]))

    def _draw_spec_with_preference(self):
        """Returns a random specimen from the population weighted by
        sexual selection."""
        n = rnd.random()
        if n <= self.dominant_threshold:
            return (A, A)
        elif n <= self.heterozyg_threshold:
            return (A, a)
        else:
            return (a, a)

    def _mate(self, first, second):
        """Mates two specimens returning a new one."""
        return (rnd.choice(first), rnd.choice(second))


if __name__ == '__main__':
    p = Population(1000, 0.5, 1, 0)
    for i in range(20):
        print(p)
        p = p.get_next_generation()
