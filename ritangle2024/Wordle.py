import random as r


dictionary = ["apple", "house", "light", "bread", "plant", "water", "grass", "tiger", "chair", "table", "money", "sleep", "world", "cloud", "space", "sweet", "phone", "music", "heart", "green", "stone", "cloud", "river", "laugh", "happy", "angry", "truck", "horse", "apple", "dance", "quick", "swing", "party", "storm", "ocean", "sunny", "silver", "shadow", "peach", "tiger", "lucky", "kingf", "booky", "knife", "honey", "green", "blend", "floor", "peach", "radio", "blood", "heart", "media", "drunk", "grasp", "music", "water", "blend", "swift", "limey", "tree", "plants", "brick", "laugh", "waves", "witch", "stone", "court", "barky", "crisp", "lappy", "smart", "learn", "sound", "magic", "flaty", "turny", "fort", "sharp", "blaze", "cooly", "track", "bread", "hunt", "brand", "clear", "unite", "clean", "dream", "shift", "glass", "watch", "frost", "pasty", "drum", "alien", "clear", "sunny", "forest", "cloudy", "slice", "ship", "rock", "dirt", "clown", "wind", "honest", "worth", "sick", "loud", "raw", "edge", "wave", "party", "cricket", "link", "slice", "print", "chief", "beach"]
num = r.randint(0,100)
actual_word = dictionary [num]

print("-----")

guess = 0
counter = 0
if guess != actual_word:
    while counter != 6:   #checks if guess incorrect
        guess = input("")
        count = 0
        for i in guess:         #loop thru letter

            if i == actual_word[count]:
                print(((i+1) * "-") + i + ((5-i)*"-"))
            count+=1
        counter+=1






