from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import health_check, user_auth, virtu_chef

app = FastAPI()

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add routes
app.include_router(health_check.router)
app.include_router(user_auth.router)

# Add virtu chef routes
app.include_router(virtu_chef.router)
