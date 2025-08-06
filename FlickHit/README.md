# 🎶 FlickHit: Cultural Playback App  
**“Match the date of your Flick to its #1 Hit.”**  
A nostalgic web app that connects your photos to the #1 Billboard song from the week they were taken.  
**Flick = Picture. Hit = Hit Song.**

🔗 **Live App:** [https://willco8.github.io/flickhit/](https://willco8.github.io/flickhit/)

---

### 💡 Problem Statement  
In the age of digital overload, our photos often become lifeless thumbnails—stripped of the sound, feeling, and cultural atmosphere that surrounded them.  
People scroll through pictures, but rarely reconnect with the full emotional context of the moment.  
There’s no soundtrack. No era. Just pixels.

---

### 💡 Solution  
FlickHit is a web app that brings still images back to life.  
Upload a photo, and FlickHit reads the original date from its metadata.  
Then, it instantly links you to the **#1 Billboard Hot 100 song from that specific week**, reconnecting you to the music and mood of that time.

> It’s like time-travel through memory.  
> You don’t just look at a picture—you **hear** it.

---

### 🔊 What is “FlickHit”?  
It’s not just an app—it’s a verb, a ritual, a powerful emotional shortcut.

When you see a picture and want to unlock its musical memory, you simply say:  
**FlickHit** (pronounced like "flick it" or "flick hit").

It’s both the action of revealing the #1 song from that moment, and the joyful declaration of reliving it.

> “We saw that picture of us at our wedding and immediately, we just said: 'FlickHit!'”  
> “We were scrolling through pics and saw my graduation photo and said 'FlickHit'.”  
> “That moment when you find a forgotten memory and all you can think is, 'FlickHit!'”

FlickHit turns scrolling into **storytelling**.

---

### 🔧 How It Works (MVP)

| Feature               | Description |
|-----------------------|-------------|
| 📸 **Photo Upload**      | Upload `.jpg` or `.png` images |
| 🕒 **Date Detection**     | Reads the `DateTimeOriginal` field from EXIF metadata |
| 🎵 **Chart Lookup**       | Finds the Billboard Hot 100 #1 song from the photo's date |
| 🔗 **Billboard Link**     | Links to the official Billboard chart for that week |
| ✅ **No File Storage**    | Everything is processed client-side in your browser |

---

### 💘 Value Proposition  
FlickHit is **emotion-first software**.  
It blends your visual history with the cultural soundtrack of your life.  
One upload and you're back in that moment—with music to match.

> It’s effortless nostalgia at your fingertips.

---

### 🧪 Assumption to Test  
> *"Users find significant emotional or nostalgic value in connecting their personal photos to the #1 song from that specific week."*

---

### 🧑‍🔬 How We'll Test This

- 👥 Early user feedback from friends, family, and testers  
- 🎤 Questions to prompt reflection:  
  - “How did it feel to hear that song?”  
  - “Did it change how you saw the photo?”  
  - “Would you FlickHit more photos?”  
- 🤔 Compare emotional reactions *with* vs. *without* the music link

---

### 📊 Data & Privacy  
- **No photos or EXIF data is stored**  
- All metadata processing happens **locally** in your browser  
- No uploads are sent to a server

---

### 🧱 MVP Scope

✅ **In Scope**
- EXIF date extraction from uploaded photos  
- Matching to historical #1 Billboard song via local JSON  
- Clean UI and responsive layout  
- Static hosting via GitHub Pages

❌ **Out of Scope (for now)**
- User accounts or photo saving  
- Other media types (movies, books, etc.)  
- Streaming service embeds (Spotify, YouTube, etc.)  
- API scraping of real-time data

---

### 🚀 Future Enhancements
- Direct links to YouTube and Apple Music songs  
- “FlickHit Memories” – save your photo-song pairings  
- Add context: top movies, shows, news headlines from the same week  
- Mobile-first UX design  
- “FlickHit Stories” – share your own time-stamped memories publicly

---

> **Developed with ❤️ to bring the sound back to your snapshots.**