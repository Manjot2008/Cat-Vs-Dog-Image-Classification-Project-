from PIL import Image
import os

folders = [
    "dataset/train/cats",
    "dataset/train/dogs",
    "dataset/test/cats",
    "dataset/test/dogs"
]

deleted = 0

for folder in folders:

    for filename in os.listdir(folder):

        path = os.path.join(folder, filename)

        try:
            with Image.open(path) as img:
                img.verify()

        except Exception:
            print(f"Deleting corrupted image: {path}")

            try:
                os.remove(path)
                deleted += 1
            except:
                pass

print(f"\nDataset cleaned successfully!")
print(f"Total corrupted images removed: {deleted}")