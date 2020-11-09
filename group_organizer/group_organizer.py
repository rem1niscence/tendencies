import sys

# Obtain command line arguments
students_file = sys.argv[1]
topics_file = sys.argv[2]
group_count = sys.argv[3]


def readFile(file_name):
    result = []
    with open(file_name) as fp:
        lines = fp.readlines()
        for line in lines:
            result.append(line.strip())
    return result


students = readFile(students_file)
topics = readFile(topics_file)
