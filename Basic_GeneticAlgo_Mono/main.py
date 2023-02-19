if __name__ == "__main__":
    from basic_genetic_algorithm import BasicGeneticAlgorithm
    from mono_cipher import MonoCipher
    import gematria as gem
    from language_model import LanguageModel

    # for testing purposes create a dummy message, encode and score it
    original_plaintext_english = """"WELCOME. WELCOME, PILGRIM, TO THE GREAT JOURNEY 
    TOWARD THE END OF ALL THINGS IT IS NOT AN EASY TRIP, BUT FOR THOSE WHO FIND 
    THEIR WAY HERE IT IS A NECESSARY ONE. ALONG THE WAY YOU WILL FIND AN END TO 
    ALL STRUGGLE AND SUFFERING, YOUR INNOCENCE, YOUR ILLUSIONS, YOUR CERTAINTY, 
    AND YOUR REALITY. ULTIMATELY, YOU WILL DISCOVER AN END TO SELF. IT IS THROUGH 
    THIS PILGRIMAGE THAT WE SHAPE OURSELVES AND OUR REALITIES. JOURNEY DEEP WITHIN 
    AND YOU WILL ARRIVE OUTSIDE. LIKE THE INSTAR, IT IS ONLY THROUGH GOING WITHIN 
    THAT WE MAY EMERGE"""
    lm = LanguageModel()
    original_plaintext_english_no_punctuation = ''.join([x for x in original_plaintext_english if x.isalpha() or (x == ' ')])
    original_plaintext_runes = ' '.join([gem.translate_to_gematria(x) for x in original_plaintext_english_no_punctuation.split()])
    original_plaintext_score = lm.get_sentence_log_probability(original_plaintext_runes)

    cipher = MonoCipher()
    # get message to solve  from initial message
    ciphertext_to_solve = cipher.encode(original_plaintext_runes)

    # set up solver
    solver = BasicGeneticAlgorithm()
    solver.solve( ciphertext_to_solve = ciphertext_to_solve, actual_pliantext = original_plaintext_runes, actual_pliantext_score = original_plaintext_score)

    best_solution  = solver.best_solution
    cipher = MonoCipher()
    decoded_message = cipher.decode(ciphertext_to_solve, best_solution)
    pte_ga = "".join([gem.rune2latin_dict.get(x, x) for x in list(cipher.decode(ciphertext_to_solve, best_solution))])

    print(f"Best Message: {decoded_message}")
    print(f"              {pte_ga}")

