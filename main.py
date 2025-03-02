import sys
import stats

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    words = stats.count_book_words(text)
    characters = stats.character_count(text)
    char_list = stats.sorted_list(characters)
    print_report(path, words, char_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(path, words, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for entry in char_list:
        char = entry["char"]
        num = entry["num"]
        print(f"{char}: {num}")    
    print("============= END ===============")

main()