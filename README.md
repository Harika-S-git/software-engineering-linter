# Automated Code Linter and Formatter Workflow

## 📌 Project Overview

This project demonstrates an **automated code quality checking system** using **GitHub Actions** and **Flake8**.

The purpose of the project is to automatically check Python code whenever a **Pull Request** is created. If the code contains style or formatting violations, the GitHub Actions workflow fails. After the developer fixes the issues, the workflow runs again and passes successfully.

## 🎯 Objectives

* Automatically check Python code for style violations.
* Use Flake8 as the Python linter.
* Run the linter automatically using GitHub Actions.
* Demonstrate a failed workflow caused by code-style violations.
* Fix the code and demonstrate a successful workflow.

## 🛠️ Technologies Used

* **Python** – Programming language used for the project.
* **Flake8** – Python linter used to detect coding-style violations.
* **GitHub** – Repository and Pull Request management.
* **GitHub Actions** – Automates the linting process.
* **YAML** – Used to configure the GitHub Actions workflow.

## ⚙️ How It Works

The workflow follows these steps:

```text
Developer writes Python code
          ↓
     Pull Request
          ↓
    GitHub Actions
          ↓
        Flake8
          ↓
     Code is checked
       ↙       ↘
   Errors      No Errors
     ↓             ↓
  ❌ FAIL        ✅ PASS
     ↓
Developer fixes code
     ↓
Push changes
     ↓
GitHub Actions runs again
     ↓
     ✅ PASS
```

## 📁 Project Structure

```text
linter-project/
│
├── calculator.py
│
└── .github/
    └── workflows/
        └── lint.yml
```

### `calculator.py`

Contains the Python code that is checked by Flake8.

### `lint.yml`

Contains the GitHub Actions workflow that automatically installs Flake8 and runs it against the project.

## 🔍 Why Flake8?

Flake8 is a **Python linting tool**. It checks Python code for coding-style and formatting violations and reports the problems.

Flake8 does **not automatically fix the code** in this project.

The developer manually fixes the reported issues and pushes the changes. GitHub Actions then automatically runs Flake8 again.

## 🚀 Workflow Demonstration

### Step 1: Write Code

A Python program is created in `calculator.py`.

### Step 2: Create a Pull Request

A Pull Request is created on GitHub.

### Step 3: Automatic Check

GitHub Actions automatically starts the workflow and runs Flake8.

### Step 4: Failed Check

If Flake8 finds style violations:

```text
❌ Workflow Failed
```

### Step 5: Fix the Code

The developer manually corrects the reported issues.

### Step 6: Push the Fix

The corrected code is pushed to GitHub.

### Step 7: Successful Check

GitHub Actions runs Flake8 again:

```text
✅ Workflow Passed
```

## 📊 Expected Result

The project demonstrates that GitHub Actions can automatically perform code-quality checks before code is merged.

**Before fixing:**

```text
Pull Request → Flake8 → ❌ Failed
```

**After fixing:**

```text
Pull Request → Flake8 → ✅ Passed
```

## ✅ Advantages

* Reduces manual code-style checking.
* Provides quick feedback to developers.
* Encourages consistent coding practices.
* Automatically checks code during Pull Requests.
* Helps maintain better code quality.

## 🏁 Conclusion

This project demonstrates a basic **Continuous Integration (CI)** workflow using GitHub Actions and Flake8.

Instead of manually checking every Python file, Flake8 automatically checks the code when a Pull Request is created. Any detected violations cause the workflow to fail, allowing the developer to fix the code before it is merged.
