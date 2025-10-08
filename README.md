# A* Pathfinding on Weighted Grid

## 📘 Overview
This project implements the A* search algorithm on a weighted, obstacle-rich grid.  
Each cell has a movement cost (terrain difficulty), and certain cells are impassable obstacles.

The algorithm finds the **shortest-cost path** between a start and goal point, considering both distances and movement costs.

---

## 🧠 Features
- Supports **weighted terrain** and **obstacles**
- Uses **priority queue (heapq)** for efficiency
- Admissible **heuristic function** (Euclidean × min cost)
- Random **grid generation** for varied testing
- Text-based **visualization** of the path

---

## 📂 Project Structure
