"""
main.py 
Gino Mangini
CS 2420
"""

from hashmap import HashMap

def clean_line(raw_line):
    '''removes all punctuation from input string and
    returns a list of all words which have a
    length greater than one '''
    if not isinstance(raw_line, str):
        raise ValueError("Input must be a string")
    line = raw_line.strip().lower()
    line = list(line)
    for index in range(len(line)): # pylint: disable=C0200
        if line[index] < 'a' or line[index] > 'z':
            line[index] = ' '
    cleaned = "".join(line)
    words = [word for word in cleaned.split() if len(word) > 1]
    return words

def main():

    dictionary = HashMap()
    data = open('AliceInWonderland.txt', encoding="utf8")

    for line in data:
        new_line = clean_line(line)
        for word in new_line:
            dictionary.set(word, dictionary.get(word, 0) + 1)
    keys = dictionary.keys()
    list_keys = []
    for i in keys:
        list_keys.append((i, dictionary.get(i)))
    list_keys.sort(key=lambda x: x[1], reverse=True)
    top = list_keys[:15]
    print("The most common words are:")
    for item in top:
        print(item[0], end="\t\t")
        print(item[1])

if __name__ == "__main__":
    main()
