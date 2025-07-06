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

        x += 1


    return tokens