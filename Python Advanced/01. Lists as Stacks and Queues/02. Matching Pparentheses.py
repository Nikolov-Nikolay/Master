expression = input()

s = []
for i in range(len(expression)):
    if expression[i] == '(':
        s.append(i)

    elif expression[i] == ')':
        start_index = s.pop()
        end_index = i + 1
        print(expression[start_index:end_index])

'''
# Variants 
Is expression valid?
    - stack should be empty at the end
    - better to do the following:
        - when '(' + 1
        - when ')' - 1
        - 0 at the end

(((1123 + 23) => count = 2 - invalid
(1123 + 23)) => count < 0 - invalid
)()( => count = 0, but invalid

'''