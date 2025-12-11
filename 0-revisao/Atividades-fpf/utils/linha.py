



def linha(texto:str, op:int) -> None:
    tmanho = len(texto)
    if(op == 1 ):
        print("#" * tmanho)
    else:
        print("=" * tmanho)