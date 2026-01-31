import pandas as pd

def findHeavyAnimals(animals):
    return animals[animals["weight"] > 100].sort_values("weight", ascending=False)[["name"]]
