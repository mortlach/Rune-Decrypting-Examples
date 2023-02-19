import numpy as np
import gematria as gem
from lm_data_with_word_len import *


class LanguageModel:


    # set the log transition probability matrices for each word length
    log_bigram_transition_matrix_by_word_len = np.array(bigram_matrix_with_word_len)
    log_unigram_transition_matrix_by_word_len = np.array(unigram_matrix_with_word_length)

    def get_word_log_probability(self, word):
        """get the word log probability"""
        word_len = len(word) - 1
        # use 1st and last letter of word with unigram probability
        first_letter_index = gem.rune_to_index[word[0]]
        log_unigram_prob = self.log_unigram_transition_matrix_by_word_len[word_len][first_letter_index]

        # get the bi-gram probabilities for the rest of the characters
        log_bigram_prob = 0
        for i in range(len(word) - 1):
            # convert each rune to an index and lookup value in the matrix
            index_in_log_bigram_transition_matrix_by_word_len = gem.rune_to_index[word[i]] * 29 + gem.rune_to_index[word[i + 1]]
            log_bigram_prob += self.log_bigram_transition_matrix_by_word_len[word_len][index_in_log_bigram_transition_matrix_by_word_len]
        return log_unigram_prob + log_bigram_prob

    def get_sentence_log_probability(self, sentence):
        """get the sentence log probability"""
        # split the sentence into tokens and get log-prob foe each
        tokens = sentence.split()
        return sum([self.get_word_log_probability(token) for token in tokens])


if __name__ == "__main__":
    print("run")
    lm = LanguageModel()
