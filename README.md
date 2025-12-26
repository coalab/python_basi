# Python Educational Website

This project is a web application designed to help middle school students learn Python programming through interactive examples. The application is built using Flask and provides a user-friendly interface for exploring various Python concepts.

## Project Structure

```
python-edu-site
├── src
│   ├── app.py                # Main entry point of the web application
│   ├── templates             # HTML templates for the web pages
│   │   ├── index.html        # Homepage
│   │   ├── examples.html     # Page listing Python examples
│   │   └── about.html        # About page with project information
│   ├── static                # Static files (CSS, JS)
│   │   ├── style.css         # Styles for the web application
│   │   └── script.js         # JavaScript for interactive features
│   └── examples              # Python example scripts
│       ├── basic_print.py    # Example of using the print function
│       ├── variables.py      # Example of variable declaration and usage
│       ├── loops.py          # Examples of using loops in Python
│       └── functions.py      # Example of defining and calling functions
├── requirements.txt          # Dependencies for the project
├── README.md                 # Documentation for the project
└── .gitignore                # Files and directories to ignore by Git
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd python-edu-site
   ```

2. **Install dependencies:**
   Make sure you have Python and pip installed. Then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```
   python src/app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Usage Guidelines

- Visit the homepage to get an introduction to the site and navigate to the examples page.
- Explore various Python examples that are suitable for middle school students.
- Each example includes a description and a link to the corresponding Python script.

## Overview of Examples

- **Basic Print:** Learn how to output text to the console using the print function.
- **Variables:** Understand how to declare and use variables in Python.
- **Loops:** Discover how to use for and while loops to iterate over data.
- **Functions:** Explore how to define and call functions for code reusability.

## Contact

For any inquiries or feedback, please reach out to the project maintainers.