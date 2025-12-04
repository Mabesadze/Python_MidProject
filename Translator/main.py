# თარჯიმანი
# თარჯიმანის აპლიკაცია მომხმარებელს საშუალებას აძლევს აირჩიოს ენების წყვილი - რომელი ენიდან რომელ ენეაზე უნდა 
# ითარგმნოს სიტყვები (მაგ: ქართული-ინგლისური, ქართული-რუსული, ინგლისური-ქართული, რუსული-ქართული). 
# ამის შემდეგ მომხმარებელს შეყავს სიტყვა ან მოკლე ფრაზა. პროგრამა კითხულობს თარგმანებს ტექსტური ფაილიდან 
# (ლექსიკონიდან) და აჩვენებს შესაბამის ნათარგმნ სიტყვას ან ფრაზას. იმ შემთხვევაში თუ სათარგმნი სიტყვა არ აღმოჩნდა 
# ლექსიკონში, პროგრამა მომხმარებელს სთავაზობს დაამატოს ამ ახალი სიტყვის თარგმანი ლექსიკონს (ტექსტურ ფაილს).

import os
import json
from typing import Dict

languages = {
    "ka": "ქართული",
    "en": "ინგლისური",
    "ru": "რუსული"
}

folder_path = "translations"

local_data={
    "ka_en.json": {"ვაშლი":"apple", "ბანანი":"banana", "ბანანი ხილია":"Banana is a fruit","ბალი":"cherry", "გარგარი":"apricot", "არაყი":"vodka", "ღვინო":"wine", "ძაღლი":"dog", "კატა":"cat", "ცხენი":"horse", "ძროხა":"cow", "ღორი":"pig",},
    "en_ka.json": {"apple":"ვაშლი", "banana":"ბანანი", "cherry":"ბალი", "apricot":"გარგარი", "vodka":"არაყი", "wine":"ღვინო", "dog":"ძაღლი", "cat":"კატა", "horse":"ცხენი", "cow":"ძროხა", "pig":"ღორი",},
    "ka_ru.json": {"ვაშლი":"яблоко", "ბანანი":"банан", "ბალი":"вишня", "გარგარი":"абрикос", "არაყი":"водка", "ღვინო":"вино", "ძაღლი":"собака", "კატა":"кот", "ცხენი":"лошадь", "ძროხა":"корова", "ღორი":"свинья",},
    "ru_ka.json": {"яблоко":"ვაშლი", "банан":"ბანანი", "вишня":"ბალი", "абрикос":"გარგარი", "водка":"არაყი", "вино":"ღვინო", "собака":"ძაღლი", "кот":"კატა", "лошадь":"ცხენი", "корова":"ძროხა", "свинья":"ღორი",},
}


# ქმნის ფოლდერს და ფაილებს საწყისი მონაცემებით, თუ არ არსებობს
os.makedirs(folder_path, exist_ok=True)
for filename, data in local_data.items():
    file_path = os.path.join(folder_path, filename)
    if not os.path.isfile(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
 
os.makedirs(folder_path, exist_ok=True)
 
# local_data ში არსებულ მონაცემებს წერს შექმნილ ფოლდერში, თუ ფაილი არ არსებობს
def load_translation_dict(filename: str) -> Dict[str, str]:
    
    file_path = os.path.join(folder_path, filename)
 
    if not os.path.isfile(file_path):
        initial = local_data.get(filename, {})
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(initial, f, ensure_ascii=False, indent=4)
        return initial
 
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}
 
 
def select_language() -> str:
    print("\nრომელ ენადან გსურთ თარგმნა?")
    print("1. ქართული → ინგლისური")
    print("2. ინგლისური → ქართული")
    print("3. ქართული → რუსული")
    print("4. რუსული → ქართული")
 
    choice = input("აირჩიეთ (1-4): ").strip()
    mapp = {"1": "ka_en.json", "2": "en_ka.json", "3": "ka_ru.json", "4": "ru_ka.json"}
    return mapp.get(choice, "ka_en.json") 
    # განსხვავებული რიცხვის შეყვანისას დეფოლტად აბრუნებს ქართული→ინგლისური ლექსიკონს.
 

# როგორც lower ასევე upper ის შემთხვევაში იპოვოს სიტყვა და სხვა სიტყვად არ აღიქვას
def translate_word(word: str, translation_dict: Dict[str, str]) -> str:
    if word in translation_dict:
        return translation_dict[word]
    lower = word.lower()
    return translation_dict.get(lower)
 
# დამატების ფუნქცია როდესაც სიტყვა არ არის ლექსიკონში 
def add_translation(word: str, translation: str, filename: str, translation_dict: Dict[str, str]):
    translation_dict[word] = translation
    file_path = os.path.join(folder_path, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(translation_dict, f, ensure_ascii=False, indent=4)
 
 
def main():
    filename = select_language()
    translation_dict = load_translation_dict(filename)
 
    while True:
        word = input("\nჩაწერეთ სიტყვა ან მოკლე ფრაზა. \nდასრულებისთვის აკრიფეთ 'exit': ").strip()
        if word.lower() == "exit":
            break
 
        result = translate_word(word, translation_dict)
        if result:
            print(f"თარგმანი: {result}")
        else:
            translation = input(f"სიტყვა '{word}' ლექსიკონში არ არის. ახალი სიტყვის დამატებისთვის გაუწერეთ შესაბამისი თარგმანი: ").strip()
            if translation:
                add_translation(word, translation, filename, translation_dict)
                print("ახალი სიტყვის თარგმანი დამატებულია ლექსიკონში")
 
 
if __name__ == "__main__":
    main()


