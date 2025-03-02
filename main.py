import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    words = count_book_words(text)
    characters = character_count(text)
    char_list = sorted_list(characters)
    print_report(path, words, char_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_book_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    results = {}
    for character in text:
        if character.isalpha() == True:
            character = character.lower()
            if character in results:
                results[character] += 1
            else:
                results[character] = 1
    return results

def sort_by(dict):
    return dict["num"]

def sorted_list(results):
    char_list = []
    for char in results:
        char_list.append({"char": char, "num": results[char]})
    char_list.sort(reverse=True, key=sort_by)
    return char_list

def print_report(path, words, char_list):
    print(f"--- Begin report of {path} ---")
    print(f"{words} were found in the document\n")
    for entry in char_list:
        char = entry["char"]
        num = entry["num"]
        print(f"The '{char}' character was found {num} times")    
    print(f"--- End Report ---")

main()