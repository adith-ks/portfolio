from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.

class Portfolio(View):
    def get (self,request):
        data = {
            "ID":"1",
            "Full_name":"ADITH k S",
            "Professional title":"FULL_STACK_DEVELOPER",
            "Bio":"PROFESSIONAL",
            "DOB":"11-05-2005",
            "Email":"adithks112233@gmail.com",
            "Contact":"8089039381",
            "Location":"Kadavanthra",
            "Github url":"",
            "Linkedin url":"",
        }
        return JsonResponse(data)

class Education(View):
    def get(self,request):
        data = {
            "ID":"1",
            "Institution":"Luminar Technolab",
            "Course":"Full_Stack",
            "University":"MGM",
            "Location":"Piravom",
            "Start_year":"2024",
            "End_year":"2026",
            "Grade":"s+",
            "Description":"Course Completed"
        }
        return JsonResponse(data)


class ProjectView(View):
    def get(self, request):
        data = [
            {
                "id":1,
                "title":"First_Aid",
                "short_description":"AI-based first aid recomendation",
                "technologies_used":["Python","Django","Google GenAI SDK"],
                "live_url":"https://first_aid.example.com",
                "github_url":"https://github.com/yourusername/first_aid",
                "image_url":"https://api.yourdomain.com/media/projects/first_aid",
                "featured":True
            },
            {
                "id":2,
                "title":"FoodBox",
                "short_description":"AI-based food odering application",
                "technologies_used":["Python","Django","Google GenAI SDK"],
                "live_url":"https://foodbox.example.com",
                "github_url":"https://github.com/yourusername/foodbox",
                "image_url":"https://api.yourdomain.com/media/projects/foodbox",
                "featured":True
            },
            {
                "id":3,
                "title":"Interview prep blog",
                "short_description":"Educational application for programming intrviews.",
                "technologies_used":["Python","Django","Google GenAI SDK"],
                "live_url":"https://interview_prep.example.com",
                "github_url":"https://github.com/yourusername/interview_prep",
                "image_url":"https://api.yourdomain.com/media/projects/interview_prep",
                "featured":True
            }
        ]
        return JsonResponse(data,safe=False)

class SkillsView(View):
    def get(self,request):
        data =[
            {
                "id":1,
                "Skill_name":"Python ",
                "Category":"Programming language",
                "Proficinecy level":"Average",
                "Years of experience":4
            },

            {
                "id":2,
                "Skill_name":"Django",
                "Category":"BAckend",
                "Proficinecy level":"Average",
                "Years of experience":3
            },

            {
                "id":3,
                "Skill_name":"React",
                "Category":"Frontend",
                "Proficinecy level":"Average",
                "Years of experience":2
            }

        ]
        return JsonResponse(data,safe=False)

class ExperienceView(View):
    def get(self,request):
        data=[
            {
                "Id":1,
                "Job_title":"Python intern",
                "Company_name":"Infosys",
                "Location":"Kakkanad",
                "Employement type":"Intern",
                "Start date":"25-09-26",
                "End date":"25-10-26",
                "Currently working":"Yes",
                "Description":"Internship completed"
            },
            {
                "Id":2,
                "Job_title":"Django intern",
                "Company_name":"IBM",
                "Location":"Kakkanad",
                "Employement type":"Intern",
                "Start date":"25-09-26",
                "End date":"25-11-26",
                "Currently working":"Yes",
                "Description":"Internship completed"
            },

            {
                "Id":3,
                "Job_title":"Full_Stack_Developer",
                "Company_name":"Luminar",
                "Location":"Kakkanad",
                "Employement type":"Coding",
                "Start date":"25-09-26",
                "End date":"25-09-30",
                "Currently working":"Yes",
                "Description":"Internship completed",
            },

        ]
        return JsonResponse(data,safe=False)

class Certificate(View):
    def get(self,request):
        data=[
            {
                "Id":1,
                "Certificate_name":"Full_Stack_Devloper",
                "Issuing_organization":"Luminar Technolab",
                "Issued_date":"10-01-2027"
            },
            {
                "Id":2,
                "Certificate_name":"Pytohn_Django",
                "Issuing_organization":"HACA",
                "Issued_date":"10-04-2026",
            },
        ]
        return JsonResponse (data,safe=False)

class Services(View):
    def get(self,request):
        data =[
            {
                "Id":1,
                "Servcie_name":"Web Developement",
                "Description":"Can make websited as per user request",
                "Technologies_used":"Python Django,Reachjs,Vs code,Html,Css",
            },
            {
                "Id":2,
                "Servcie_name":"Database MAnagement",
                "Description":"Can store,update delete data",
                "Technologies_used":"Mysql,Sqlite",
            },
            

        ]
        return JsonResponse(data,safe=False)