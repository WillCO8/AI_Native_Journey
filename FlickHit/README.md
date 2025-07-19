# 🎶 FlickHit: Cultural Playback App  
**“Match the date of your Flick to its #1 Hit”**

---

### 💡 Problem Statement  
In the age of digital overload, our photos often become lifeless thumbnails—stripped of the sound, feeling, and cultural atmosphere that surrounded them.  
People flip through old pictures, but rarely do they reconnect emotionally with the full context of the moment.  
There’s no soundtrack. No era. Just pixels.

---

### 💡 Solution  
FlickHit is a web app that brings still images back to life.  
Users upload a photo, and FlickHit reads the original date from its metadata.  
Then, it instantly links you to the **#1 Billboard Hot 100 song from that specific week**, reconnecting you to the music and mood of that time.

> It’s like time-travel through memory.  
> You don’t just look at a picture—you **hear** it.

---

### 🔊 What is “FlickHit”?  
It’s not just an app—it’s a verb or a powerful statement.

When you see a picture and want to unlock its musical memory, you simply say:  
**FlickHit** (pronounced like "flick it" or "flick hit").  

It’s both the action of revealing the #1 song from that moment, and the immediate, memorable declaration of wanting to experience that connection.

> “We saw that picture of us at our wedding and immediately, we just said: 'FlickHit!'”  
> “We were scrolling through pics and saw my graduation pictures and said 'FlickHit'.”  
> “That moment when you find a forgotten memory and all you can think is, 'FlickHit!'”

FlickHit turns scrolling into **storytelling**.

---

### 🔧 How It Works (MVP)

| Feature | Description |
|--------|-------------|
| 📸 **Photo Upload** | Users upload `.jpg` or `.png` photos |
| 🕒 **Date Detection** | The app reads the `DateTimeOriginal` from EXIF metadata |
| 🎵 **Chart Lookup** | Matches the photo's date to the Billboard Hot 100 #1 song |
| 🔗 **Billboard Link** | Provides a direct link to the Billboard chart for that week |
| ✅ **No Photo Storage** | Files are processed in-browser only — no persistent storage |

---

### 💘 Value Proposition  
FlickHit is **emotion-first software**.  
It creates a deeply personal cultural experience—blending your own visual history with the sounds of that time.  
This kind of sensory reconnection makes memories feel present, not past.

> It’s effortless nostalgia with just one upload.

---

### 🧪 Assumption to Test  
> *"Users find significant emotional or nostalgic value in connecting their personal photos to the #1 song from that specific week."*

---

### 🧑‍🔬 How We'll Test This

- 👥 User trials with friends and family  
- 🎤 Ask:  
  - “How did it feel to hear that song?”  
  - “Did it change how you saw the photo?”  
  - “Would you FlickHit more photos?”  
- 🤔 Compare emotional reactions with vs. without music

---

### 📊 Data & Privacy  
- **No files saved. Ever.**  
- EXIF data read **locally** in-browser  

---

### 🧱 MVP Scope

✅ **In Scope**
- Upload & EXIF date extraction  
- Linking to Billboard #1 chart page based on date  
- Static hosting on GitHub Pages  
- Clean, intuitive UI  

❌ **Out of Scope (for now)**
- Accounts or saved lookups  
- Multiple media types (movies, books, etc.)  
- Direct streaming service integrations (YouTube/Spotify embeds)  
- API scraping of Billboard, YouTube, etc.

---

### 🚀 Future Enhancements
- Support for direct streaming service links (e.g., YouTube, Apple Music)  
- Let users create and save “FlickHit Memories” (requires data persistence)  
- Pull in top movies, shows, and news headlines from that date  
- Mobile-first app experience  
- Public-facing “FlickHit Stories” gallery  

---

> **Developed with ❤️ to bring the sound back to your snapshots.**
