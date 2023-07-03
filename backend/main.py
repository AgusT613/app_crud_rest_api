# Frameworks
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Routers
import users

# Main app and user router
app = FastAPI()
app.include_router(users.router)

# Allowed HTML (on localhost) to make requests
index_html = 'http://localhost:5173'
# CORS Authentication
app.add_middleware(
    CORSMiddleware,
    allow_origins = index_html,
    allow_methods = ['GET', 'POST']
)

# Root
@app.get('/')
def root():
    return {'message': 'Hello Fast API!'}