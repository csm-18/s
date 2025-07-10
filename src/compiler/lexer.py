


# Token Types
token_types = {
    "string":1,
    "error":2,
    "left_paren":3,
    "right_paren":4,
    "left_brace":5,
    "right_brace":6,
    "identifier":7,
    "reserved_word":8,
}

# Reserved-words
reserved_words = ['fn','log','main']

number_symbols = ['0','1','2','3','4','5','6','7','8','9','.']
identifier_symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                      'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                      '_''0','1','2','3','4','5','6','7','8','9','.']
def is_identifier_symbol(text:str)->bool:
    for char in text:
        valid = False
        for sym in identifier_symbols:
            if char == sym:
                valid = True
                break
        
        if not valid:
            return False

    return True

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
                temp = Token(type=token_types["error"],value="Unclosed string literal!",start_index=x)
                tokens.append(temp)
                break
        elif(code[x] == '('):
            temp = Token(type=token_types["left_paren"],value=code[x],start_index=x)
            tokens.append(temp)
            x = x+1
            continue
        elif(code[x] == ')'):
            temp = Token(type=token_types["right_paren"],value=code[x],start_index=x)
            tokens.append(temp)
            x = x+1
            continue
        elif(code[x] == '{'):
            temp = Token(type=token_types["left_brace"],value=code[x],start_index=x)
            tokens.append(temp)
            x = x+1
            continue
        elif(code[x] == '}'):
            temp = Token(type=token_types["right_brace"],value=code[x],start_index=x)
            tokens.append(temp)
            x = x+1
            continue
        elif(is_identifier_symbol(code[x])):
            temp_id = ''
            y = x
            while y < len(code) and is_identifier_symbol(code[y]):
                temp_id += code[y]
                y+=1

            if temp_id[0] in number_symbols:
                temp_token = Token(type=token_types['error'],value="Identifiers should not start with numbers!",start_index=x)
                tokens.append(temp_token)
                x = y
                continue
            else:
                is_reserved_word = False
                for reserved_word in reserved_words:
                    if temp_id == reserved_word:
                        is_reserved_word = True
                        break
                
                if is_reserved_word:
                    temp_token = Token(type=token_types['reserved_word'],value=temp_id,start_index=x)
                    tokens.append(temp_token)
                    x = y
                    continue
                else:
                    temp_token = Token(type=token_types['identifier'],value=temp_id,start_index=x)
                    tokens.append(temp_token)
                    x = y
                    continue  
                
                

        x += 1


    return tokens