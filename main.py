from _datetime import datetime


def main():
    valid_words = get_initial_words()
    print(f"{len(valid_words)} five letter words with unique characters and no more than two vowels")

    words_by_letter = wordlist_to_map(valid_words)

    # figure out the least-popular letters
    # display_words_by_letter(words_by_letter)

    with open("success.txt", "w") as success:
        # only 53 valid words contain a 'q', and 168 contain a 'j'. At least one of these two letters MUST be used.
        starting_words = set(words_by_letter['q'] + words_by_letter['j'])

        for i, word in enumerate(starting_words):
            # start with an empty set, and try to pick each q/j word as the first word in the set
            result = try_pick((), word, valid_words, words_by_letter)
            if result:
                print(f"{i}/{len(starting_words)} Yahoo! {result}")
                success.write(f"{result}\n")
            else:
                print(f"{i}/{len(starting_words)} No Matches: {word}")


def display_words_by_letter(words_by_letter):
    for letter, list in sorted(words_by_letter.items(), key=lambda tup: len(tup[1])):
        print(f"{letter}: {len(list)}")


def get_initial_words():
    valid_words = []
    with open("dict.txt") as file:
        for line in file:
            word = line.strip().lower()
            if len(word) != 5:
                continue
            if not has_unique_letters(word):
                continue
            # a word must contain a unique vowel
            # if any word in the set contains 3+ vowels, there won't be enough for the other 4 words
            if vowel_count(word) > 2:
                continue
            valid_words.append(word)
    return valid_words

def has_unique_letters(word: str) -> bool:
    return len(word) == len(set(word))


def vowel_count(word: str) -> int:
    count = 0
    for letter in word:
        if letter in 'aeiouy':
            count += 1
    return count


def try_pick(alredy_selected, new_word, candidates, words_by_letter):
    """
    Recursively searches "candidates" for a set of 5 words with 25 unique letters
    :param alredy_selected: the current list of unique words, excluding new_word
    :param new_word: the word to add to memo
    :param candidates: a set of valid words, none of which contain any letters used in memo
    :param words_by_letter: a map of each english letter to a list of candidate words that contain that letter
    :return: returns either None if there is no valid solution, or a tuple of 5 words with 25 distinct characters
    """

    # create a new memo by adding our new word
    new_selected = alredy_selected + (new_word,)

    # check to see if we're done
    if len(new_selected) == 5:
        return new_selected

    # create a new set of valid candidates, then remove each word that shares a letter with new_selected
    remaining_candidates = set(candidates)
    for letter in new_word:
        remaining_candidates = remaining_candidates.difference(words_by_letter[letter])

    # if there aren't enough candidate words left, give up
    if len(remaining_candidates) + len(new_selected) < 5:
        return None

    # create a new map of letters -> word-containing-that-letter
    remaining_words_by_letter = wordlist_to_map(remaining_candidates)

    # for each candidate remaining, recurse
    for candidate in remaining_candidates:
        result = try_pick(new_selected, candidate, remaining_candidates, remaining_words_by_letter)
        if result:
            return result
    # if none of our candidates were fruitful, signal that upwards
    return None


def wordlist_to_map(wordlist):
    words_by_letter = {l: [] for l in "abcdefghijklmnopqrstuvwxyz"}
    for word in wordlist:
        for letter in word:
            words_by_letter[letter].append(word)

    return words_by_letter


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(datetime.now().strftime("%H:%M:%S"))
    main()
    print(datetime.now().strftime("%H:%M:%S"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
