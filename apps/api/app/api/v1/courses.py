"""Course catalog endpoints used by the company website."""

from fastapi import APIRouter


router = APIRouter(prefix="/courses", tags=["courses"])


@router.get("")
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
                "badge": "Bestseller",
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
                "badge": "Hot",
            },
        ],
    }
