
def find_first(grammar):
    first = {}
    for non_terminal in grammar.keys():
        first[non_terminal] = set()

    changed = True
    while changed:
        changed = False
        for non_terminal, productions in grammar.items():
            for production in productions:
                for symbol in production:
                    if symbol in grammar.keys():
                        initial_length = len(first[non_terminal])
                        first[non_terminal] |= first[symbol]
                        if len(first[non_terminal]) != initial_length:
                            changed = True
                        if '' not in first[symbol]:
                            break
                    else:
                        initial_length = len(first[non_terminal])
                        first[non_terminal].add(symbol)
                        if len(first[non_terminal]) != initial_length:
                            changed = True
                        break
                else:
                    first[non_terminal].add('')
    return first

def display_first(first):
    print("FIRST sets:")
    for non_terminal, symbols in first.items():
        print(f"FIRST({non_terminal}) = {symbols}")

def get_grammar():
    grammar = {}
    while True:
        non_terminal = input("Enter non-terminal symbol (or leave blank to finish): ")
        if not non_terminal:
            break
        productions = []
        while True:
            production = input(f"Enter production for {non_terminal} (or leave blank to finish): ")
            if not production:
                break
            productions.append(production)
        grammar[non_terminal] = productions
    return grammar

if __name__ == "__main__":
    print("Enter the grammar:")
    grammar = get_grammar()
    first = find_first(grammar)
    display_first(first)
