def check_parentheses(lines):
    results = []
    
    for line in lines:
        stack = []
        result_line = list(line)
        markers = [' '] * len(line)
        
        for i, char in enumerate(line):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    markers[i] = '?'
        
        while stack:
            markers[stack.pop()] = 'x'
        
        results.append("".join(result_line))
        results.append("".join(markers))
    
    return results
