# Loops(for, while)


# for-loop:
# n= 0
# for i in range(5):
#     print(i)
# print(n)


# for i in range(5,10):
#     print(i)

# steps to jump
# for i in range(2,11,2):
#     print(i)

# reverse number print
# for i in range(10,1,-2):
#     print(i)

# countries = ["japan","nepal","india"]

# for country in countries:
#     print(country)

# predection_score = [77,99,23,67]
# for score in predection_score:
#     if score>80:
#         print(f"Good score {score}")
#     else:
#         print(f"Bad score {score}")



email_list = [
    "Bhatbhateni ma discount",
    "yeti airelines free ticket congrats jityo",
    "what is the project update guys",
    "Congratulations, you won rolex watch"
]

for mail in email_list:
    # print(mail)
    if "congrats" in mail or "Congratulations" in mail or "discount" in mail:
        print("Spam mail: ",mail)
    else:
        print("Not spam: ",mail)
