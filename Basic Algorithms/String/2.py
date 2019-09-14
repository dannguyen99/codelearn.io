from string import ascii_uppercase


def amendTheSentence(s):
    positions = [0, ]
    for i in range(len(s)):
        if s[i] in ascii_uppercase and i != 0:
            positions.append(i)
    words = []
    for i in range(len(positions) - 1):
        words.append(s[positions[i]:positions[i + 1]])
    words.append(s[positions[len(positions) - 1]:])
    return " ".join(words).lower()
