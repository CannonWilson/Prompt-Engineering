from deepface import DeepFace
import os
import csv

CSV_DESTINATION_FILE_NAME = 'diverse_results.csv'
BASE_DIR = 'diverse_generated_images'

with open(CSV_DESTINATION_FILE_NAME, 'a', encoding='utf-8') as f:

    csv_writer_obj = csv.writer(f)
    header = ["phrase", "num", "age", "sex", "race"]
    csv_writer_obj.writerow(header)

    for dir in [dirs for dirs in os.listdir(BASE_DIR) if dirs[0] != "."]:
        for img in [files for files in os.listdir(os.path.join(BASE_DIR, dir)) if files[0] != "."]:
            path = os.path.join(BASE_DIR, dir , img)
            phrase = " ".join(dir.split("_"))
            num = img.split(".")[0]
            try:
                obj = DeepFace.analyze(img_path = path, 
                    actions = ['age', 'gender', 'race']
                )
                found_age, found_sex = obj['age'], obj['gender']
                found_race = max(obj['race'], key=obj['race'].get)
                csv_writer_obj.writerow([phrase, num, found_age, found_sex, found_race])
            except ValueError as e:
                print('Could not find face for path: ' + path)
                csv_writer_obj.writerow([phrase, num, "NA", "NA", "NA"])
