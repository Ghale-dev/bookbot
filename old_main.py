def get_book_text(filepath):
	with open(filepath, 'r') as file:
		Frankenstein = file.read()
	return str(Frankenstein)
            test line

from stats import get_num_words, count_characters
def main():
	book_contents = get_book_text("books/frankenstein.txt")
	num_words = get_num_words(book_contents)
	char_counts = count_characters(book_contents)
	for char, count in char_counts.items():
		print(f"'{char}': {count}")

	print(f"{num_words} words found in the document")
	print(char_counts)
    
main()
