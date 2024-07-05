num = 6
def guessing_game():
  input_num = int(input("Enter a number: "))
  if input_num == num:
    print("Your Guess Is Correct!")
  elif input_num<num:
    print("your guess is almost there")
  else:
    print("your guess is higher")

guessing_game()
