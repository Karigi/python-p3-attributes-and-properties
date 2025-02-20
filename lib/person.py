#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, job = "Unemployed"):
        self.job = job
    
    def get_job(self):
        return self._job
    
    def set_job(self, job):
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            self._job = "Unemployed"
        else:
            self._job = job

    job = property(get_job, set_job)

person = Person()
person.job = "Admin"
print(person.job)
person.job = "Pilot"
print(person.job)
person.job = ""
print(person.job)
