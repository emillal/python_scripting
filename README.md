# python_scripting
Python scripting Project for Parsing and automation of data

# Game Directory Organizer

This project organizes Go-based game directories from a given `/data` folder into a cleaner `/games` directory, compiles the Go code, and runs each game.

## 📁 Assumptions

- The `/data` directory contains many files and subdirectories.
- Only the directories related to games are of interest.
- A game directory contains the word `"game"` in its name.
- Each game directory contains a **single `.go` file** that needs to be compiled and run.

## 🚀 Project Steps

1. **Find** all game directories inside `/data` (i.e., those containing `"game"` in the directory name).
2. **Create** a new `/games` directory.
3. **Copy and rename** each game directory by removing the `"game"` suffix and placing it into the `/games` directory.
4. **Generate** a `.json` file with metadata (e.g., original name, new name, path).
5. **Compile** all `.go` files inside the `/games` directory.
6. **Run** each compiled game binary.

## 📂 Example

If `/data` contains:

