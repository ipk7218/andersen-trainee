# Answer the questions
# Given bracket sequence: [((())()(())]] 
# Can this sequence be considered correct? 
# No, this is can't be considered correct.

# If the answer to the previous question is “no”, then what needs to be changed in it to make it correct? 
def BracketsFixer(brackets):
    fixed_brackets = '' # create resulted string
    
    if brackets[0] != '[' or brackets[len(brackets)-1] != ']':
        print('Error. The brackets musst have start "[" and end "]"') # main condition
    else:
        left_round_bracket = 0
        right_round_bracket = 0
        left_quad_bracket = 0
        right_quad_bracket = 0
        trash = 0
        for i in range(len(brackets)): # checking brackets, and special for "[", "]"
            if brackets[i] == '[':
                if i > 0:
                    trash += 1
                left_quad_bracket += 1    
            elif brackets[i] == ']':
                if i < len(brackets)-1:
                    trash += 1
                else:
                    right_quad_bracket += 1
            elif brackets[i] == '(':
                left_round_bracket += 1    
            elif brackets[i] == ')':
                right_round_bracket += 1
            else:
                trash += 1  # trsh, if other symbols
            if left_quad_bracket > 1 or right_quad_bracket > 1 or trash > 0:
                if left_quad_bracket - right_quad_bracket > 0: # if need right side, then...
                    fixed_brackets += ')'
                else:
                    fixed_brackets += '('
                # костыль в виде аннулирования, хотя можно было попробовать счётчик перевести в флажки
                left_quad_bracket = 0
                right_quad_bracket = 0
                trash = 0
            else: 
                fixed_brackets += brackets[i]
    print(fixed_brackets)

#tests
BracketsFixer('[((())()(())]]') # [((())()(()))]
BracketsFixer('[((())()9())]]') # [((())())())(]
BracketsFixer('[(([[(]]))()(())]]') # [(())((())()(())(]
BracketsFixer(')(([[(]]))()(())]]') # Error. The brackets musst have start "[" and end "]"
