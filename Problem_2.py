#Creating the list for test scores and Calc the sum and average and
#Adding new score and finding their sum and average

scores = [70,80,85,90,95]
total = sum(scores)
print("Sum of scores:",total)
average = total / len(scores)
print("Average:",average)
def new_score():
    new_score = int(input("Enter the new score:"))
    scores.append(new_score)
    total = sum(scores)
    print("New sum of Scores:",total)
    average = total / len(scores)
    print("New Average of Scores:",average)
       

new_score()
        

    


