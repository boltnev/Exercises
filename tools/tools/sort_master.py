import random


class SortMaster:

    def create_random_sequence(self, elements=100):
        return [random.randint(0, elements) for _ in range(elements)]

    def check_sorted(self, sequence):
        return sorted(sequence) == sequence
