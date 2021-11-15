# lecturer.py
from pydantic import BaseModel
# Make the Lecturer Class inherit from BaseModel
class Lecturer(BaseModel):
    name: str # e.g.: Nathan Segers
    language: str # e.g.: Dutch
    track: str # e.g.: Next Web Developer
    programmingLanguage: str # e.g.: Python
    favouriteCourse: str # MLOps
        
    def sayHello(self):
        print(f"Hello, my name is {self.name} and I love {self.favouriteCourse}")