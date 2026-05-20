import os
import shutil
import random

# Source folders
source_cats = "PATH_TO_DATASET_CATS"
source_dogs = "PATH_TO DATASET_DOGS"

# Destination folders
train_cats = "dataset/train/cats"
train_dogs = "dataset/train/dogs"

test_cats = "dataset/test/cats"
test_dogs = "dataset/test/dogs"

# Create folders
for folder in [train_cats, train_dogs, test_cats, test_dogs]:
    os.makedirs(folder, exist_ok=True)

def split_data(source, train, test, split_size=0.8):

    files = os.listdir(source)
    random.shuffle(files)

    split_index = int(len(files) * split_size)

    train_files = files[:split_index]
    test_files = files[split_index:]

    # Move training files
    for file in train_files:
        shutil.move(
            os.path.join(source, file),
            os.path.join(train, file)
        )

    # Move testing files
    for file in test_files:
        shutil.move(
            os.path.join(source, file),
            os.path.join(test, file)
        )

    print(f"Done splitting {source}")

# Split datasets
split_data(source_cats, train_cats, test_cats)
split_data(source_dogs, train_dogs, test_dogs)

print("Dataset split completed successfully!")