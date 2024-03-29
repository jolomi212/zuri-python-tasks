class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name: str, age: int, tracks: list, score: float):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
    def change_name(self, new_name):
        self.name = new_name

    def change_age(self, new_age):
        if type(new_age)== int:
            self.age = new_age
        else:
            print("Age value, not an integer")
    
    def add_track(self, new_track):
        
        self.tracks.append(new_track)
        

    def get_score(self):
        return self.score
       
        
        
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()




