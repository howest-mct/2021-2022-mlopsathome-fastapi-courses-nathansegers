# course.py
from typing import List
from pydantic import BaseModel
# Make the Course Class inherit from the base-class `object`
class Course(BaseModel):
    title: str # e.g.: MLOps
    description: str # e.g.: A course where you will learn how to deploy AI models
    track: str # e.g.: AI Engineer
    semester: str # e.g.: 5 --> Year 3, semester 1
    lecturers: List[str] # e.g.: ['Nathan Segers', 'Wouter Gevaert']

        
    def showLecturers(self):
        print(f"The Lecturers for the {self.name} course are {self.lecturers}")