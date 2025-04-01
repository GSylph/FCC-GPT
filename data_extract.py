import os
import lzma
from tqdm import tqdm

def xz_files_in_dir(directory):
    """
    Generator function to yield .xz files in a directory and its subdirectories.
    """
    files=[]
    for filename in os.listdir(directory):
        if filename.endswith('.xz') and os.path.isfile(os.path.join(directory, filename)):
            files.append(filename)
    return files


folder_path = "C:/Users/hp/Desktop/Code/Projects/fcc-gpt/openwebtext"
output_file_train="output_train.txt"
output_file_val="output_val.txt"
vocab_file="vocab.txt"
split_files = int(input("How many files do you want to split into?"))

files = xz_files_in_dir(folder_path)
total_files = len(files)

#calculate the split indices
split_index=int(total_files*0.9) #90% for training, 10% for validation
files_train = files[:split_index]
files_val = files[split_index:]

#Process the files for training and validation separately 
vocab = set()


#Process the training files
with open(output_file_train, 'w', encoding='utf-8') as outfile:
    for filename in tqdm(files_train, total=len(files_train)):
        file_path = os.path.join(folder_path, filename)
        with lzma.open(file_path, 'rt', encoding='utf-8') as infile:
            for line in infile:
                text=infile.read()
                outfile.write(line)
                characters = set(text)
                vocab.update(characters)

