<div align="center">
  <img src="./data/banner.png" alt="Mr. Le Président" width="100%" />

  # 🎖️ Mr. Le Président

  > A narrative game where every decision shapes the fate of a nation.

  ![Python](https://img.shields.io/badge/Python-3.14.2-blue?style=flat-square&logo=python)
  ![Pygame](https://img.shields.io/badge/pygame--ce-2.5.6-green?style=flat-square)
  ![License](https://img.shields.io/badge/Code-GPL%20v3-red?style=flat-square)
  ![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=flat-square)
  ![NSI](https://img.shields.io/badge/Trophée%20NSI-2026-gold?style=flat-square)

</div>

---

## 🗺️ About

**Mr. Le Président** is a narrative decision-making game inspired by *Lapse: A Forgotten Future*.  
You play as the president of a near-futuristic nation at war. State officials will present you with decisions to manage national crises — war, economy, politics — and your choices will determine the fate of your country across **10 different endings**.

---

## ⚙️ Requirements

- [Python 3.14.2](https://www.python.org/downloads/)
- pygame-ce 2.5.6

---

## 📥 Installation

**1. Clone the repository**
```bash
git clone https://github.com/TroTro34/mr-le-president.git
cd mr-le-president
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the game**
```bash
python sources/main.py
```

---

## 🎮 How to Play

| Action | Control |
|--------|---------|
| Advance text / intro | Left click anywhere |
| Choose YES | Left button |
| Choose NO | Right button |
| Quit | `Échap` |

> Only a mouse is needed to play. No prior gaming experience required.

---

## 📁 Project Structure

```
mr-le-president/
├── sources/
│   └── main.py
├── data/
│   ├── histoire.txt       # Situation dialogues
│   ├── question.txt       # Decision questions
│   ├── intro.txt          # Introduction text
│   ├── Assistant.png      # Character sprites
│   ├── Général.png
│   ├── vraiYES.png        # Buttons
│   ├── vraiNON.png
│   ├── Capture it.ttf     # Fonts
│   └── Sakire.ttf
├── requirements.txt
├── licence.txt
└── README.md
```

---

## 👥 Team

| Name | Role |
|------|------|
| **Maxence** (TroTro) | Game systems, gauges, text display |
| **Laura** | Special dialogue system, character design |
| **Apolline** | Characters, backgrounds, visual effects |

---

## 📜 License

- **Source code** → [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.fr.html)
- **Documentation & texts** → [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr)
