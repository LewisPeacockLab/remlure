import csv
import os
import random

# Folder where your master CSVs are stored
csv_input_folder = "/Users/cnj678/Documents/GitHub/remlure/stimuli/csvs/master"

# Categories to read
categories = ["faces", "places", "fruits"]

# Dictionary to hold lists of image paths
image_paths = {}

for category in categories:
    csv_filename = os.path.join(csv_input_folder, f"{category}_master.csv")

    with open(csv_filename, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        # Read each row (each row has a single column: the path)
        paths = [row[0] for row in reader]
        image_paths[category] = paths

    print(f"Read {len(paths)} paths from {csv_filename}")

# Create mainTask lists and remove selected images
mainTask = {}

for category in categories:
    all_paths = image_paths[category]

    # Randomly select 19 images
    selected = random.sample(all_paths, 19)

    # Add to new list
    mainTask[f"{category}_mainTask"] = selected

    # Remove these images from the original list
    image_paths[category] = [p for p in all_paths if p not in selected]

    print(f"\n{category}_mainTask ({len(selected)} images):")
    print(selected[:3], "...")  # show first 3 as example
    print(f"Remaining in image_paths[{category}]: {len(image_paths[category])}")

print("\nDone selecting images!")

# ----------------------
# Save to CSV files
# ----------------------

# Output folder for CSVs
output_folder = "/Users/cnj678/Documents/GitHub/remlure/stimuli/csvs/main_task"

# Make sure it exists
os.makedirs(output_folder, exist_ok=True)

for category in categories:
    # Save mainTask images
    mainTask_list = mainTask[f"{category}_mainTask"]
    mainTask_csv = os.path.join(output_folder, f"{category}_mainTask.csv")

    with open(mainTask_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for path in mainTask_list:
            writer.writerow([path])

    print(f"Wrote {len(mainTask_list)} paths to {mainTask_csv}")

    # Save leftover images as novel
    novel_list = image_paths[category]
    novel_csv = os.path.join(output_folder, f"{category}_novel.csv")

    with open(novel_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for path in novel_list:
            writer.writerow([path])

    print(f"Wrote {len(novel_list)} paths to {novel_csv}")

print("\nAll CSVs created successfully!")
