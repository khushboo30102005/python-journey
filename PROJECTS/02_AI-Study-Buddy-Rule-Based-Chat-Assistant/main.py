import time
import datetime
name = input("Welcome, What is your name: ")
presentHour = datetime.datetime.now().hour

if 5 <=presentHour <=11:
  print("Good Morning, ", name)
elif 11 <= presentHour <=17:
  print("Good AfterNoon, ", name)  
elif 17 <= presentHour <= 20:
  print("Good Evening, ", name)  
else:
  print("Good Night, ", name)  

print("NAMASTY!!, Welcome to your Study Buddy ChatBot..")
print("Ask Me Basic Question, Type 'Bye To Exit.")

responses = {
    "hello": "Hello! I'm your Study Buddy 😊",
    "hi": "Hi! How can I help you today?",
    "hey": "Hey! Ready to study?",
    
    "bye": "Goodbye! Keep learning 📚",
    "good night": "Good night! Take rest 😴",
    "sad": "Don’t worry! Even code breaks sometimes, but it always runs again 😊",
    "thanks": "You're welcome 😊",
    "happy": "That’s great to hear! Keep that positive energy going 🎉",
    "tip": "Study Tip: Use Pomodoro — 25 min study + 5 min break 🍅",
    
    "motivation": "You are doing great! Keep going 🚀",
    
    "dbms": "DBMS includes SQL, Transactions, Normalization, ER Models, etc.",
    "dsa": "DSA improves your logic and problem-solving skills.",
    "python": "Python is simple and powerful. Ask me any concept!",
    "react": "React helps you build UI using components.",
    
    "exam": "Tell me your subject, I will give important exam questions.",
    
    "reminder": "Reminder: Take a short break and drink water 💧",
    
    "goal": "Set one small goal today and achieve it! 🎯",
    
    "fact": "Fun Fact: Writing notes improves memory ✍️",
    
    "default": "Sorry, I didn't understand that. Try again 🙂"
}

def getResponse(userQuestion):
  userQuestion = userQuestion.lower()
  for eachKey in responses:
    if eachKey in userQuestion:
      return responses[eachKey]
  return "I am not able to tell that. I'm still in learning mode. "  
    
while(1): 
  userInput  = input("Please Ask Your Question: ")
  reply = getResponse(userInput)
  time.sleep(1)
  print(reply)
  if "bye" in userInput.lower():
    break
