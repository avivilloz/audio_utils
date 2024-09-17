# Audio Utils

This is a Python package that provides a collection of utility functions for audio processing and manipulation. It offers simple and efficient tools for common audio-related tasks, with plans for expansion to cover a wide range of audio operations.

## Description:

This is a comprehensive Python package designed to simplify audio file handling and processing tasks for developers, audio engineers, and multimedia professionals. While currently offering basic functionality, the package is built with extensibility in mind and is set to evolve into a robust suite of audio manipulation tools.

Key features and potential future expansions include:
- Audio Duration Calculation: Accurately determine the length of audio files in seconds.
- Format Conversion: (Planned) Convert audio files between various formats (e.g., MP3, WAV, FLAC, AAC).
- Audio Editing: (Planned) Trim, split, merge, and manipulate audio segments.
- Metadata Handling: (Planned) Read, write, and modify audio file metadata.
- Audio Analysis: (Planned) Analyze audio properties such as bit rate, sample rate, and channels.
- Volume Adjustment: (Planned) Normalize audio levels and apply volume changes.
- Effects Processing: (Planned) Apply various audio effects like fade in/out, pitch shifting, and equalization.
- Silence Detection: (Planned) Identify and process silent segments in audio files.
- Transcoding: (Planned) Change audio codecs while preserving quality.
- Batch Processing: (Planned) Perform operations on multiple audio files simultaneously.

The package aims to provide an intuitive API that allows users to perform complex audio operations with minimal code. It leverages popular audio processing libraries to ensure high-quality results and broad format support.

Whether you're building a music application, processing podcast episodes, or integrating audio functionality into a larger system, audio_utils is designed to be a valuable addition to your toolkit. Its modular structure allows for easy integration into existing projects and workflows.

## How to install:

Run the following command in your python venv:

```bash
pip install git+https://github.com/avivilloz/audio_utils.git@main#egg=audio_utils
```

Or add the following line to your project's `requirement.txt` file:

```
git+https://github.com/avivilloz/audio_utils.git@main#egg=audio_utils
```

And run the following command:

```bash
pip install -r requirements.txt
```

## How to use:

```python
from audio_utils import *

# Use audio utils functions
```