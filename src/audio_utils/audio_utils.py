from pydub import AudioSegment

__all__ = ["get_audio_duration_in_seconds"]


def get_audio_duration_in_seconds(audio_path: str):
    return len(AudioSegment.from_file(audio_path)) / 1000.0
