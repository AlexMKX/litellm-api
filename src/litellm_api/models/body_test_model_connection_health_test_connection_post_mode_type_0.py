from enum import Enum

class BodyTestModelConnectionHealthTestConnectionPostModeType0(str, Enum):
    AUDIO_SPEECH = "audio_speech"
    AUDIO_TRANSCRIPTION = "audio_transcription"
    BATCH = "batch"
    CHAT = "chat"
    COMPLETION = "completion"
    EMBEDDING = "embedding"
    IMAGE_GENERATION = "image_generation"
    OCR = "ocr"
    REALTIME = "realtime"
    RERANK = "rerank"
    RESPONSES = "responses"
    VIDEO_GENERATION = "video_generation"

    def __str__(self) -> str:
        return str(self.value)
