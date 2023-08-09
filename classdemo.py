class Comment:
    def __init__(self,username,text,likes,dislikes):
        self.username=username
        self.text=text
        self.likes=likes
        self.dislikes=dislikes

c1=Comment("JohnnyWalker","Good Course")      
c2=Comment("John Smith","Very Good Course")
c3=Comment("Emmet Brown","Course is not bad",50,10)
c4=Comment("Jessica Lovrence","I didn't like the course")
c5=Comment("Jane Larkin","The course is fantastic",100)

comments=[c1,c2,c3,c4,c5]

for c in [comments]:
    print(f"{c.username}: {c.text}")
    print(f"likes: {c.likes}-dislikes:{c.dislike}")

        
