from collections import Counter

words = ["Ayodhya and directed the Centre to allot an alternative 5 acre plot\
        to the Sunni Waqf Board for building a new mosque at a prominent place\
        in the holy town in Uttar Pradesh"]
split_word = str(words).split()
print("Splitted Word :",split_word)
words_counts = Counter(split_word)
top_three = words_counts.most_common(3)
print(f"Top three words  {top_three} ")
print(words_counts)
print(top_three)
print(f"Top thre words {top_three}")
