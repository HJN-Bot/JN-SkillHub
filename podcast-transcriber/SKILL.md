---
name: podcast-transcriber
description: >
  Download and transcribe podcast episodes from RSS feeds for Jianan's curated analysis pipeline.
  Use when Jianan asks to "transcribe this episode", "process podcast", "pull podcast transcript",
  or when Gbrain curation identifies a high-match episode for processing.
  Input: RSS feed URL or specific episode URL. Output: structured transcript + metadata + quotes.
---

# Podcast Transcriber

Standard RSS → mp3 → Whisper transcription pipeline for Jianan's 4 curated podcast sources.

## Curated Sources

| Source | RSS Feed | Priority |
|--------|---------|----------|
| Google DeepMind | `https://feeds.simplecast.com/JT6pbPkg` | P0 |
| Dwarkesh Podcast | `https://apple.dwarkesh-podcast.workers.dev/feed.rss` | P0 |
| Lenny's Podcast | `https://api.substack.com/feed/podcast/10845.rss` | P1 |
| School of Hard Knocks | `https://feed.ausha.co/rj98WHq4P9rm` | P1 |

## Pipeline

```
RSS Feed → Parse XML → Find matching episode
  → Download mp3 (curl, partial OK for whisper)
    → Transcribe (faster-whisper tiny, 150x+ real-time)
      → Output: transcript.md + metadata.json + quotes.json
```

## Usage

### Process a specific episode
```
"Transcribe the latest Google DeepMind episode"
"Download and transcribe Lenny's Podcast episode about agency"
```

### Process from curation filter
When Gbrain curation identifies a match:
1. Feed the episode URL to this skill
2. Download → transcribe → write output
3. Return output path to Gbrain for analysis

## Output Structure

```
books/celebrity-interviews/transcripts/
├── YYYY-MM-DD_show-name_episode-name_transcript.md
├── YYYY-MM-DD_show-name_episode-name_metadata.json
└── YYYY-MM-DD_show-name_episode-name_quotes.json
```

### metadata.json
```json
{
  "show": "Lenny's Podcast",
  "episode": "Why cultivating agency matters...",
  "guest": "Max Schoening",
  "date": "2026-05-03",
  "duration_seconds": 5400,
  "language": "en",
  "rss_feed": "https://api.substack.com/feed/podcast/10845.rss",
  "transcription_model": "faster-whisper tiny",
  "transcription_speed": "158x",
  "matched_dimensions": ["AI product", "agency", "PM methodology"]
}
```

### quotes.json
```json
[
  {
    "text": "The first 10% of every project are now free",
    "timestamp": 31.0,
    "tags": ["AI", "productivity", "cost"],
    "use_case": "presentation_beat3_insight"
  }
]
```

## Technical Notes

- **Whisper model**: `faster-whisper` with `tiny` model on CPU (int8)
- **Performance**: ~158x real-time on Mac mini M-series
- **Memory**: ~500MB for model loading + audio processing
- **Partial downloads**: Whisper works on truncated mp3 files (no cleanup needed)
- **Audio format**: Many podcast hosts use 302 redirects to CDN — follow redirects
- **Rate limiting**: Respect RSS feed TTL, don't hammer sources

## Curation Integration

Before transcribing, episode must pass the curation filter (see INFO_PIPELINE_DESIGN.md):

```
L1 — Keyword pass: episode title/description contains relevant terms
L2 — Profile match: ≥2 dimensions matched (active projects, interests, knowledge gaps)
```

Only transcribe episodes that pass L1+L2. Store rejected episodes in `curation_skip_log.json` for periodic review.

## Dependencies

```bash
pip install faster-whisper  # already installed
# curl + ffmpeg (already available via brew)
```

## Failure Modes

1. **RSS feed 404/blocked** → Flag in SAM_DAILY_BRIEF.md, skip to next source
2. **Download timeout** → Retry once with longer timeout, skip if still fails
3. **Whisper OOM** → Use smaller audio sample (first 10MB), flag for full download on better hardware
4. **Empty transcript** → Check if episode has actual speech (not music-only intro)
