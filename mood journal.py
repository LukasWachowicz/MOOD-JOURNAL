import datetime
import json

def load_words():
    try:
        with open("data.json", "r", encoding= "utf-8") as file:
            return json.load(file)

    except FileNotFoundError:

        return{"positive": [], "negative": []}
words_db = load_words()
POSITIVE_WORDS = words_db["positive"]
NEGATIVE_WORDS = words_db["negative"]

def analyze_sentiment(text):
    #We convert the text to lowercase so that "Happy" and "happy" are the same
    text = text.lower()
    word_is_entry = text.split()
    # We count the occurrences of words
    pos_count = sum(1 for word in POSITIVE_WORDS if word in text)
    neg_count = sum(1 for word in NEGATIVE_WORDS if word in text)

    if pos_count > neg_count:
        return "😊 That sounds like a wonderful day! Keep it up!"
    elif neg_count > pos_count:
        return "😟 I'm sorry to hear that. Tomorrow is a new chance!"
    else:
        return "😐 A neutral day. Sometimes peace is all we need."
#---function of adding a new word
def add_new_words(words_list):
    """Funkcja uczy się nowych słów od użytkownika"""
    for word in words_list:
        word = word.strip(",.!?").lower() # Purification of the word
        if word not in POSITIVE_WORDS and word not in NEGATIVE_WORDS:
            while True:
                chose = input(f"I don't know the word '{word}'. Is it positive(1), negative(2) or skip(s)? ")
                if chose == "1":
                    POSITIVE_WORDS.append(word)
                    break
                elif chose == "2":
                    NEGATIVE_WORDS.append(word)
                    break
                elif chose.lower() == "s":
                    break
                else:
                    print("Wrong choice! Choose 1, 2 or s.")


# --- MAIN PROGRAM LOOP ---
print("--- Welcome to your AI Mood Journal ---")

while True:
    entry = input("\nHow was your day? (Describe it in English or type 'quit' to exit): ")
    
    if entry.lower() == 'quit':
        
        print("Goodbye! See you tomorrow.")
 #saving to a json file
        data_for_write = {
             "positive": POSITIVE_WORDS ,
            "negative": NEGATIVE_WORDS
    
         }

        with open("data.json", "w", encoding= "utf-8") as file:
            json.dump(data_for_write, file, indent=4)

        break
    
    if len(entry) < 5:
        print("❌ Please write a bit more so I can understand you.")
        continue

    result = analyze_sentiment(entry)
    print(f"\nAI Analysis: {result}")
    add_new_words(entry.split())
    # Saving to a txt file
    with open("journal.txt", "a", encoding="utf-8") as file:
        date = datetime.date.today()
        file.write(f"{date}: {entry} -> {result}\n")
        print(" Entry saved to journal.txt")
   
