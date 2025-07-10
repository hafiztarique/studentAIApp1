import requests
import os

CANVAS_BASE_URL = "https://canvas.gmu.edu/api/v1"
CANVAS_API_KEY = os.getenv("CANVAS_API_KEY")

# Dummy implementation – replace with actual API calls
def get_canvas_courses(student_id):
    return [
        {"name": "IT 341 - Data Communications", "term": "Fall 2025"},
        {"name": "IT 499 - Capstone Project", "term": "Fall 2025"},
    ]