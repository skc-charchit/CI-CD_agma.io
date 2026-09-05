from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="AGMA.io API",
    description="Backend API for AGMA.io EdTech Platform",
    version="1.0.0"
)

# Set up Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# ---------------------------------------------------------
# 1. FRONTEND ROUTE: Serves the main HTML page
# ---------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ---------------------------------------------------------
# 2. API ROUTE: Sample endpoint to fetch course data
# (You can connect your frontend JS to this endpoint later)
# ---------------------------------------------------------
@app.get("/api/courses")
async def get_courses():
    return {
        "status": "success",
        "data": [
            {
                "id": 1,
                "title": "Complete Web Development Bootcamp 2026",
                "instructor": "Dr. Angela Yu",
                "rating": 4.8,
                "reviews": 15420,
                "price": 499,
                "originalPrice": 3999,
                "discount": "88% off",
                "image": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=500&auto=format&fit=crop&q=60",
                "badge": "Bestseller"
            },
            {
                "id": 2,
                "title": "Python for Data Science and Machine Learning",
                "instructor": "Jose Portilla",
                "rating": 4.7,
                "reviews": 8900,
                "price": 549,
                "originalPrice": 4499,
                "discount": "87% off",
                "image": "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=500&auto=format&fit=crop&q=60",
                "badge": "Hot"
            }
        ]
    }

# ---------------------------------------------------------
# 3. RUN SERVER
# ---------------------------------------------------------
if __name__ == "__main__":
    # reload=True enables hot-reloading during development
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)