import sys  # Import sys module
from stats import print_book_stats

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    # Check if sys.argv has exactly 2 entries (script name + book path)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with status code 1
    
    # Use the second argument as the book path
    book_path = sys.argv[1]
    
    try:
        text = get_book_text(book_path)
        print_book_stats(text, book_path)
    except FileNotFoundError:
        print("Error: The file could not be found")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
