# Enter your NTA scores here (don't enter 100 for everything)
NTA_scores = [float(input("Enter Physics NTA score: ")),
              float(input("Enter Chemistry NTA score: ")),
              float(input("Enter Mathematics NTA score: ")),
              float(input("Enter Total NTA score: "))]


def is_possible(total_candidates: int, NTA_score: float) -> bool:
    # Number of candidates with a score greater than you (IF 'total_candidates' is valid)
    better_candidates = round(total_candidates * (1 - NTA_score / 100))

    # Check if the value of 'total_candidates' gives 'NTA_score' to 7 digit precision
    return round((1 - better_candidates / total_candidates) * 100, 7) == NTA_score


# List of all possible values of (Total number of candidates appeared in the “session”)
possible_totals = list(range(1, 12_00_000))

for NTA_score in NTA_scores:
    refined = []  # A filtered list with values that are from 'possible_totals' and are also possible with the new NTA score
    for total in possible_totals:
        if is_possible(total, NTA_score):
            refined.append(total)
    possible_totals = refined  # Updating possible_totals to be more precise

print()
print("POSSIBLE TOTAL CANDIDATES:", possible_totals)
print()

# After this, it is all aesthetics and rank display

print("POSSIBILITIES")

data = [["Total people appeared in this shift",
         "Physics shift rank",
         "Chemistry shift rank",
         "Mathematics shift rank",
         "Total shift rank"]]

for possible in possible_totals:
    data.append([str(possible)])
    for NTA_score in NTA_scores:
        better = round(possible * (1 - NTA_score / 100))
        data[-1].append(str(better + 1))

max_lens = [max(len(row[i]) for row in data) for i in range(5)]


def line():
    text = '+'
    for max_len in max_lens:
        text += '-' * (max_len + 2)
        text += '+'
    print(text)


def display_row(row: list):
    text = '| '
    for length, item in zip(max_lens, row):
        text += item
        text += ' ' * (length - len(item))
        text += ' | '
    print(text)


line()
display_row(data[0])
line()
for row in data[1:]:
    display_row(row)
line()

print()
print("NOTE")
print("The accurate row should be the first one (with little above 1 lakh total people)")
print("If this is not the case, the NTA scores are unable to accurately determine anything")
print("Usually hapens when 3 or more scores are 100")
print("If you face this issue, you can replace a 100 score with any other NTA score by someone else in the same shift")
print()

input("Enter to quit")
