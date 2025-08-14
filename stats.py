def get_num_words(text):
	words = text.split()
	return len(words)

def count_characters(text):
	char_counts = {}
	for char in text:
		char = char.lower()
		if char in char_counts:
			char_counts[char] += 1
		else:
			char_counts[char] = 1
	return char_counts

def get_chars_sorted(char_counts_dict):
	my_list = []
	for key, value in char_counts_dict.items():
		new_item = {"char": key, "num": value}
		my_list.append(new_item)

	def sort_on(items):
		return items["num"]
	my_list.sort(reverse=True, key=sort_on)
	return my_list
