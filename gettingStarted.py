### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
        if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
            return "pcap"
        elif question == "Are encoding and encryption the same? - Yes/No":
            return "No"
        elif question == "Is it possible to decrypt a message without a key? - Yes/No":
            return "No"
        elif question == "Is it possible to decode a message without a key? - Yes/No":
            return "Yes"
        elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
            return "No"
        elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
            return "50b3b6dba4dfd8d20e4aafa16e7088f67f9107f553eac80ab04ea9591a7d01fa"
        elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
            return "No"
        elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
            return 5
        elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
            return 3
        else: 
            return "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
            
if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    '''
    questions = [
      "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?",
      "Are encoding and encryption the same? - Yes/No",
      "Is it possible to decrypt a message without a key? - Yes/No",
      "Is it possible to decode a message without a key? - Yes/No",
      "Is a hashed message supposed to be un-hashed? - Yes/No",
      "What is the SHA256 hashing value of your NYU email and use the answer in your code - ",
      "Is MD5 a secured hashing algorithm? - Yes/No",
      "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number",
      "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number"
    ]
    
    for question in questions:
      print(welcome_assignment_answers(question))
    '''

#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#"Are encoding and encryption the same? - Yes/No":
#"Is it possible to decrypt a message without a key? - Yes/No":
#"Is it possible to decode a message without a key? - Yes/No":
#"Is a hashed message supposed to be un-hashed? - Yes/No":
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#"Is MD5 a secured hashing algorithm? - Yes/No":
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
