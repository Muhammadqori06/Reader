import playsound


def split(word):
    return list(word)


from_user = input("Enter your sentence: ").strip().lower()
new_word = split(from_user)

i = 0

while i < len(new_word):
    if new_word[i].isalpha():
        if i != len(new_word)-1:
            if new_word[i] + new_word[i + 1] == 'ch' or new_word[i] + new_word[i + 1] == 'sh' or \
                    new_word[i] + new_word[i + 1] == 'ng' or new_word[i] + new_word[i + 1] == "g'" or \
                    new_word[i] + new_word[i + 1] == "o'":
                letter = new_word[i] + new_word[i + 1]
                playsound.playsound(f'/home/muhammad/alifbo/{letter}.mp3')
                i += 2
            else:
                playsound.playsound(f'/home/muhammad/alifbo/{new_word[i]}.mp3')
                i += 1
        else:
            playsound.playsound(f'/home/muhammad/alifbo/{new_word[i]}.mp3')
            i += 1
    elif new_word[i] == " ":
        playsound.playsound(f'/home/muhammad/alifbo/ab.mp3')
        i += 1
    else:
        playsound.playsound(f'/home/muhammad/sonlar/{new_word[i]}.mp3')
        i += 1
