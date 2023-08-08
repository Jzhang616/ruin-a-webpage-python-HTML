import re
from bs4 import BeautifulSoup

def repl1(match):
    return match.group()[3:-4] + "<br><br>"

#def repl2(match):

def ruin_a_webpage(filename):
    if re.search(".htm|.html", filename):
        file = open(filename)
        str = file.read()
        result = re.sub("<p*?>(.|\n)*?<\/p*?>", repl1, str)
        soup = BeautifulSoup(result, features="html.parser")
        for match in soup.findAll('span'):
            match.unwrap()
        print(soup)
        f = open("ruined.html", "w+")
        f.write(soup.__str__())
    else:
        return None
    return result



if __name__ == '__main__':
    (ruin_a_webpage("q3.html"))