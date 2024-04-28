from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "TheBloke/Mistral-7B-Instruct-v0.2-GGUF"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Function to create a prompt for the model
def user_message(inquiry):
    user_message = (
        f"""
        You are a customer service bot. Your task is to assess customer intent 
        and categorize customer inquiry after <<<>>> into one of the following predefined numbers. This numbers represent answer_class:
11
15
27
21
25
10
2
6
22
3
12
24
26
0
5
17
1
4
14
13
23
8
20
7
18
9
29
16
28
19
0

        If the text doesn't fit into any of the above categories or answer numbers, classify it as:
        999

You will only respond with the predefined answer number do not include the word "Answer number". Do not provide explanations or notes. Provide only number
        ####
Here are some samples. Remember, that this only samples. Inquiry can be different from sample, so you need to understand where as closest as possible sample to the inquiry
What if I want to change group or specialization during my studies? 11
What does the basic training in your personal account consist of?   15
What is included in your school's employment assistance program? What tools or resources will be provided to students?  27
Please tell me the holiday schedule for 2024    21
What tools and resources do you provide for finding a job after graduation? 25
Who checks my submitted work?   10
When will I receive my diploma? 2
What is the sequence of courses in the program? 6
Where can I find information about the schedule of courses and lectures?    22
When did you have to pay for training to get a certificate? 3
How can I correct the "not accepted" rating?    10
How to submit homework on the platform? 12
What programs and tools do I need to become a tester?   24
How can I get help with employment? 26
Where can I find out about documents or certificates after completing training? 0
Where are weinar broadcasts?    5
I do not want to receive notifications from your platform. How to disable them? 17
When will the schedule be available?    6
How to obtain a final education document?   1
How can I set up notifications for upcoming lessons on my profile?  17
Can I get a diploma on paper?   4
How can I find a list of courses that I must take as part of my studies?    14
What is included in the basic training at LC?   15
How long will I study?  13
What programs and tools do I need to become a programmer?   23
What is a consultation? 8
What does employment assistance include?    27
What is the difference in structure and duration between a professional retraining program and an advanced training program?    20
Can I expect lessons to be interactive and include opportunities to ask questions?  7
Where do the lessons take place?    5
Does your training program include activities or resources to assist with post-training employment? 25
How to pick up a diploma?   4
How to add information about yourself to your profile?  18
Where can I find an assignment to complete? 12
What days do classes take place?    22
When will the webinar recording be available?   9
My IRS refuses to accept your school's agreement. What should I do? 29
What document will I receive after training?    0
From what date does the training period begin for possible transfers?   11
How are the courses taught? 7
What are the main differences between a professional retraining program and an advanced training program?   20
Are the courses in the Individual tab required? 16
What is the difference between the Specialist and Experienced Specialist programs?  13
How to start studying?  14
I am a student studying the Testing Specialization on your platform. Can you suggest which programs should I install for effective learning?    24
What are the courses that are in the "Individual" tab?  16
I want to transfer to another group, how do I do this?  11
How to get help with employment?    26
I would like to know what program requirements are required for the Programmer specialization?  23
What documents do I need to provide to receive my diploma?  2
Where on the GeekBrains website can I find a list of courses that I should take?    14
Where can I find recordings of past webinars?   9
Can I retake the paper again if I missed the retake deadline?   10
Can I get a tax deduction for your training?    28
Can you tell us more about how the training program is structured?  19
What training formats are there?    8
Under what conditions can I obtain a certificate?   3
Is it possible to get a diploma without passing intermediate and final certifications?  1
What accreditations or credentials can I expect to receive upon completion of my training?  0
What should I do if I was unable to attend the online lesson?   9
Will there be holidays in GB this year? 21
How do I enable lesson notifications for my account?    17
How to get to the lesson?   5
What needs to be done to receive a document after training? 1
Is it possible to get a tax deduction for taking your courses?  28
How can I add information about myself to my account?   18
What assignment delivery options are available? 12
What actions should you take if the tax office refuses to accept an agreement with your school? 29
        ###
        <<<
        Inquiry: {inquiry}
        >>>
        """
    )
    return user_message


def classify_inquiry(inquiry):
    input_ids = tokenizer.encode(inquiry, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(input_ids, max_length=50, temperature=0.7)

    response = tokenizer.decode(output[0], skip_special_tokens=True).strip()

    return response

