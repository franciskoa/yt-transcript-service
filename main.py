from fastapi import FastAPI
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/transcript")
def get_transcript(video_id: str):
    try:
        ytt = YouTubeTranscriptApi()
        transcript = ytt.fetch(video_id)
        full_text = " ".join([t.text for t in transcript])
        return {"success": True, "transcript": full_text}
    except Exception as e:
        return {"success": False, "error": str(e)}
