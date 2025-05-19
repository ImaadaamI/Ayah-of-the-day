import json
import random
import os

# Define the list of topics available
topics = ["iklaq", "relationships", "mercy", "jannah", "zakat"]

# Choose a random topic
chosen_topic = random.choice(topics)

# Load the ayahs from the corresponding file
with open(f"{chosen_topic}.json", "r", encoding="utf-8") as f:
    ayahs = json.load(f)

# Choose a random ayah from that topic
chosen_ayah = random.choice(ayahs)

# Write the chosen ayah to data.json
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(chosen_ayah, f, ensure_ascii=False, indent=2)
