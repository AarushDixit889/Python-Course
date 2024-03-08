import time
print("Get into quiz of python")
time.sleep(5)
def create_question(question_no,question,options,correct_answer_index):
    print(f"Q{question_no}. {question}")
    options_str=""
    for i in options:options_str+=i+", "
    print("Options are {}\n".format(options_str))
    answer=int(input("Enter your answer number from the options:\t"))
    if correct_answer_index-1==answer-1:
        print("You are right the answer is "+options[correct_answer_index-1])
    else:
        print("Nope, The correct answer is "+options[correct_answer_index-1])


with open("questions.csv","r") as f:
    questions=f.readlines()
    for question in questions:
        question_no,question_name,option1,option2,option3,option4,correct_index=question.split(",")
        create_question(question_no,question_name,[option1,option2,option3,option4],int(correct_index))
        time.sleep(2)