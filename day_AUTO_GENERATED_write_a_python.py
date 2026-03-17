def contains_pangram(words):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    for word in words:
        if set(word.lower()) >= alphabet:
            return True
    return False

def is_pangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return set(sentence.lower()) >= alphabet

def find_pangrams(sentences):
    return [sentence for sentence in sentences if is_pangram(sentence)]

def main():
    words = ["The quick brown fox jumps over the lazy dog", "Hello world", "Pack my box with five dozen liquor jugs"]
    print(contains_pangram(words))
    print(find_pangrams(words))

if __name__ == "__main__":
    main()