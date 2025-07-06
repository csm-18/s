from .lexer import lexer

def compile(code:str):
    tokens = lexer(code)
    return tokens