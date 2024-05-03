import csv

# Function to determine if the limerick was guessed to be written by a human or GPT
def lim_type(input):
   if (input == "Human Written"):
      return 0
   elif (input == "GPT Written"):
      return 1

with open("responses.csv") as my_file:
  reader=csv.reader(my_file)

  true_human_predict_human = 0
  true_human_predict_gpt = 0
  true_gpt_3_predict_gpt = 0
  true_gpt_3_predict_human = 0
  true_gpt_4_predict_gpt = 0
  true_gpt_4_predict_human = 0

  for row in reader:
    if (row[1][0:4] != "Pers"):
        correct = row[1][0:4]
    
        # Define the four limericks
        limericks = [ lim_type(row[2]), lim_type(row[3]), lim_type(row[4]), lim_type(row[5])]

        for i in range(4):
            if (correct[i] == '0'):
                if (limericks[i] == 0):
                    true_human_predict_human += 1
                else:
                    true_human_predict_gpt += 1
            elif (correct[i] == '1'):
                if (limericks[i] == 0):
                    true_gpt_3_predict_human += 1
                else: 
                    true_gpt_3_predict_gpt +=1
            else:
                if (limericks[i] == 0):
                    true_gpt_4_predict_human += 1
                else: 
                    true_gpt_4_predict_gpt +=1
        
print(f'true human predict human: {true_human_predict_human}')
print(f'true human predict gpt: {true_human_predict_gpt}')
print(f'true gpt3 predict human: {true_gpt_3_predict_human}')
print(f'true gpt3 predict gpt: {true_gpt_3_predict_gpt}')
print(f'true gpt4 predict human: {true_gpt_4_predict_human}')
print(f'true gpt4 predict gpt: {true_gpt_4_predict_gpt}')
       
        
