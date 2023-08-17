class Question:
    def __init__(self,text,choices,answer):
        self.text=text
        self.choices=choices
        self.answer=answer

    def checkAnswer(self,answer):
        if answer not in self.choices:
            raise ValueError("Wrong Information")
        return self.answer==answer

q1=Question("Best Language Program is",["Python","C#","Java","Dart"],"Python")            

print(q1.text)
print(q1.choices)
print(q1.answer)

result=q1.checkAnswer('Java')
print(result)
