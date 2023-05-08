def course_name (ASKING TO ENTER COURSE NAME) course=input (ENTER COURSE NAME)
return course
def std scores(n):
scores=|
for i in range(n): scores.append(int(input(" Enter their score:")))
return scores
def calculate_avg(scores): (FIND THE AVERAGE OF THE COURSE PT 2) sum=0
for i in range (len(scores)):
sum=sum+scores[il
avg=sum/len(scores) return avg
def print_avg(avg,course): (FIND THE AVERAGE OF THE COURSE PT 2) print(" The average test score of"
course." course is:F)
while True:
for i in range(3):
course=course_name®
n=int(input(" How many students
took the test:"))
scores=std_scores(n) (call back to the std score) avg=calculate_avg(scores)

print_avg(avg,course) (let them know their avg) print(N/A)
ch=input(" Do you want to keep going? (YES OR NO) Print:
if(CHOICE="YES": continue
