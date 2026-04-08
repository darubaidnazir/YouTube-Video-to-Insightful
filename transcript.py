from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    return url.split("v=")[-1].split("&")[0]

def fetch_transcript(url):
    try:
        video_id = get_video_id(url)

        api = YouTubeTranscriptApi()
        data = api.fetch(video_id)

        return " ".join([t.text for t in data])

    except Exception as e:
        print("❌ Transcript Error:", e)
        return ""