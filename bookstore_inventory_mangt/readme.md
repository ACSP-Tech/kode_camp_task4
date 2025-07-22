# 📚 Bookstore Inventory System

A command-line bookstore management system built with Python. This app allows users to add, view, edit, and purchase books, all managed through a simple menu system. Inventory is stored in a JSON file for persistence.

---

## 🎯 Goal

To build a Python application that manages bookstore inventory with good Git version control practices using feature branches.

---

## 🧩 Features

- ✅ **Book Class**: Represents a book with `title`, `author`, `price`, and `stock`
- 📦 **Inventory Management**: Add, edit, view, purchase, and track book sales
- 💾 **Data Persistence**: Stores all inventory in a `books.json` file
- 🔢 **Price Rounding**: Uses the `math` module to round prices to 2 decimal places
- 🌿 **Git Workflow**: Branching and merging via Git
  - Create a new feature branch:
    ```bash
    git checkout -b feature-search
    ```
  - Merge it back into main:
    ```bash
    git merge feature-search
    ```

---

## 🏗️ Project Structure

bookstore_inventory/
├── inventory.py # Core inventory logic and Book class
├── books.json # Book inventory storage
├── main.py # CLI entry point with menu system
├── README.md # Project documentation