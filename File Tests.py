import random
import os
def main():
    path = "C:/Users/mande_000/Desktop"
    file_name = os.path.join(path,"Test.txt")
   # my_file = open(file_name)

    path2 = "C:/Users/mande_000/Desktop"
    answer_file = os.path.join(path2,"Answers.txt")


    correct = 0
    total_questions = 0
    with open(file_name,"r")as ins:
        array = []
        for line in ins:
            array.append(line)
            for q in range(len(array)):
                array[q] = array[q].rstrip()

    with open(answer_file,"r") as outs:
        answer_array = []
        for new_line in outs:
            answer_array.append(new_line)
            for i in range(len(answer_array)):
                answer_array[i] = answer_array[i].rstrip()

    test = random.randint(0,len(array)-1)

    print(answer_array[test])
    x = str(input("Enter your answer here: "))

    if x == answer_array[test]:
        print("Good job!")
    else:
        print("WTF")



main()