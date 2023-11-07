from Json_Scrapper import scrapper_title_json
from fuzzywuzzy import fuzz
from tqdm import tqdm

# Load your JSON data into a list of conference titles
conference_data = scrapper_title_json("HAL_2000_test_1000.json")

# Create a list to store duplicate titles
duplicate_titles = []

# Define a similarity threshold (adjust as needed)
threshold = 80

# Normalize and compare conference titles
for i in tqdm(range(len(conference_data)), desc="conf", colour='red'):
    for j in range(i + 1, len(conference_data)):
        title1 = conference_data[i]
        title2 = conference_data[j]
        similarity_score = fuzz.ratio(title1.lower(), title2.lower())

        if similarity_score >= threshold and similarity_score != 100:
            duplicate_titles.append((title1, title2, similarity_score))

# Print the list of duplicate titles
with open("Result_Test/duplicate_titles_" + "_11k" + ".txt", "w", encoding='utf-8') as output_file:
    # Write the list of duplicate titles to the file
    for pair in duplicate_titles:
        output_file.write(f"Duplicates: {pair[0]} // {pair[1]} --- TH= {pair[2]}\n")

    # Write the count of duplicates and total conferences
    output_file.write(f"{len(duplicate_titles)}/{len(conference_data)}\n")
