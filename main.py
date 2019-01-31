from parser import Parser

if __name__ == "__main__":
    with open("html/ivy-sc6.html", 'r') as htmlfile:
        parser = Parser(htmlfile.read())
    parser.print_framedata()
