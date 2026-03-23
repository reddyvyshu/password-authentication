sentences = [
    "Heyyyy!!! how r u 😂😂",
    "I canttt believe this!!!",
    "LOL!!! this is sooo funny 😆",
    "Gud mrng!!! hv a nyc day",
    "Wht r u doin??",
    "OMG!!! unbelievable 😱",
    "Thnks alottt bro",
    "C u soon!!!",
    "This is gr8!!!",
    "Yessss!!! finally done 🎉"
]

for sentence in sentences:
    print(sentence)
    slang = any(word in sentence.lower() for word in ["r", "u", "hv", "gr8", "c"])
    emoji = any(char in sentence for char in "😂😆😱🎉")
    typo = any(char*3 in sentence for char in set(sentence))
    print(slang, emoji, typo)

print("lowercase, remove punctuation, remove emojis, spelling correction, remove stopwords")
