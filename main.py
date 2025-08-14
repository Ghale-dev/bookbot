import sys
def get_book_text(filepath):
	with open(filepath, 'r') as file:
		Frankenstein = file.read()
	return str(Frankenstein)

from stats import get_num_words, count_characters, get_chars_sorted
def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	print(f"============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path} ...")
	print(f"----------- Word Count ----------")
	from pprint import pprint
	book_contents = get_book_text(book_path)
	num_words = get_num_words(book_contents)
	print(f"Found {num_words} total words")
	char_counts = count_characters(book_contents)
	sorted_characters_list = get_chars_sorted(char_counts)
	print(f"--------- Character Count -------")
	for item in sorted_characters_list:
		char = item["char"]
		count = item["num"]
		if char.isalpha():
			print(f"{char}: {count}")
			
	print(f"============= END ===============")    
main()
