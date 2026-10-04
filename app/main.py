from fastapi import FastAPI

app = FastAPI(
    title="Graphify API",
    description="Graph database application POC",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "application": "Graphify",
        "status": "running",
        "version": "0.1.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }