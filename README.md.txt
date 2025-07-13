Flickhit: Cultural Playback App - Project Plan
Problem Statement (using the McKinsey framework)
Many individuals struggle to emotionally reconnect with their past digital photos, often viewing them as static images devoid of the rich, multi-sensory context of the moment they were captured. This leads to a missed opportunity for deeper personal engagement with their digital memories and a lack of readily accessible cultural context for their personal history.
Solution (your idea)
Flickhit is a unique web application that allows users to upload personal photos, automatically extracts the date metadata, and then instantly provides a link to the #1 song on the Billboard Hot 100 from that exact week, enabling users to "hear the past" and rediscover their memories with their forgotten soundtracks.
How you plan to use/collect data
	1	Collection:
	◦	User-Uploaded Photo Files: Users will directly upload .jpg or .png image files.
	◦	No Persistent Storage: Crucially, these photo files will not be stored persistently on any server or database. They will be processed in temporary memory for date extraction and then discarded.
	2	Usage:
	◦	EXIF Metadata Extraction: The app will use a Python library (Pillow) to read the DateTimeOriginal (or similar) EXIF tag from the uploaded image to get the exact date the photo was taken.
	◦	Historical Music Chart Lookup: The extracted date will be used to query a historical music chart API/library (billboard.py) to find the #1 song on the Billboard Hot 100 for that specific week.
	◦	Streaming Link Generation: The identified song title and artist will be used to construct a search query URL for a popular streaming service (e.g., Spotify Web Player, YouTube Music) to provide a clickable "listen" link.
Value Proposition
Flickhit offers a novel and emotionally resonant way for users to re-experience their personal memories by instantly connecting their photos to the popular music soundtrack of that exact moment in time. It transforms static images into a dynamic, nostalgic journey, providing a unique cultural context to their personal history with minimal effort.
What's in MVP scope
	•	Photo Upload: Ability to upload .jpg or .png files.
	•	Date Extraction: Successfully read the DateTimeOriginal (or similar) EXIF tag from the uploaded photo.
	•	Billboard #1 Song Lookup: Accurately retrieve the #1 song on the Billboard Hot 100 for the extracted date's week.
	•	Streaming Link: Generate a clickable search link to a single, pre-defined streaming service (e.g., YouTube Music) for the identified song.
	•	Basic UI: A clean, simple Streamlit interface for upload, display of song info, and the listen link.
	•	No Persistent Storage: Ensure no user photos or personal data are stored after processing.
What's out of MVP scope
	•	User accounts or profiles.
	•	Saving or sharing generated "Flickhits."
	•	Support for multiple streaming service choices (e.g., Spotify, Apple Music, etc. selection).
	•	Retrieving top movies, TV shows, albums, books, or news events.
	•	Advanced error handling for malformed EXIF data or missing chart data.
	•	Complex UI animations or design elements beyond Streamlit's defaults.
	•	Machine learning for personalized song recommendations beyond #1 hits.
The assumption you want to test with your MVP
The core assumption I want to test is: "Users find significant emotional or nostalgic value in instantly connecting their personal photos to the #1 hit song from that specific week."
How you plan to test the assumption
I plan to test this assumption through qualitative feedback and direct observation during initial user trials:
	1	Direct User Feedback: After building the MVP, I will share it with a small group of target users (friends, family, early adopters). I will ask them to upload their own photos and then specifically ask questions like:
	◦	"How did you feel when you saw the song for your photo?"
	◦	"Did it bring back memories or evoke a particular feeling?"
	◦	"Is this a feature you would use regularly?"
	◦	"Does the song choice feel relevant to the photo's date?"
	2	Observation: I will observe their reactions as they use the tool for the first time, noting any expressions of surprise, delight, or engagement.
	3	Informal A/B Testing (Mental): I'll compare their reactions to this specific feature versus general photo viewing, looking for signs that the music connection truly enhances the experience.
The goal is to gauge the emotional impact and perceived value, not just technical functionality.
