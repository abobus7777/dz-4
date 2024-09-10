vocabulary = set()


def parrot(phrase):
    global vocabulary
    if phrase in vocabulary:
        print(phrase)
    else:
        vocabulary.add(phrase)


phrase = input('Скажіть будь-що,а я повторю: ').lower()
while phrase:
    parrot(phrase)
    phrase = input('Скажіть другий раз,а я повторю: ').lower()
    print("повторюю:")
