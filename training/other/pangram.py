def is_pangram(s):
    alfa = set("abcdefghijklmnopqrstuvwxyz")
    if set(s.lower()) >= alfa:
        return "pangram"
    else:
        return ("not pangram")


test_sentence = "The quick brown fox umps over the lazy dog"
print(is_pangram(test_sentence))