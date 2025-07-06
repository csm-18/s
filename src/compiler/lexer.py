
# Token Types
token_types = {
    "string":1,
    "error":2,
}


class Token:
    def __init__(self, type: int, value: str, start_index: int):
        self.type = type
        self.value = value
        self.start_index = start_index

    def __repr__(self):
        return f"Token(type={self.type}, value='{self.value}', start_index={self.start_index})"


def lexer(code:str):
    tokens = []

    x = 0
    while(x < len(code)):
        if(x+1 < len(code) and code[x:x+2] == "//"):
            found_newline = False

            y = x+2
            while (y < len(code)):
                if(code[y] == '\n'):
                    found_newline = True
                    break
                y+=1

            if(found_newline):
                x = y
                continue
            else:
                break    
        elif(code[x] == '"'):
            found_end_quote = False

            y = x+1
            while(y < len(code)):
                if(code[y] == '"'):
                    found_end_quote = True
                    break
                y+=1

            if(found_end_quote):
                temp = Token(type=token_types["string"],value=code[x:y+1],start_index=x)
                tokens.append(temp)
                x = y+1
                continue
            else:
                temp = Token(type=token_types["error"],value="Unclosed string literal",start_index=x)
                tokens.append(temp)
                break

        x += 1


    return tokens