import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "6779bbd0-a980-11e9-a84b-951c0154684a2e910ad8-c55d-452a-8146-c89931184ca2"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
def answer_question():
    question = input(">")
    answer = classify(question)
    answerclass = answer["class_name"]
    confidence = answer["confidence"]
    
    if confidence < 75:
        print("I'm not quite sure, Please ask another question:")
        
    elif answerclass == "Length":
        print("The average length of a soccer game is 90 minutes.")
    elif answerclass == "Place":
        print("A good place to play soccer is on a dry soccer field.")
    elif answerclass == "size":
        print("The average soccer field is 100m by 80m.")
    elif answerclass == "Popularity":
        print("Soccer is the most popular sport in the world with 250 million people playing currently.")
    
print("Ask me a question about the time, size, popularity, and place about soccer!")
while True:
    answer_question()