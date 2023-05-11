#!/usr/bin/python3

if __name__ == "__main__":
    
    import hidden_4

    ident = dir(hidden_4)
    for i in ident:
        if i[:2] != "__":
            print(i)
