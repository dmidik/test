import random
import prompt

LOWER_LIMIT = 1
UPPER_LIMIT = 10
DESCRIPTION = 'What is the result of the expression?'

def main():
    logic()

  
def calc():
    random_number1 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    random_number2 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    operator = ['-', '+', '*']
    op = random.choice(operator)
    question = (f'{random_number1} {op} {random_number2}')
    answer = str(eval(question))
    return question, answer


def logic():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(DESCRIPTION)
    index = 0
    raund = 3

    while index < raund:
      question = calc()
      random_number1 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
      random_number2 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
      operator = ['-', '+', '*']
      op = random.choice(operator)
      question = (f'{random_number1} {op} {random_number2}')
      answer = str(eval(question))
      print(f'Question: {question}')
      user_answer = prompt.string('Your answer: ')
      if user_answer == answer:
            print('Correct!')
      else:
        print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was {answer}.")
        print(f'Let\'s try again, {name}!')
        return
      index = index + 1
      print(f'Congratulations, {name}!')
     
if __name__ == '__main__':
    main()