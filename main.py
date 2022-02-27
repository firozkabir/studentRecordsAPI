from fastapi import FastAPI
from deta import Deta
import os

project_key = os.getenv("DETA_PROJECT_KEY")
deta = Deta(project_key)
reg_db = deta.Base("registrations-db")
courses_db = deta.Base("courses-db")
app = FastAPI()


@app.get("/studentRegistration/key/{key}")
async def get_reg_by_key(key: str):
    reg_records = reg_db.get(key)
    return reg_records if reg_records else {"error": "no record found"}


@app.get("/studentRegistration/sisid/{sisid}/academicyear/{academicyear}")
async def get_reg_by_sisid_academicyear(sisid: int, academicyear: int):
    reg_records = reg_db.fetch({"sisid": sisid, "academicyear": academicyear})
    return reg_records._items


@app.get("/studentRegistration/sisid/{sisid}")
async def get_reg_by_sisid(sisid: int):
    reg_records = reg_db.fetch({"sisid": sisid})
    return reg_records._items


@app.get("/studentCourses/key/{key}")
async def get_courses_by_key(key: str):
    courses_records = courses_db.get(key)
    return courses_records if courses_records else {"error": "no record found"}


@app.get("/studentCourses/sisid/{sisid}/academicyear/{academicyear}")
async def get_courses_by_sisid_academicyear(sisid: int, academicyear: int):
    courses_records = courses_db.fetch({"sisid": sisid, "academicyear": academicyear})
    return courses_records._items


@app.get("/studentCourses/sisid/{sisid}")
async def get_courses_by_sisid(sisid: int):
    courses_records = courses_db.fetch({"sisid": sisid})
    return courses_records._items