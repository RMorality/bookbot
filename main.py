def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
    words = file_contents.split()
    amount_words = len(words)
    letter_count = {}
    for word in words:
        for letter in word:
            if letter.isalpha():
                letter_count[letter] = letter_count.get(letter, 0) + 1
    letters = sorted(letter_count, key=letter_count.get, reverse=True)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"Total words: {amount_words}")
    print("")
    for letter in letters:
        print(f"The '{letter}' character was found {letter_count[letter]} times.")


if __name__ == "__main__":
    main()
