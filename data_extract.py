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
output_path="output{}.txt"
vocab_path="vocab.txt"
split_files = int(input("How many files do you want to split into?"))

files = xz_files_in_dir(folder_path)
total_files = len(files)
max_count = total_files // split_files if split_files != 0 else total_files

print(f"Total files: {total_files}")
print(f"Files to split into: {split_files}")
print(f"Max count per split: {max_count}")

vocab = set()

for i in range(split_files):
    with open(output_path.format(i), 'wb') as outfile:
        for count,filename in enumerate(tqdm(files[:max_count],total=max_count)):
            if count>=max_count:
                break
            file_path = os.path.join(folder_path, filename)
            with lzma.open(file_path, 'rt', encoding="utf-8") as infile:
                data = infile.read()
                outfile.write(data.encode('utf-8'))
                vocab.update(data)
        files = files[max_count:]

with open(vocab_path, 'w',encoding = "utf-8") as vfile:
    for char in vocab:
        vfile.write(char + '\n')