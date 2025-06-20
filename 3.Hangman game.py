import random
# import hangamanstages
word_list=["apple","beautiful","potato","mohan","keerthi","sham","carrot","arogyaa","karrot"]
lives=6
chosen_word=random.choice(word_list)
print(chosen_word)#apple
display=[]
for i in range(len(chosen_word)):#01234 
    display +='_'
print(display)
game_over= False
while not game_over:
    guessed_letter=input("Guess a letter :").lower()
    for postion in range(len(chosen_word)):#0,1,2,3,4
        letter=chosen_word[postion]
        if letter==guessed_letter:
            display[postion]=guessed_letter
    print(display)
    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("you Lose")
    if '_' not in display:
        game_over= True
        print("you won")
    # print(hangamanstages.stages[lives])
