# Rune-Decrypting-Examples

Over the past few years I've been re-building lots of my rune-decrypting tools, specifically different language-models based on data from the Google N-gram database and Project Guttenberg, all converted to runes. These word lists can be used to build "transition probability matrices" used in heuristic algorithms to solve many ciphers.
As a first example a very simple Genetic-Algorithm that can solve general mono-alphabetic ciphers is shared. 
This is for demonstration purposes. 


# 1: Mono-Alphabetic Substitution Ciphers:  Genic Algorithm Solver

## Introduction
Information on  mono-alphabetic substitution cipher and genetic algorithms (GA) can be found in many places. Here a very simple asexually reproducing GA is used to solve a general mono-alphabetic cipher.
Briefly: a pool of solutions is generated, and scored using the language-model. Each solution has offspring, that are mutated slightly from the previous generation. The most successfully solutions survive and can reproduce  again next generation.  
The data used to fit each generation is contained in two "log transition probability matrices" one for rune uni-grams and 1 for rune bi-grams. For this example these have been calculated foreword lengths 1 to 14 runes using the Project Gutenberg data. 
Log Probabilities are found via a simple look-up and added together 

## Requirements 
For increased speed, numpy is used in the current solution and the main non-standard python library that should be installed 

## Run
From the source directory run:   
>>> python3 main.py



## Troubleshooting
Depending on your text size, randomness, the algorithm can get stuck in locally optimal solutions. There a few parameters that can be tweaked to improve the performance of the GA.  
Alternatively, more sophisticated genetic algorithms can be used (this one is about as basic as could be). 
Parameters to tweak in basic_genetic_algorithm.py are: 
1. DNA_POOL_SIZE  
number of solutions that survive each generation 
2. OFFSPRING_POOL_SIZE  
number of offspring each generation 
3. NUM_ITER  
maximum number of generations 
4. MAX_MUTATIONS  
Maximum number of mutations each child will have 
