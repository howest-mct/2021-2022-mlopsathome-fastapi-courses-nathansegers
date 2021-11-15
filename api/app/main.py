from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

from schemas.course import Course
from schemas.lecturer import Lecturer

with open('data/courses.json', 'r') as f:
  courses = json.load(f)
courses = list(map(lambda course: Course(**course), courses))
with open('data/lecturers.json', 'r') as f:
  lecturers = json.load(f)
lecturers = list(map(lambda lecturer: Lecturer(**lecturer), lecturers))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message":"Hello World"}

# Course routes
@app.get('/mct/courses',
    summary='Get all courses',
    tags=['Course'],
    response_model=List[Course])
async def getAllCourses():
    return courses

@app.get('/mct/courses/track/{track}', description='Return all the courses by a Track',
    summary='Return all the courses by a Track',
    tags=['Course'],
    response_model=List[Course])
async def getAllCoursesByTrack(track: str):
    return list(filter(lambda course: course.track == track, courses))

@app.get('/mct/courses/name/{name}', description='Return one course by name',
    summary='Return one course by name',
    tags=['Course'],
    response_model=Course)
async def getCourseByName(name: str):
    returnCourses = list(filter(lambda course: course.title == name, courses))
    if len(returnCourses) == 0:
        raise HTTPException(404, 'No course with that name')
    elif len(returnCourses) > 1:
        raise HTTPException(400, 'Too many courses with that name')
    return returnCourses[0]
    
# Lecturer routes
@app.get('/mct/lecturers', description='Return all the lecturers of MCT', 
    summary='Get all lecturers',
    tags=['Lecturer'],
    response_model=List[Lecturer])
async def getAllLecturers():
    return lecturers

@app.get('/mct/lecturers/track/{track}', description='Return all the lecturers by a Track',
    summary='Return all the lecturers by a Track',
    tags=['Lecturer'],
    response_model=List[Lecturer])
async def getAllLecturersByTrack(track: str):
    return list(filter(lambda lecturer: lecturer['track'] == track, lecturers))

@app.get('/mct/lecturers/name/{name}', description='Return one lecturer by name',
    summary='Return one lecturer by name',
    tags=['Lecturer'],
    response_model=List[Lecturer])
async def getLecturerByName(name: str):
    return list(filter(lambda lecturer: lecturer['name'] == name, lecturers))