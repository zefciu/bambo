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
        for i in range(self.number):
            new_spec = self._draw_new()
            if new_spec == ('A', 'A'):
                self.dominant += 1
            elif new_spec == ('A', 'a'):
                self.heterozyg += 1
            else:
                self.recess += 1
            

    def __str__(self):
        return 'AA: {}, Aa: {}, aa: {}'.format(
            self.dominant,
            self.heterozyg,
            self.recess,
        )

    def _draw_new(self):
        """Returns a new specimen for initial population."""
        def get_allele():
            return A if rnd.random() > self.init_fraction_recess else a
        return tuple(sorted([get_allele(), get_allele()]))


if __name__ == '__main__':
    p = Population(1000, 0.5, 1, 0)
    print(p)
                

