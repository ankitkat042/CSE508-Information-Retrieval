import os
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

directory = 'text_files'
destination_directory = 'preprocessed'

if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

stop_words = set(stopwords.words('english'))
punctuation_table = str.maketrans('', '', string.punctuation)
count = 0
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            if count < 5: print(file); count += 1 
            text = file.read().lower()  # Lowercase the text
            tokens = word_tokenize(text)  # Tokenize
            tokens = [w.translate(punctuation_table) for w in tokens]  # Remove punctuations
            tokens = [word for word in tokens if word not in stop_words]  # Remove stopwords
            tokens = [word for word in tokens if word.strip()]  # Remove blank space tokens

            processed_file_path = os.path.join(destination_directory, filename)
            with open(processed_file_path, 'w', encoding='utf-8') as processed_file:
                processed_file.write(' '.join(tokens))

                
