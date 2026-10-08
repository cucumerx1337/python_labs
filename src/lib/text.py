import re

def normalize(text):
    return text.lower()

def tokenize(text):
    return re.findall(r'\b\w+\b', text)

def count_freq(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def top_n(freq, n):
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]
