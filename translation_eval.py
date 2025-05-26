 

import json
import pandas as pd 
import random   
random.seed(42)

# import translated_ds_az.json and translated_ds_tr.json 
with open('translated_ds_az.json', 'r', encoding='utf-8') as f:
    az_data = json.load(f)

with open('translated_ds_tr.json', 'r', encoding='utf-8') as f:
    tr_data = json.load(f)



# Print the first 50 characters of the string representation of az_data
# print("az_data: ", str(az_data)[:450])


az_data_combined = az_data['train'] + az_data['test'] + az_data['validation']
tr_data_combined = tr_data['train'] + tr_data['test'] + tr_data['validation']

# Print the first 50 characters of the string representation of az_data
# print("az_data: ", str(az_data_combined)[:450])
# print("tr_data: ", str(tr_data_combined)[:450])


# sort both dictionaries by the 'hash' key
az_data_combined.sort(key=lambda x: x['hash'])
tr_data_combined.sort(key=lambda x: x['hash'])

# add a key called 'grade' to all elements and set it to -1 for both tr and az
for i in range(len(az_data_combined)):
    az_data_combined[i]['grade'] = -1
for i in range(len(tr_data_combined)):
    tr_data_combined[i]['grade'] = -1
    
# Print the first 50 characters of the string representation of az_data
# print("az_data: ", str(az_data_combined)[:450])
# print("tr_data: ", str(tr_data_combined)[:450])

# make "hash" key the index of both dictionaries. 
az_data_combined = pd.DataFrame(az_data_combined).set_index('hash')
tr_data_combined = pd.DataFrame(tr_data_combined).set_index('hash')

# print(az_data_combined.head())




# Convert lists to DataFrames and set 'hash' as index if not already done
if not isinstance(az_data_combined, pd.DataFrame):
    az_data_combined = pd.DataFrame(az_data_combined).set_index('hash')
if not isinstance(tr_data_combined, pd.DataFrame):
    tr_data_combined = pd.DataFrame(tr_data_combined).set_index('hash')

random_hashes = random.sample(list(az_data_combined.index), 50)
print("random_hashes: ", random_hashes[:10])

# 5 Grades of translation: 

# 0 = Semantically wrong
# 1 = Major syntaxical errors
# 2 = Minor syntaxical errors
# 3 = Correct translation
# 4 = Not applicable (e.g. the text is not a translation)

# Loop over random hashes and let user manually grade the translation. 
for hash in random_hashes:
    print("Hash: ", hash)
    print("EN: ", " ".join(az_data_combined.loc[hash]['original_tokens']))
    print("AZ: ", " ".join(az_data_combined.loc[hash]['tokens']))
    print("TR: ", " ".join(tr_data_combined.loc[hash]['tokens']))
    while True:
        try:
            az_grade = int(input("Grade for Azerbaijani (0-4): "))
            if 0 <= az_grade <= 4:
                break
            else:
                print("Please enter a valid grade between 0 and 4.")
        except ValueError:
            print("Invalid input. Please enter an integer between 0 and 4.")

    while True:
        try:
            tr_grade = int(input("Grade for Turkish (0-4): "))
            if 0 <= tr_grade <= 4:
                break
            else:
                print("Please enter a valid grade between 0 and 4.")
        except ValueError:
            print("Invalid input. Please enter an integer between 0 and 4.")   # add the grades to the respective dataframes
    az_data_combined.loc[hash, 'grade'] = az_grade
    tr_data_combined.loc[hash, 'grade'] = tr_grade
    
    # clear the screen
    print("\033[H\033[J", end='')
    

# print grades of both dataframes
print("tr_data_combined nonzero grades: ", tr_data_combined[tr_data_combined['grade'] != -1]['grade'])
print("az_data_combined nonzero grades: ", az_data_combined[az_data_combined['grade'] != -1]['grade'])



# based on it create a new dataframe with the following columns:
# hash, original_tokens (joined by space), az_tokens (joined by space), tr_tokens (joined by space), az_grade, tr_grade
az_data_combined = az_data_combined[az_data_combined['grade'] != -1]
tr_data_combined = tr_data_combined[tr_data_combined['grade'] != -1]
az_data_combined = az_data_combined[['original_tokens', 'tokens', 'grade']]
tr_data_combined = tr_data_combined[['original_tokens', 'tokens', 'grade']]
az_data_combined.columns = ['original_tokens', 'az_tokens', 'az_grade']
tr_data_combined.columns = ['original_tokens', 'tr_tokens', 'tr_grade']

# Convert 'original_tokens' from lists to strings for merging
az_data_combined['original_tokens'] = az_data_combined['original_tokens'].apply(lambda x: " ".join(x))
tr_data_combined['original_tokens'] = tr_data_combined['original_tokens'].apply(lambda x: " ".join(x))
# Convert 'tokens' from lists to strings
az_data_combined['az_tokens'] = az_data_combined['az_tokens'].apply(lambda x: " ".join(x))
tr_data_combined['tr_tokens'] = tr_data_combined['tr_tokens'].apply(lambda x: " ".join(x))
# Convert 'grade' columns to integers
az_data_combined['az_grade'] = az_data_combined['az_grade'].astype(int)
tr_data_combined['tr_grade'] = tr_data_combined['tr_grade'].astype(int)


# merge both dataframes on the hash key
merged_data = pd.merge(az_data_combined, tr_data_combined, on='original_tokens', how='inner')

# print the first 5 rows of the merged dataframe
print(merged_data.head())
# save the merged dataframe to a csv file
merged_data.to_csv('translation_grades.csv', index=False, encoding='utf-8')
