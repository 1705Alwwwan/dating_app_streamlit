import random
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def match_user(current_user, candidates, generations=50, population_size=20):
    def is_valid_pair(male, female):
        return (
            male["gender"] == "male" and
            female["gender"] == "female" and
            male["location"].lower() == female["location"].lower() and
            0 <= male["age"] - female["age"] <= 10
        )

    if current_user["gender"] == "female":
        candidates = [c for c in candidates if is_valid_pair(c, current_user)]
    else:
        candidates = [c for c in candidates if is_valid_pair(current_user, c)]

    if not candidates:
        return None

    def fitness(u1, u2):
        vec1 = np.array(u1["vector"]).reshape(1, -1)
        vec2 = np.array(u2["vector"]).reshape(1, -1)
        similarity = cosine_similarity(vec1, vec2)[0][0]
        age_diff = abs(u1["age"] - u2["age"])
        age_bonus = 0.1 if u1["gender"] == "male" and u1["age"] > u2["age"] else 0
        return similarity - (age_diff / 100) + age_bonus

    population = random.sample(candidates, min(len(candidates), population_size))

    for _ in range(generations):
        population.sort(key=lambda x: -fitness(current_user, x))
        new_population = population[:5]
        while len(new_population) < population_size:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = parent1.copy()
            if random.random() < 0.5:
                child["vector"] = parent2["vector"]
            if random.random() < 0.2:
                idx = random.randint(0, len(child["vector"]) - 1)
                child["vector"][idx] = 1 - child["vector"][idx]
            new_population.append(child)
        population = new_population

    population.sort(key=lambda x: -fitness(current_user, x))
    return population[0]
