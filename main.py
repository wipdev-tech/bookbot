file_name = "books/frankenstein.txt"

def count_words(s):
    return len(s.split())

def count_letters(s):
    counts = {}
    for l in s.lower():
        if l not in counts:
            counts[l] = 0
        counts[l] += 1
    return counts

def filter_alpha_counts(counts_list):
        counts_filtered = []
        for k, v in counts_list:
            if k.isalpha():
                counts_filtered.append((k, v))
        return counts_filtered

def report_counts(file_name):
    with open(file_name) as f:
        counts_dict = count_letters(f.read())
        counts_list = list(counts_dict.items())
        counts_filtered = filter_alpha_counts(counts_list)
        counts_filtered.sort(key=lambda count: count[1], reverse=True)

        print(f"--- Begin report of {file_name} ---")

        for count in counts_filtered:
            print(f"The '{count[0]}' character was found {count[1]} times")

        print("--- End report ---")



report_counts(file_name)
