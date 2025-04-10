def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words  # Return instead of print, for use in new function

def count_all_chars(text):
    # Convert alphabetic characters to lowercase
    text_lower = ''.join(char.lower() if char.isalpha() else char for char in text)
    # Dictionary for all character counts
    all_counts = {}
    # Count every character
    for char in text_lower:
        all_counts[char] = all_counts.get(char, 0) + 1
    return all_counts

def print_book_stats(text, filepath):
    # Header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    # Word count
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    # Character count
    char_counts = count_all_chars(text)
    print("--------- Character Count -------")
    # Sort by count (descending), then by character (ascending) for ties
    sorted_chars = sorted(char_counts.items(), key=lambda x: (-x[1], x[0]))
    for char, count in sorted_chars:
        print(f"{char}: {count}")
    
    # Footer
    print("============= END ===============")
