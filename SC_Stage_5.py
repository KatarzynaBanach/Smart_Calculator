# Smart Calculator - Hyperskill
# Stage 5

def main():
  while True:
    action = input()

    if action == '':
      continue
    if action[0] == '/':
      if action == '/exit':
        print('Bye!')
        break
      elif action == '/help':
        print('The program calculates the sum or substraction of numbers.')
      else:
        print('Unknown command')
    else:
      try:
        print(eval(action))
      except:
        print('Invalid expression')
main()
