word1 = input("Enter your first word: ").lower().strip()
word2 = input("Enter your Sceond word: ").lower().strip()

count1 = {}
count2 = {}

for word in word1:
    if word in count1:
        count1[word] += 1
    else:
        count1[word] = 1

for word in word2:
    if word in count2:
        count2[word] += 1
    else:
        count2[word] = 1

if len(word1) == len(word2) and count1 == count2:
    print("Anagram")
else:
    print("Not a Anagram")