# Read .xml file and putlines row_name and Product ID into new .txt file
search = 'domain'

#source file
with open('domains.xml') as f1:
    #output file
    with open('hardDriveSummary.txt', 'wt') as f2:
        lines = f1.readlines()
        for i, line in enumerate(lines):
            if line.startswith(search):
                f2.write("\n" + line)

#count how many occurances of 'Product ID' in .txt file
def main():

    file  = open('domains.xml', 'r').read()
    word  = "domain"
    count = file.count(word)

    print(count)

main()
