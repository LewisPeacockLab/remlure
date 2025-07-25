import os
import csv

# Root images folder (absolute path for finding files)
images_root = "/Users/cnj678/Documents/GitHub/remlure/stimuli/images"

# Folder where CSVs will be saved (relative to where you run the script)
csv_output_folder = "/Users/cnj678/Documents/GitHub/remlure/stimuli//csvs/master"

# Prefix to add to paths to make them relative to your repo
relative_prefix = "stimuli/images"

# Make sure the CSV output folder exists
os.makedirs(csv_output_folder, exist_ok=True)

# Categories
categories = ["faces", "places", "fruits"]

for category in categories:
    category_folder = os.path.join(images_root, category)
    csv_filename = os.path.join(csv_output_folder, f"{category}_master.csv")

    # List all files in the category folder
    files = [
        f
        for f in os.listdir(category_folder)
        if os.path.isfile(os.path.join(category_folder, f))
    ]

    # Sort to make output deterministic
    files.sort()

    # Write to CSV
    with open(csv_filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for filename in files:
            # Make path like: stimuli/images/places/360_bridge.png
            relative_path = os.path.join(relative_prefix, category, filename)
            writer.writerow([relative_path])

    print(f"Created {csv_filename} with {len(files)} entries.")

print("All CSVs created in the 'master' folder with relative paths.")
