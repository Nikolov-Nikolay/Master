most_powerful_word_counter = 0
most_powerful_word = 0
while True:
    word = input()

    if word == 'End of words':
        break

    current_counter_of_chars = 0

    for ch in word:
        current_counter_of_chars += ord(ch)

    if word[0].lower() in 'aeiouy':
        current_counter_of_chars *= len(word)
    else:
        current_counter_of_chars = int(current_counter_of_chars / len(word))

    if current_counter_of_chars > most_powerful_word_counter:
        most_powerful_word_counter = current_counter_of_chars
        most_powerful_word = word

