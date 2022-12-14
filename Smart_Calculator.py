# SMART CALCULATOR - hyperskill

import re
help_mess = 'The program calculates expressions that use +, -, (), /, //, * and allows to save variables.'

def assignment(action, values):
    patter = r'([\S ]*)=([\S ]*)'
    l_side, r_side = re.search(patter, action).groups()
    l_side, r_side = l_side.strip(), r_side.strip()
    if l_side.isalpha():
        if r_side.isdigit():
            values[l_side] = int(r_side)
        else: 
            if r_side.isalpha():
                if r_side in values.keys():
                    values[l_side] = values[r_side]
                else:
                    print('Unknown variable')
            else:
                print('Invalid assignment')
    else: 
        
        print('Invalid identifier')
    
    return values


def calculate(action, values):
    expression = re.findall(r'[\+\-\*\(\)/]|[a-zA-z0-9]+', action)
    to_eval = []

  
    for e in expression:
        if e.isdigit() or e in ['+', '-', '*' , '(', ')', '/']:
            to_eval.append(e)
        else:
            if e in values.keys():
                to_eval.append(str(values[e]))
            elif e.isalpha():
                print('Unknown variable')
                to_eval = []
                break
            else:
                print('Invalid identifier')
                to_eval = []
                break

    if to_eval:
        try:
            print(int(eval(''.join(to_eval))))
        except:
            print('Invalid expression')



def main():
    values = {}
    while True:
        action = input()

        if action == '':
              continue
        elif action[0] == '/':
            if action == '/exit':
                print('Bye!')
                break
            elif action == '/help':
                print(help_mess)
            else:
                print('Unknown command')
        elif action.count('=') > 1:
            print('Invalid assignment')
        elif action.count('=') == 1:
            values = assignment(action, values)
        else:
            calculate(action, values)

            
if __name__ = '__main__':
    main()
