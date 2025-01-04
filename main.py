
def count_words(string: str) -> int:
    return len(string.split())

def get_character_frequency(string: str) -> dict[str, int]:
    frequency = {}
    string = string.lower()
    for char in string:
        if not char.isalpha():
            continue
        if not char in frequency:
            frequency[char] = 0
        frequency[char] += 1

    return dict(sorted(frequency.items(), reverse=True, key=lambda item: item[1]))

if __name__ == "__main__":
    path_to_book = "books/frankenstein.txt"
    
    with open(path_to_book) as f:
        file_contents = f.read()
    
    print(f"--- Begin report of {path_to_book} ---")
    print(f"{count_words(file_contents)} words found in the document")
    
    character_frequency = get_character_frequency(file_contents)
    for char in character_frequency:
        print(f"The '{char}' character was found {character_frequency[char]} times")
    
    print(f"--- End report ---")
