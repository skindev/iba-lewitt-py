import re

line_number = 0

out_fh = open('/Users/skin/repository/iba-lewitt-py/docs/lewitt-corpus/wall_drawing_corpus.csv', 'w')
out_fh.write('title,description\n')

with open('/Users/skin/repository/iba-lewitt-py/docs/lewitt-corpus/wall_drawing_corpus.txt', 'r') as fh:
    for i, line in enumerate(fh):

        # skip blank lines
        if not line.strip():
            continue

        line = line.strip()

        line_number += 1

        line = re.sub('\s+', ' ', line)

        # detect whether the line is a title or a description
        # print('{0}:{1}'.format(i, line))

        # title
        if line_number % 2 == 1:
            title = re.sub('\(|\)', '', line)
            description = None
        else:
            description = line

        if title and description:
            print('{0},{1}'.format(title, description))
            out_fh.write('{0},{1}\n'.format(title, description))

out_fh.close()
if __name__ == "__main__":
    pass