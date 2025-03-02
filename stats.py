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