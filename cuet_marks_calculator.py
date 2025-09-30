import bs4
import requests

# Pass questions id with answers id in a. Simply copy and paste question and answer id from CUET Portal

# Pass candidate's response sheet link in b.

# Pass number of questions before the test.

#Pass lower_limit + number_of_questions in that particular test as upper_limit.

# Pass 0 or 1 in questionid. If number of digits in questionid = number of digits in answer id then pass 1 otherwise pass 0.

def calculate_marks(a,b,lower_limit,upper_limit,questionid):
    answerkey = a.split()
    x = 1
    #answerkey= []
    #while x<len(k):
       # answerkey.append(k[x])
       # x+=2
    loading_url = requests.get(b)
    
    html_text = bs4.BeautifulSoup(loading_url.text,"lxml")
    
    new2 = html_text.select("td.bold")
    
    x= 0
    
    while x<len(new2):
        
        new2[x] = str(new2[x])
        x+=1
    options = []
    answer_given = []
    x = 0
    y = 0
    while x<upper_limit:
        for items in new2:
            if x == upper_limit:
                break
            if len(items) == 32: #subject to change
                options.append(items[17:27])
            elif len(items) == 23:
                answer_given.append(items[17])
                x+=1
            elif "--" in items:
                answer_given.append("--")
                x+=1
            else:
                pass
    answer_given =  answer_given[lower_limit::]
    if questionid == 0:
        answer_options = options
    else:
        

        answer_options = []
        index1 = 0
        for items in options:
            if index1%5 == 0:
                index1+=1
            else:
                answer_options.append(items)
                index1+=1
                
    answer_options = answer_options[lower_limit*4::]
    actual_answer = []
    x = -1
    y = 0
    while y<(upper_limit-lower_limit):
        new4 = answer_given[y]
        if new4 == "--":
            actual_answer.append("--")
            x+=4
            y+=1
        else:
            actual_answer.append(answer_options[int(new4)+x])
            x+=4
            y+=1
    correct = 0
    wrong = 0
    marks = 0
    correct_answers = []
    wrong_answers = []
    passed_questions = []
    question_number = 1
    for items in actual_answer:
        if items in answerkey:
            correct+=1
            marks+=4
            correct_answers.append(question_number)
            question_number+=1
        elif items == "--":
            pass
            passed_questions.append(question_number)
            question_number+=1
            
        else:
            wrong+=1
            marks-=1
            wrong_answers.append(question_number)
            question_number+=1
            
    print(f"You scored {marks} in this exam")
    print(f"{correct} answers are coreect and {wrong} answers are wrong")
    print(f"Correct answers are {correct_answers}")
    print(f"Wrong answers are {wrong_answers}")
    print(f"You did not attempted these questions - {passed_questions}")

def my_marks(a,b):
    return calculate_marks(a,b,0,75,1)

stats="7311308401 7311308440 7311308444 7311308446 7311308452 7311308454 7311308459 7311308461 7311308465 7311308470 7311308473 7311308405 7311308478 7311308483 7311308486 7311308491 7311308493 7311308498 7311308502 7311308505 7311308510 7311308513 7311308412 7311308520 7311308523 7311308526 7311308529 7311308535 7311308538 7311308541 7311308547 7311308551 7311308553 7311308415 7311308559 7311308562 7311308566 7311308570 7311308573 7311308578 7311308582 7311308586 7311308592 7311308593 7311308418 7311308598 7311308604 7311308605 7311308611 7311308616 7311308619 7311308621 7311308626 7311308629 7311308633 7311308424 7311308638 7311308641 7311308645 7311308651 7311308655 7311308659 7311308662 7311308665 7311308670 7311308675 7311308428 7311308679 7311308683 7311308687 7311308692 7311308695 7311308698 7311308431 7311308435"
response_sheet1="https://cdn3.digialm.com//per/g28/pub/2083/touchstone/AssessmentQPHTMLMode1//2083O2579/2083O2579S1D14025/174220858915148/UP180801541_2083O2579S1D14025E1.html"
print(my_marks(stats,response_sheet1))
