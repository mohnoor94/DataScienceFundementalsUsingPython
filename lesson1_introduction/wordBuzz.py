# objective: return all words that have multiple duplicate letters


def wordbuzz(arr):
    for word in arr:
        counts = {}
        for letter in word:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
        if max(counts.values()) > 1:
            print(word)


input_arr = ['hello', 'world', 'my', 'name', 'is', 'Noor']
wordbuzz(input_arr)
wordbuzz(['hi', 'bad', 'wooooorld!'])
