def isValid(s: str) -> bool:
    stack = []
    for i in range(len(s)):
        if s[i] == "(" or s[i] == "{" or s[i] == "[":
            stack.append(s[i])
        if s[i] == ")" or s[i] == "}" or s[i] == "]":        
            if len(stack) == 0:
                return False
            top_stack = stack.pop()
            if s[i] == ")":
                if top_stack == "(":
                    continue
                else: 
                    return False
            elif s[i] == "]":
                if top_stack == "[":
                    continue
                else: 
                    return False
            elif s[i] == "}":
                if top_stack == "{":
                    continue
                else: 
                    return False
    if len(stack) == 0:
        return True
    return False   

print(isValid("{[()]}"))

    