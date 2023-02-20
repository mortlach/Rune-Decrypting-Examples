import numpy as np
import random
from language_model import LanguageModel
from mono_cipher import MonoCipher
from copy import copy
import time
import gematria as gem


class BasicGeneticAlgorithm:

    DNA_POOL_SIZE = 20
    OFFSPRING_POOL_SIZE = 10
    NUM_ITER = 1000
    MAX_MUTATIONS = 2
    
    def __init__(self):
        self.mean_score_per_it = None
        self.best_score_per_it = None
        self.best_dna = None
        self.best_solution = None
        self.best_score = None

        self.language_model = LanguageModel()   # the language model
        self.cipher = MonoCipher()              # the 'cipher'
        """ Generate DNA pool: random permutation of the runes """
        self.dna_pool = ["".join(list(np.random.permutation(gem.runes))) for x in range(self.DNA_POOL_SIZE)]
        self.offspring_pool = []
        print(f'init len(self.dna_pool) = {len(self.dna_pool)}')

    #@staticmethod
    def mutate(self, s, n):
        """ randomly swap two characters in s at random positions n times """
        #index_1, index_2 = random.sample(list(np.arange(len(sequence))), 2) # random positions
        num_mutations = 1
        if n > 1:
            num_mutations = random.choice( list(range(1,n)))

        s_copy = copy(s)
        mutation_count = 0
        while mutation_count < num_mutations:
            i, j = random.sample( list(range(len(s))), 2) # random positions
            s_list = list(s_copy)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            s_copy = s_list
            mutation_count += 1
        return "".join(s_copy)

    def evolve_offspring(self):
        """ asexual reproduction, evolves offspring by random swaps for every dna sequence in the dna pool,  """
        for dna in self.dna_pool:
            # mutate offspring for each dna in the dna pool
            self.offspring_pool += [ self.mutate(dna, self.MAX_MUTATIONS) for x in range(self.OFFSPRING_POOL_SIZE) ]
        return self.offspring_pool + self.dna_pool

    def solve(self, ciphertext_to_solve, actual_pliantext = "", actual_pliantext_score = 0):
        """ try and "solve" message_to_solve  """
        ts= time.time()
        self.mean_score_per_it = np.zeros(self.NUM_ITER)
        self.best_score_per_it = np.zeros(self.NUM_ITER)
        self.best_dna = None
        self.best_solution = None
        self.best_score = -9999999999999999.9
        dna_scores = {} # for each dna, keep its score
        #
        for i in range(self.NUM_ITER):
            # only evolve on 2nd iteration
            if i > 0:
                self.dna_pool = self.evolve_offspring()
            # scores each 'NEW' dna
            for dna in self.dna_pool:
                if dna not in dna_scores:
                    # get current solution from  dna
                    current_sol = {p: c for p, c in zip(gem.runes, dna)}
                    # get PT using current_solution and score it
                    current_pt = self.cipher.decode(ciphertext_to_solve, current_sol)
                    dna_scores[dna] = self.language_model.get_sentence_log_probability2(current_pt)
                    # keep the best solution and scores
                    if dna_scores[dna] > self.best_score:
                        self.best_score = dna_scores[dna]
                        self.best_solution = current_sol
                        self.best_dna = dna

            # get the current generation average scores
            self.mean_score_per_it[i] = np.mean(list(dna_scores.values()))
            self.best_score_per_it[i] = self.best_score

            # choose OFFSPRING_POOL_SIZE best performing dna to pass on to the next generation
            sorted_dna_curr_gen = sorted( dna_scores.items(), key=lambda x: x[1], reverse=True)
            self.dna_pool = [s[0] for s in sorted_dna_curr_gen[:BasicGeneticAlgorithm.OFFSPRING_POOL_SIZE]]

            if i % 10 == 0:
                pt_guess = self.cipher.decode(ciphertext_to_solve, self.best_solution)
                print(f"\n{i}, mean score = {self.mean_score_per_it[i]}, best score /(desired score) = {self.best_score}/({actual_pliantext_score})")
                print(f"pt_in = {actual_pliantext}")
                print(f"pt_ga = {pt_guess}")
                pte_in = "".join([gem.rune2latin_dict.get(x, x) for x in list(actual_pliantext)])
                pte_ga = "".join([gem.rune2latin_dict.get(x, x) for x in list(pt_guess)])
                print(f"pte_in = {pte_in}")
                print(f"pte_ga = {pte_ga}")

            if actual_pliantext_score == self.best_score:
                print(f"\n *** Iteration {i} found known solution , quitting! *** ")
                break
