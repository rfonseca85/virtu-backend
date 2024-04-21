
Backend run command

```bash
cd backend
echo "OPENAI_API_KEY=sk-your-key" > .env
echo "SECRET_KEY=your_key"
echo "ALGORITHM=HS256"
echo "ACCESS_TOKEN_EXPIRE_MINUTES=60"
echo "MONGO_URI=your_mongo_db_connection_string"
echo "ENVIRONMENT=prod" 

poetry install
poetry shell
poetry run uvicorn main:app --reload --port 8080
```