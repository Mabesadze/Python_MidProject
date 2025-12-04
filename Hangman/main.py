# Hangman
# Hangman არის სიტყვების გამოცნობის თამაში. პროგრამა ირჩევს შემთხვევით სიტყვას წინასწარ განსაზღვრული სიიდან 
# და აჩვენებს მას ქვედა ტირეების გამოყენებით (რამდენი ასოცაა სიტყვაში, იმდენი ქვედა ტირე), რომელიც წარმოადგენს 
# ფარულ ასოებს. მომხმარებლებს სთხოვენ გამოიცნონ ასო და პროგრამა ამოწმებს არის თუ არა ასო სიტყვაში. 
# ვლინდება სწორად გამოცნობილი ასოები და თამაში გრძელდება მანამ, სანამ მომხმარებელი არ გამოიცნობს სიტყვას ან 
# არ ამოიწურება მცდელობები.

import random
from typing import List, Set, Dict

# შემოვიტანე ქართული ანბანი, რის მიხედვითაც გამოვრიცხავ ლათინურ ასოებსა და რიცხვებს
GEORGIAN_ALPHABET = set("აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ")

# ლოკალურად განსაზღვრული სიტყვების ლექსიკონი თავისი კატეგორიებით
WORDS_AND_HINTS: List[Dict[str, str]] = [ 
    {"word": "ვაშლი", "hint": "ხილი"},
    {"word": "ბანანი", "hint": "ხილი"},
    {"word": "ბალი", "hint": "ხილი"},
    {"word": "გარგარი", "hint": "ხილი"},
    {"word": "ფორთოხალი", "hint": "ხილი"},
    {"word": "მანგო", "hint": "ხილი"},
    {"word": "ჯინი", "hint": "ალკოჰოლური სასმელი"},
    {"word": "ვისკი", "hint": "ალკოჰოლური სასმელი"},
    {"word": "არაყი", "hint": "ალკოჰოლური სასმელი"},
    {"word": "ღვინო", "hint": "ალკოჰოლური სასმელი"},
    {"word": "ძაღლი", "hint": "შინაური ცხოველი"},
    {"word": "კატა", "hint": "შინაური ცხოველი"},
    {"word": "ძროხა", "hint": "შინაური ცხოველი"},
    {"word": "ღორი", "hint": "შინაური ცხოველი"},
   
]

def main():
   
    if not WORDS_AND_HINTS:
        print("შეცდომა: სიტყვების სია ცარიელია. თამაშის დაწყება შეუძლებელია.")
        return
 
    # სიტყვის არჩევა
    chosen_word: Dict[str, str] = random.choice(WORDS_AND_HINTS)
    word: str = chosen_word["word"]
    hint: str = chosen_word["hint"]
   
    print("მოგესალმებით Hangman თამაშში!")
 
    # სიტყვის გამოსახვა
    while True:
        guessed_word_list: List[str] = ["_"] * len(word)
        max_attempts = 5
        wrong_guesses = 0
        # დარჩენილი მცდელობები
        left_attempts = max_attempts-wrong_guesses
        guessed_letters: Set[str] = set()
        hint = False  
 
        print(f"სიტყვა შედგება {len(word)} ასოსგან. თქვენ გაქვთ {max_attempts} მცდელობა.")
 
        while left_attempts > 0 and '_' in guessed_word_list:
            print("\nსიტყვა:" + " ".join(guessed_word_list))
            print(f"დარჩენილი მცდელობები: {left_attempts}")
            # მენიუ
            print("\n მენიუ:")
            print("  1. გამოიცანი ასო")
            print("  2. გამოიცანი სიტყვა")
            if not hint and left_attempts > 1:
                print("  3. მიიღე მინიშნება")
           
            menu = input("\nაირჩიეთ სასურველი მოქმედება: ")
           
            if menu == '1':
                # ასოს გამოცნობა
                guess = input("გამოიცანით ასო: ")
 
                if len(guess) != 1:
                    print("გთხოვთ შეიყვანოთ ერთი ასო.")
                    continue
                elif guess not in GEORGIAN_ALPHABET:
                    print("გთხოვთ შეიყვანოთ მხოლოდ ქართული ასობგერა (რიცხვები და ლათინური ასოები არ დაიშვება).")
                    continue
                elif guess in guessed_letters:
                    print("ეს ასო უკვე გამოყენებულია. სცადეთ სხვა.")
                    continue
                elif guess not in word:
                    left_attempts -= 1
                    print(f"ასო '{guess}' არ არის სიტყვაში. დარჩენილი მცდელობები: {left_attempts}")                
                else:
                    print(f"გილოცავ! ასო '{guess}' არის სიტყვაში.")
                    for index, letter in enumerate(word):
                        if letter == guess:
                            guessed_word_list[index] = guess
                guessed_letters.add(guess)
                   
            elif menu == '2':
                # სრული სიტყვის გამოცნობა
                word_guess = input("შეიყვანეთ სიტყვა: ")
               
                if word_guess == word:
                    guessed_word_list = list(word)
                    attempts_used = max_attempts - left_attempts
                    print(f"გილოცავ შენ გამოიცანი სიტყვა! '{word}' {attempts_used} მცდელობით.")
                    print("მადლობა თამაშისთვის. ნახვამდის!")
                    return
                else:
                    left_attempts -= 1
                    print("არასწორი სიტყვა!")
                   
            elif menu == '3' and not hint and left_attempts > 1:
                # მინიშნის მიღება
                hint = chosen_word["hint"]
                left_attempts -= 1
                print(f"მინიშნება: კატეგორია არის '{hint}'")
            else:
                print("მენიუ შედგება მხოლოდ სამი მოქმედებისგან. სცადეთ თავიდან.")
 
        print("სამწუხაროდ, მცდელობები ამოიწურა. თამაში დასრულდა.")
        print(f"სწორი სიტყვა იყო: '{word}'")
        print("მადლობა თამაშისთვის. ნახვამდის!")
        return
           
if __name__ == "__main__":
    main()
