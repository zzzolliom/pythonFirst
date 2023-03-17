



def chek_guess(guess, answer):
    global score
    still_guessing= True
    attempt= 0
    while still_guessing == True  and attempt < 3:
        if guess.lower()==answer.lower():
            score=score+1
            still_guessing = False
            print("Верно")
        else:
            if attempt < 2:
                 guess= input("Еще раз'")
            attempt =attempt+1
    if attempt ==3:
            print(answer)



score=0
guess1=input("Какое самое большое животное?")


chek_guess(guess1,"Кит")
print("Викторина")



guess2=input("Какое животное самое быстрое")
chek_guess(guess2,"Сапсан")
guess3=input("Какое животное живет на северном полюсе?")
chek_guess(guess3,"Белый медведь")
print(score)
