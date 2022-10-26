# Download YouTube auto subtitles.

Download the subtitles of the latest 50 videos published of the channel.

Uses Youtube API to get the videos ID and [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api) to get the transcripts.

## Requirements

- You need to have a Google API key. You can get one [here](https://console.developers.google.com/apis/credentials) for free.

- Save the API key in a file named `api_key.txt` in the same directory as the script.

## Installation

```
git clone git@github.com:JonasBrother97/youtube_subtitles.git
```

```
cd youtube_subtitles
```

```
pip install -r requirements.txt
```

## Usage

```
python main.py 
```

## Language options

- English: en
- German: de
- French: fr
- Spanish: es
- Italian: it
- Portuguese: pt
- etc

Paste the URL of the desired channel and the language of the subtitles you want to download. **No quotation marks**.
