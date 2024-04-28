from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.auth.routes import health_check, user_auth
from src.virtu_chef.routes import virtu_chef
from src.virtu_hunter.routes import virtu_hunter

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
# app.include_router(user_auth.router)
app.include_router(virtu_chef.router)
app.include_router(virtu_hunter.router)
