import random

# Parameter Genetic Algorithm
N = 8  # Jumlah Ratu
POPULATION_SIZE = 100  # Ukuran Populasi
MUTATION_RATE = 0.05  # Tingkat Mutasi
MAX_GENERATIONS = 1000  # Jumlah Maksimal Generasi

# Fungsi untuk menghitung fitness (jumlah pasangan ratu yang tidak saling menyerang)
def fitness(chromosome):
    non_attacking_pairs = 0
    for i in range(len(chromosome)):
        for j in range(i + 1, len(chromosome)):
            if chromosome[i] != chromosome[j] and abs(chromosome[i] - chromosome[j]) != abs(i - j):
                non_attacking_pairs += 1
    # Maksimal pasangan yang tidak saling menyerang untuk N-Queen adalah N*(N-1)/2
    max_pairs = N * (N - 1) / 2
    return non_attacking_pairs / max_pairs

# Fungsi untuk membuat individu acak
def create_individual():
    return [random.randint(0, N - 1) for _ in range(N)]

# Fungsi untuk melakukan crossover dua individu (parent)
def crossover(parent1, parent2):
    point = random.randint(1, N - 2)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Fungsi untuk mutasi
def mutate(individual):
    if random.random() < MUTATION_RATE:
        i = random.randint(0, N - 1)
        individual[i] = random.randint(0, N - 1)

# Fungsi untuk memilih individu berdasarkan roulette wheel
def select(population):
    total_fitness = sum(fitness(ind) for ind in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual in population:
        current += fitness(individual)
        if current > pick:
            return individual

# Fungsi utama Algoritma Genetika untuk menyelesaikan N-Queen
def genetic_algorithm():
    # Inisialisasi populasi
    population = [create_individual() for _ in range(POPULATION_SIZE)]
    generation = 0
    solution_found = False

    while generation < MAX_GENERATIONS and not solution_found:
        # Seleksi individu dengan fitness terbaik
        population = sorted(population, key=fitness, reverse=True)
        
        # Cek jika ada solusi optimal
        if fitness(population[0]) == 1:
            solution_found = True
            break

        # Generasi baru
        new_population = []
        
        # Reproduksi (Crossover dan Mutasi)
        while len(new_population) < POPULATION_SIZE:
            parent1 = select(population)
            parent2 = select(population)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])

        population = new_population
        generation += 1

    # Output solusi
    if solution_found:
        print(f"Solusi ditemukan dalam generasi ke-{generation}:")
        print(population[0])
    else:
        print("Solusi tidak ditemukan dalam batas generasi maksimum.")

# Menjalankan Algoritma Genetika untuk N-Queen
genetic_algorithm()
