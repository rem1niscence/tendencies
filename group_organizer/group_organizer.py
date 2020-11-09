import sys
import random

# Obtain command line arguments
students_file = sys.argv[1]
topics_file = sys.argv[2]
group_count = int(sys.argv[3])


def readFile(file_name):
    result = []
    with open(file_name) as fp:
        lines = fp.readlines()
        for line in lines:
            result.append(line.strip())
    return result


students = readFile(students_file)
topics = readFile(topics_file)

# Validate invalid comnbinations
if (group_count > len(students)):
    print("Cannot have more groups than students")
    sys.exit(1)
if (group_count > len(topics)):
    print("Cannot have more groups than topics")
    sys.exit(1)

student_groups_count = len(students) // group_count
students_out = abs((student_groups_count * group_count) - len(students))

topics_per_group_count = len(topics) // group_count
topics_out = abs((topics_per_group_count * group_count) - len(topics))


def assign_matches(matcher_list, counter, group_count):
    result = [[] for _ in range(0, group_count)]
    for x in range(0, counter * group_count):
        rnd_index = random.randint(0, len(matcher_list) - 1)
        item = matcher_list.pop(rnd_index)
        result[x % group_count].append(item)

    # Prevent giving an unfair amount of items
    used_numbers = []

    for x in range(0, len(matcher_list)):
        rnd_index = random.randint(0, len(matcher_list) - 1)
        item = matcher_list.pop(rnd_index)

        while True:
            rand_group = random.randint(0, group_count - 1)
            if rand_group not in used_numbers:
                used_numbers.append(rand_group)
                break

        result[used_numbers[len(used_numbers) - 1]].append(item)

    return result
