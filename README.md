# 🎨 Map Coloring Problem using CSP (Tkinter GUI)

## 📌 Problem Description

The Map Coloring Problem is a classic **Constraint Satisfaction Problem (CSP)** in Artificial Intelligence. The objective is to assign colors to different regions of a map such that:

* No two adjacent regions share the same color
* Only a limited set of colors is used

This project provides an **interactive GUI-based solution** where users can:

* Add regions dynamically
* Define adjacency relationships
* Select available colors
* Visualize the colored graph

---

## 🧠 Algorithms Used

### 🔹 Constraint Satisfaction Problem (CSP)

The problem is modeled as a CSP with:

* **Variables** → Regions
* **Domains** → Available colors
* **Constraints** → Adjacent regions must have different colors

### 🔹 Backtracking Search

The solution uses a **recursive backtracking algorithm**:

* Assign colors to regions one by one
* Check constraints at each step
* Backtrack when a conflict occurs
* Continue until a valid assignment is found

### 🔹 Constraint Checking

A helper function ensures:

* No neighboring region has the same color

---

## ⚙️ Execution Steps

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Run the application:

```bash
python app.py
```

3. Using the GUI:

* Add regions (e.g., A, B, C, D)
* Define adjacency using dropdowns
* Select available colors
* Click **SOLVE**

4. View results:

* Regions are colored visually
* Solution mapping is displayed

---

## 📊 Sample Input

* Regions: A, B, C, D
* Adjacency:

  * A → B, C
  * B → A, C, D
  * C → A, B, D
  * D → B, C
* Colors: Red, Green, Blue

---

## ✅ Sample Output

```
A → Red  
B → Green  
C → Blue  
D → Red  
```

Graph visualization:

* Each node represents a region
* Colors are assigned dynamically
* Edges represent adjacency

---

## 🎯 Features

* Interactive GUI using Tkinter
* Dynamic graph creation
* Drag-and-drop node positioning
* Real-time constraint validation
* Visual representation of solution

## 🛠️ Tech Stack

* Python
* Tkinter (GUI)
* Backtracking Algorithm (CSP)

---

## 👨‍💻 Author

* Your Name

---

## 📌 Notes

* If no solution exists, the system notifies the user
* Increasing the number of colors improves solvability
