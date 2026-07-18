$ cat /workspace/README.md
cat /workspace/README.md
# Password Generator 🛡️
A powerful and secure password generator with a simple and beautiful user interface.
![Banner](./banner.jpeg)
## 📋 Features
This program supports three different types of passwords:
### 1. Random Password
- Configurable length (5 to 50 characters)
- Option to include numbers
- Option to include special symbols
### 2. Memorable Password
- Combination of random words
- Configurable number of words (2 to 4 words)
- Customizable separator between words
- Option for capitalizing first letters
### 3. Pin Code
- Simple numeric code
- Configurable length (4 to 12 digits)
## 🚀 Prerequisites
- Python 3.7 or higher
- Streamlit
## 📦 Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```
2. Install dependencies:
```bash
pip install streamlit
```
## ▶️ How to Run
To run the application, enter the following command in the terminal:
```bash
streamlit run app.py
```
After running, the application will automatically open a tab in your browser.
## 🧪 Testing
To run unit tests, execute the following command:
```bash
python generator.py
```
This command tests all password generation functions.
## 📁 Project Structure
```
├── app.py              # Streamlit user interface
├── generator.py        # Password generation functions
├── banner.jpeg         # Banner image
└── README.md           # Project documentation
```
## 🔧 Functions
### `generate_random_password(length, include_numbers, include_symbols)`
Generate a random password with custom specifications.
### `generate_memorable_password(no_of_words, separator, capitalization, vocabulary)`
Generate a memorable password from a word list.
### `generate_pin(length)`
Generate a numeric pin code.
## 📝 Usage Example
```python
from generator import generate_random_password, generate_memorable_password, generate_pin
# Generate a 12-character random password with numbers and symbols
password = generate_random_password(12, True, True)
# Generate a memorable password with 3 words
memorable = generate_memorable_password(3, '-', True)
# Generate a 6-digit pin
pin = generate_pin(6)
```
## 🤝 Contributing
Contributions are welcome! Please create a Pull Request to submit changes.
## 📄 License
This project is published under the MIT license.
---
**Developed with ❤️ and Python**
