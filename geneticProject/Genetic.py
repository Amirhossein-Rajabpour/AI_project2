from geneticProject.AdditionalFunctions import *
from geneticProject.Chromosome import *

def is_end():
    pass

def calculate_average_score(array_of_chromosomes):
    sum_scores = 0
    for chromosome in array_of_chromosomes:
        sum_scores += chromosome.score
    return sum_scores/len(array_of_chromosomes)


class Genetic:
    # population is a dictionary of generation and array of chromosome objects
    # => {1: [chromosome1, chromosome2, ...], 2:[chromosomeK, ...]}
    def __init__(self, population, game_plate, selection_mode, crossover_mode, crossover_point):
        self.population = population
        self.game_plate = game_plate
        self.selection_mode = selection_mode
        self.crossover_mode = crossover_mode
        self.crossover_point = crossover_point
        self.best_answer = ''
        self.generation_average_scores = {}

        current_generation = 2
        len_population = len(self.population[1])
        self.generation_average_scores[1] = calculate_average_score(self.population[1])

        while not is_end():

            # crossover step
            new_generation = []
            while len(new_generation) <= len_population-2:
                # TO DO: how to decide which chromosomes to choose for offspring?
                child1, child2 = crossover(, , self.crossover_point, self.crossover_mode)
                game = Game(self.game_plate)
                score1, failure_points1 = game.get_score(child1, score_mode="")
                new_generation.append(Chromosome(child1, score1, current_generation, failure_points1))

                score2, failure_points2 = game.get_score(child2, score_mode="")
                new_generation.append(Chromosome(child2, score2, current_generation, failure_points2))

            self.population[current_generation] = new_generation


            # mutation step
            for chromosome in self.population[current_generation]:
                mutation(chromosome, 0.1, game)

            self.generation_average_scores[current_generation] = calculate_average_score(self.population[current_generation])
            
            # selection step
            self.population[current_generation+1] = selection(len_population, self.population[current_generation], self.population[current_generation-1], self.selection_mode)

            current_generation += 1
