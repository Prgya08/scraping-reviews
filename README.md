# 🛍️ Google Reviews Scraper for Smoke Shops in El Paso

This Python Selenium project extracts Google reviews for various smoke shops listed on [elpasosmokeshops.com](https://www.elpasosmokeshops.com/locations/) and saves them into a CSV file.

---

## 🔍 Features

- Scrapes store names from the official website
- Automates Google Maps searches for each store
- Extracts customer reviews by scrolling and parsing visible content
- Saves all reviews in a clean CSV format (`reviews.csv`)

---

## 🚀 Tech Stack

- Python 3.x
- Selenium WebDriver
- Google Chrome + ChromeDriver

---

## 📂 Project Structure

review selenium project/
├── review.py # Main script
├── drivers/
│ └── chromedriver.exe # ChromeDriver executable
├── reviews.csv # Output (auto-generated)
└── README.md # Project info (this file)
