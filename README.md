# Wordle Clone in Python (Pygame)

A simple clone of the popular word game **Wordle**, implemented using Python and Pygame.

## 🎮 Features

* Grid-based input for guesses
* Real-time feedback with colored tiles:

  * 🟩 Green: Correct letter, correct position
  * 🟨 Yellow: Correct letter, wrong position
  * ⬛ Grey: Incorrect letter
  
* Pulsing animation on tile state change
* Error message display for invalid words
* Random or fixed target word
* Validity check using an English word list

---

## 🛠️ Requirements

* Python 3.7+
* Pygame

Install dependencies:

```bash
pip install pygame
```

---

## 📁 Project Structure

```
wordle/
│
├── main.py                # Main game loop
├── grid_cell.py           # Grid cell logic and drawing
├── word_guess.py          # Game logic and word validation
├── display_message.py     # For temporary messages like "invalid word"
├── words_dictionary.json  # JSON file containing valid words
└── README.md
```

---

## 📚 How to Play

* You have 6 attempts to guess a 5-letter word.
* After each guess, tiles will change color based on accuracy.
* Use your physical keyboard to type.
* Only valid English words are accepted.

---

## ⚙️ Customization

* **Target Word**: You can specify a word or allow the game to pick a random one.
* **Word List**: Update `words_dictionary.json` to use a custom word list.
* **Word Lenght**: You can play this game with words of any length, that needs to be specified before starting.

---

## 🧠 Credits

Built by Harshul using [Python](https://www.python.org/) and [Pygame](https://www.pygame.org/).

---

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/64546f3f-f1a3-45e0-969f-83a1f7ae6a3f)

