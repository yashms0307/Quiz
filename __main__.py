class Test:
    def __init__(self):
        self.MCQ={}
        self.Answers={}
        self.Difficulty_level = {}
        self.All_Topic={}
        
    #----------------------------------Admin Place-----------------------------------------
        
#-----------------------------------1. Admin Create Quiz-------------------------------------


    def Create_Quiz(self):
        how_many_topic=int(input("How Many Topic You Want to Add in Quiz: "))#
        for i in range(1,how_many_topic+1):
            topics={}
            question_option={}
            options={}
            d_level={}
            answer={}
            
            input_topic=input("Enter topic\n\n:")#
            self.All_Topic[i]=input_topic
            topics["Topic"]=input_topic
            how_many_question=int(input("How Many Question You Want to Add in Quiz: "))#

            for j in range(1,how_many_question+1):

                question_option={}

                question_option["question"]=input("Enter the question: ")#
                options={}

                option=int(input("How many option in there you want: "))#

                for k in range(1,option+1):

                    options[k]=input("Enter the options: ")#

                question_option["option"]=options

                topics[j]=question_option
                d_level[j]=input("Enter Type of difficulty: ")#
                answer[j]=int(input("Enter correct option: "))#
                
            self.Difficulty_level[i]=d_level
            self.Answers[i]=answer
                

            self.MCQ[i]=topics
            
#------------------------------ Admin Create Quiz Ended ------------------------------



#------------------------------------2. View Quiz Function---------------------------------------

    def View_Quizzes(self):
        if self.MCQ=={}:
            print("------------No Quiz Available------------")
            print("If You Are User Please Come After Some Time\n\nIf You Are a Admin Please Add Quiz First")
        else:
            for type_of_sub in range(1,len(self.MCQ)+1):
                print('Topic',str(type_of_sub)+'.',self.MCQ[type_of_sub]['Topic'])
                print('===================')
                question_counter = 1
                for question_no in range(1,len(self.MCQ[type_of_sub])):
                    print('Q.',str(question_counter)+')',self.MCQ[type_of_sub][question_no]['question'])
                    print('===================')
                    question_counter+=1
                    option_counter = 1
                    for option in self.MCQ[type_of_sub][question_no]['option'].values():
                        print(str(option_counter)+'.',option)
                        option_counter+=1
                    print('\n')
                print('\n')
            
#--------------------------------View Quiz Function End --------------------- 



#------------------------------------3. Edit Quiz Function Start---------------------------------------
            
    def Edit_Quiz(self):
        if self.MCQ=={}:
            print("------------No Quiz Available------------")
            print("--------------Please Add Quiz First--------------")
        else:
            choices = {1:'Topic',2:'Question',3:'Option'}
            for value in choices:
                print(str(value)+'.',choices[value])
            edit=int(input("\n Press 1 for edit topic 2 for edit question and 3 for edit option: "))




            if edit==1:
                for Topic in self.MCQ:
                    print(str(Topic)+'.',self.MCQ[Topic]['Topic'])
                topic_no=int(input("\n Enter the topic no you want to edit"))
                self.MCQ[topic_no]['Topic']=input("Enter topic name: ")




            elif edit==2:
                for value in self.MCQ:
                    print(str(value)+'.',self.All_Topic[value])

                for type_of_sub in self.MCQ:
                    print(str(type_of_sub)+'.',self.MCQ[type_of_sub]['Topic'])
                    print('==================')
                    question_counter = 1
                    for question_no in self.MCQ:
                        print(str(question_counter)+')',self.MCQ[type_of_sub][question_no]['question'])
                        question_counter+=1
                    print()
                topic_no=int(input("\n Enter the topic no you want to edit"))
                Question_no=int(input("\n Enter the question no you want to edit"))
                self.MCQ[topic_no][Question_no]['question']=input("\n Enter the question: ")





            elif edit==3:
                for type_of_sub in self.MCQ:
                    print('Topic',str(type_of_sub)+'.',self.MCQ[type_of_sub]['Topic'])
                    print('===================')
                    question_counter = 1
                    for question_no in self.MCQ:
                        print('Q.',str(question_counter)+')',self.MCQ[type_of_sub][question_no]['question'])
                        print('==========================')
                        question_counter+=1
                        option_counter = 1
                        for option in self.MCQ[type_of_sub][question_no]['option'].values():
                            print(str(option_counter)+'.',option)
                            option_counter+=1
                        print('\n')
                    print('\n')


                topic_no=int(input("\n Enter the topic no you want to edit"))
                Question_no=int(input("\n Enter the question no you want to edit"))
                Option_no=int(input("\n Enter the option no you want to edit"))

                self.MCQ[type_of_sub][question_no]['option'][Option_no]=input("\n Enter the option: ")
            
#--------------------------------Edit Quiz Function End----------------------             
    

    
    
#------------------------------------4. Delete Quiz Function Start--------------------------------------
                
    def Delete_Quiz(self):
        if self.MCQ=={}:
            print("------------No Quiz Available------------")
            print("--------------Please Add Quiz First--------------")
        else:
            for i in range(1,len(self.MCQ)+1):
                del self.MCQ[i]
        
#------------------------------------Delete Quiz Fundtion End---------------------------------------

        
        
#------------------------------------5. Create Topic Function Start---------------------------------------#
            
    def Create_Topic(self):
        keys_len=list(self.All_Topic.keys())
        how_many_topic=int(input("\n Enter the no of topic you want to create: "))
        length_of_key=len(keys_len)
        last=length_of_key+how_many_topic
        
        for i in range(length_of_key+1,last+1):
            self.All_Topic[i]=input("\n Enter topic name: ")

#------------------------------------Create Topic Function End ---------------------------------------

     
#------------------------------------6. View Topic Function Start---------------------------------------

    def View_Topics(self):
        if self.All_Topic=={}:
            print("------------No Topic Available------------")
            print("--------------Please Add Topic First---------------")
        else:
            for value in self.All_Topic:
                print(str(value)+'.',self.All_Topic[value],'\n')
            
#------------------------------------View Topic Function End ---------------------------------------

                
#------------------------------------7. Edit Topic Function Start---------------------------------------
            
    def Edit_Topics(self):
        if self.All_Topic=={}:
            print("------------No Topic Available------------")
            print("--------------Please Add Topic First--------------")
        else:
            for value in self.All_Topic:
                print(str(value)+'.',self.All_Topic[value])
            topic_no=int(input("\n Enter the topic number you want to edit"))
            topic_name=input("\n Enter topic name: ")
            self.All_Topic[topic_no]=topic_name
            self.MCQ[topic_no]['Topic']=topic_name

#------------------------------------Edit Topic Function End ---------------------------------------

    
#------------------------------------8. Delete Topic Function Start ---------------------------------------#    
    
    def Delete_Topics(self):
        for i in range(1,len(self.All_Topic)+1):
            del self.All_Topic[i]
        
#------------------------------------Delete Topic Function End---------------------------------------        
        
        
        
                            #------------User Place----------#
            
#------------------------------------9. User Test Function Start---------------------------------------   

    def user_test(self):
        answerr={}
        if self.MCQ=={}:
            print("------------No Quiz Exist------------")
            print("-- If You Are User Please Come After Some Time --\n\n--If You Are a Admin Please Add Quiz First--")
        else:
            print("================List of Topic Available for Quiz===============")
            for type_of_sub in self.MCQ:
                print('Topic',str(type_of_sub)+'.',self.MCQ[type_of_sub]['Topic'])
            print("Select Topic Number in Which You Want to Take Quiz from Above")
            topic_selection=int(input())
            print("---------------WELCOME TO QUIZ---------------")
            print()
            print("------------------ Best of Luck ------------------")
            question_counter = 1
            storing_answer={}
            for question_no in range(1,len(Admin.MCQ[topic_selection])):
                print('Q.',str(question_counter)+')',self.MCQ[topic_selection][question_no]['question'])
                print('==========================')
                question_counter+=1
                option_counter = 1
                for option in self.MCQ[topic_selection][question_no]['option'].values():
                    print(str(option_counter)+'.',option)
                    option_counter+=1
                print("Difficulty can be",self.Difficulty_level[topic_selection][question_no],'\t',"Topic Could be",self.MCQ[topic_selection]['Topic'])
                print("Choose the correct answer\n")
                storing_answer[question_no]=int(input())

                print('\n')
            answerr[topic_selection]=storing_answer
            print('\n')

            result=Admin.find_percentage(self.Answers,answerr,topic_selection)
            if result is not None:
                correct_answer=result[1]
                question_count_out_of=result[2]
                percentage = result[0]
                topic_selection=result[3]
                format_float_percentage = "{:.2f}".format(percentage)
                user_answer=answerr
                
                for j in self.Answers[topic_selection]:
                    print('Topic No.',' Q.No.','   Correct Answer','\t','Your Answer')
                    print('........','........','.................','\t','..............')
                    print(topic_selection,'   ','      ',j,'      ',self.Answers[topic_selection][j],'        ','\t',user_answer[topic_selection][j])

                print('\n\n\n','Your percent is', format_float_percentage,'\n','Your score',correct_answer,'out of',question_count_out_of)
            
        
#------------------------------------10. Staticmethod Start---------------------------------------

    @staticmethod
    def find_percentage(Answers,user_answerr,topic_selection):
        question_count = 0
        result_count_score = 0
        for j in Answers[topic_selection]:
            question_count+=1
            if Answers[topic_selection][j]==user_answerr[topic_selection][j]:
                result_count_score+=1
                    
        percentage = (result_count_score/question_count)*100#
        
        return percentage,result_count_score,question_count,topic_selection
    
#------------------------------------------------------------------------------------------------
Admin=Test()  


user={}
admin={}
#----------------------------------------11. Login Function Start-----------------------------------------------------------
def login(user_or_admin):
    if user_or_admin=='1':
        username=input("Enter username: ")
        password=input("Enter password: ")
        if username in user:
            if user[username]==password:
                choice_user = {1:'press 1 for Attempt Quizzes',2:'press 2 for logout'}
                while True:
                    for value in choice_user:
                          print('\n ',str(value)+'.',choice_user[value])
                    action=input()
                    if action=='1':
                        Admin.user_test()
                    elif action=='2':
                        action_perform()
                    else:
                        print('Invaild input')
                        login(input("Press 1 for LOGIN as USER and 2 for LOGIN as ADMIN: "))
            else:
                print("\n Invaild Credentials!")
        else:
        	print("We search everywhere in our system but unfortunately username not found please register with us first")
        	register()

    elif user_or_admin=='2':
        username=input("\nEnter username: ")
        password=input("Enter password: ")
        if username in admin:
            if admin[username]==password:
                choice = {1:'press 1 for View Quizzes',2:'press 2 for Create Quiz',
                          3:'press 3 for Edit Quiz',4:'press 4 for Delete Quiz',
                          5:'press 5 for Create Topic',6:'press 6 for View Topics',
                          7:'press 7 for Edit Topics',8:'press 8 for Delete Topics',
                          9: 'press 9 for logout'
                         }
                while True:
                    for value in choice:
                        print('\n ',str(value)+'.',choice[value])
                    action=input()
                    if action=='1':
                        Admin.View_Quizzes()
                    elif action=='2':
                        Admin.Create_Quiz()
                    elif action=='3':
                        Admin.Edit_Quiz()
                    elif action=='4':
                        Admin.Delete_Quiz()
                    elif action=='5':
                        Admin.Create_Topic()
                    elif action=='6':
                        Admin.View_Topics()
                    elif action=='7':
                        Admin.Edit_Topics()
                    elif action=='8':
                        Admin.Delete_Topics()
                    elif action=='9':
                        action_perform()
                    else:
                        print("\n Opp's invalid input! Please try again.\n ")


            else:
                print("\n Invaild Credentials!!")
                login(input("Press 1 for LOGIN as USER and 2 for LOGIN as ADMIN: "))
        else:
        	print("We search everywhere in our system but unfortunately username not found please register with us first")
        	register()


        	
#------------------------------------12. Register Function Start----------------------------------------------------            
def register():       
    user_or_admin=input("Press 1 for register as user \nPress 2 for register as admin: ")
    if user_or_admin=='1':
        username=input("\nEnter username: ")
        password=input("Enter password: ")
        user[username]=password
        login(input("Press 1 for login as user and 2 for login as admin: "))
    elif user_or_admin=='2':
        username=input("\n Enter username: ")
        password=input("Enter password: ")
        admin[username]=password
        login(input("Press 1 for login as user and 2 for login as admin: "))     
        
#-------------------------------13. Action Perform Function Start---------------------------------------------------------           

def action_perform():   
    choice = {1:'press 1 for login',2:'press 2 for register: '}
    print("You have already registerd with us? ")
    print("Then press 1 \nIf you are new user then register with us by clicking 2")
    for value in choice:
        print('\n ....................................... \n')
        print('\n ',str(value)+'.',choice[value])
    choice_input=int(input())
    if choice_input==1:
        login(input("Press 1 for login as user and 2 for login as admin: "))
    elif choice_input==2:
        register()
action_perform()

#---------------------------- End of Code ---------------------------------

 
                     
