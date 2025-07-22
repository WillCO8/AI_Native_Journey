# 📌 Apple Notes Pin/Unpin Redesign Project

This document outlines the planning process for a UX/UI redesign project focusing on the **"Quick Pin/Unpin Note"** feature within the Apple Notes application.

---

## 🧠 Step 1: Project Framework

### 🔧 Feature to Redesign  
**Apple Notes** – Quick Pin/Unpin a note from within an open note.

---

## 🧐 Problem Statement (McKinsey Framework)

- **Situation**  
  Apple Notes users frequently work within individual notes and often need to quickly prioritize or de-prioritize them.

- **Complication**  
  The current process for pinning or unpinning a note requires tapping a "More" menu (three dots), then selecting "Pin Note" or "Unpin Note". This menu-driven interaction adds friction and cognitive load, interrupting the user's flow. Additionally, the feature is hidden, reducing its discoverability and utility.

- **Question**  
  How might we redesign the in-note pinning/unpinning interaction to be a **single-tap, intuitive action**, improving user efficiency and focus?

---

## 💡 Proposed Solution

- Introduce a **prominent Pin/Unpin button** directly within the header/toolbar of an open note.  
- Provide **visual feedback** via icon state changes and brief toast messages — no need for additional navigation or menus.

---

## 🎯 Value Proposition

For Apple Notes users, this redesign provides a **fast, intuitive way to pin or unpin notes** directly within an open note.  
It improves organization, streamlines workflow, and increases discoverability of a valuable feature.

---

## ✅ What's in MVP Scope

- **Screen 1 (Unpinned State):**  
  A static note view with an unpinned icon (e.g., outlined pushpin).

- **Screen 2 (Pinned State):**  
  Same note, now with the pin icon in its filled "pinned" state.

- **Screen 3 (Confirmation Toast):**  
  Temporary overlay: `"Note Pinned!"` or `"Note Unpinned!"`

- **Figma Prototype Logic:**  
  - Link Screen 1’s unpinned icon → Screen 3 (toast: *"Note Pinned!"*) → Screen 2  
  - Link Screen 2’s pinned icon → Screen 3 (toast: *"Note Unpinned!"*) → Screen 1

---

## ❌ What's *Out* of MVP Scope

- Backend pinning logic or note list updates  
- Complex animations  
- Persistent data handling  
- Redesigning any other part of the Notes app

---

## 🧪 MVP Assumption

Users will find a **direct, single-tap Pin/Unpin button** significantly faster and more intuitive than the current multi-tap method.  
This redesign will increase user satisfaction, feature discoverability, and pinning frequency.

---

## 🧠 Testing Plan

### 👀 Usability Testing (Moderated)
Present users with the Figma prototype. Ask:
- "Imagine you're in this note and want to quickly pin it. Show me how."
- "Now unpin it."

Observe ease and speed of completion.

### 💬 Qualitative Feedback
Ask follow-up questions:
- "How does this compare to the existing method?"
- "Was it clear what the pin button did?"
- "Would this improve your note-taking workflow?"
- "Were you previously aware of this feature?"

---

## 🔗 Live Prototype  
👉 [View the Figma Prototype](https://www.figma.com/make/WwxkA9J5atwMjfCTjaYoi2/Apple-Notes-Pin-Unpin-Redesign?node-id=0-1&p=f&t=86K6clE2tfKASrOn-0&fullscreen=1)

---

## 🧰 UI Kit Integration

To ensure **scalability, consistency, and maintainability**, this redesign uses reusable components:

- **Pin Button:**  
  Reusable Button component with pinned/unpinned states and subtle animation.

- **Toast Notification:**  
  Non-intrusive "Note Pinned!" and "Note Unpinned!" messages powered by the [Sonner](https://sonner.emilkowal.ski/) Toaster component.

This component-driven approach enhances both **developer experience and UX quality**, allowing focus on meaningful improvements.

---
