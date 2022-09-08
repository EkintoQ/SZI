import random


class genetic:
    def __init__(self, chrome):
        self.chrome = chrome
        self.key = 10
        self.pop_size = 500
        self.gen_max = 20
        self.length = len(chrome) - 1
        self.div = self.length // 2
        self.rand = list(range(1, self.length + 1))

    def create_genome(self):
        genome = "0"
        exclusive = random.sample(self.rand, self.length)
        genome += "".join(map(str, exclusive))
        return genome

    def find_fitness(self, genome):
        fitness = 0
        for i in range(len(genome) - 1):
            fitness += self.chrome[int(genome[i])][int(genome[i + 1])]
        return fitness

    def crossOver(self, gen1, gen2):
        gen = []
        for i in range(self.div):
            gen.append(gen1[i])
        for i in range(self.div, self.length+1):
            if gen2[i] not in gen:
                gen.append(gen2[i])
            else:
                j = 0
                while gen1[j] in gen:
                    j += 1
                gen.append(gen1[j])
        return ''.join(gen)

    def mutation(self, genome):
        genome = list(genome)
        while True:
            gen1 = random.randint(1, self.length - 1)
            gen2 = random.randint(1, self.length - 1)
            if gen1 != gen2:
                genome[gen1], genome[gen2] = genome[gen2], genome[gen1]
                break
        return ''.join(genome)

    def search(self):
        gen = 1
        population = []

        for i in range(self.pop_size):
            ind = individual()
            ind.genome = self.create_genome()
            ind.fitness = self.find_fitness(ind.genome)
            population.append(ind)

        print("First population:")
        for ind in population:
            print(ind.genome, ind.fitness)

        while gen <= self.gen_max:
            new_population = population

            key = random.randint(0, 100)
            if key > self.key:
                for i in range(self.pop_size):
                    temp1, temp2 = random.sample(population, 2)
                    new_ind1 = individual()
                    new_ind1.genome = self.crossOver(temp1.genome, temp2.genome)
                    new_ind1.fitness = self.find_fitness(new_ind1.genome)
                    new_ind2 = individual()
                    new_ind2.genome = self.crossOver(temp2.genome, temp1.genome)
                    new_ind2.fitness = self.find_fitness(new_ind2.genome)
                    new_population.append(new_ind1)
                    new_population.append(new_ind2)
                    new_population.sort()
                    new_population.pop()
                    new_population.pop()
            else:
                print('mutation')
                for i in range(self.pop_size):
                    temp1 = random.choice(population)
                    new_ind = individual()
                    new_ind.genome = self.mutation(temp1.genome)
                    new_ind.fitness = self.find_fitness(new_ind.genome)
                    new_population.append(new_ind)
                    new_population.sort()
                    new_population.pop()
            print("\n")
            print("New Generation # ", gen)
            print("Genome	 Fitness")

            for i in range(self.pop_size):
                print(new_population[i].genome, new_population[i].fitness)

            print("\n")

            gen += 1

        ans = min(population, key=lambda x: x.fitness)
        print("Final order: ", ans.genome, ans.fitness)
        return ans.genome


class individual:
    def __init__(self):
        self.genome = 0
        self.fitness = 0

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness

    def __le__(self, other):
        return self.fitness <= other.fitness

    def __ge__(self, other):
        return self.fitness >= other.fitness
