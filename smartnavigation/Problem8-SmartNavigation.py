import tkinter as tk
from tkinter import ttk, messagebox
from collections import deque
import math

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    explored = []

    while queue:
        node, path = queue.popleft()
        if node not in visited:
            visited.add(node)
            explored.append(node)
            if node == goal:
                return path, explored
            for n in graph.get(node, []):
                queue.append((n, path + [n]))
    return None, explored

def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]
    explored = []

    while stack:
        node, path = stack.pop()
        if node not in visited:
            visited.add(node)
            explored.append(node)
            if node == goal:
                return path, explored
            for n in graph.get(node, []):
                stack.append((n, path + [n]))
    return None, explored

class NavigationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Navigation – BFS & DFS")
        self.root.geometry("900x620")
        self.root.configure(bg="#1e1e2e")

        self.nodes = []
        self.graph = {}
        self.pos = {}
        self.dragging = None

        self._build_ui()

    def _build_ui(self):
        left = tk.Frame(self.root, bg="#2a2a3e", width=260)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=(12,0), pady=12)
        left.pack_propagate(False)

        tk.Label(left, text="SMART NAVIGATION", bg="#2a2a3e", fg="#a78bfa",
                 font=("Courier", 11, "bold")).pack(pady=(16,2))
        tk.Label(left, text="BFS / DFS", bg="#2a2a3e", fg="#6b7280",
                 font=("Courier", 9)).pack(pady=(0,14))

        self._section(left, "ADD NODE")
        self.node_entry = self._entry(left, "Node name")
        tk.Button(left, text="+ Add Node", command=self._add_node,
                  bg="#7c3aed", fg="white", font=("Courier", 9, "bold"),
                  relief=tk.FLAT).pack(fill=tk.X, padx=12, pady=(0,12))

        self._section(left, "ADD EDGE")
        self.edge_a = self._dropdown(left, "From")
        self.edge_b = self._dropdown(left, "To")
        tk.Button(left, text="+ Add Edge", command=self._add_edge,
                  bg="#7c3aed", fg="white", font=("Courier", 9, "bold"),
                  relief=tk.FLAT).pack(fill=tk.X, padx=12, pady=(0,12))

        self._section(left, "START / GOAL")
        self.start_cb = self._dropdown(left, "Start")
        self.goal_cb = self._dropdown(left, "Goal")

        tk.Button(left, text="▶ BFS", command=self._run_bfs,
                  bg="#059669", fg="white", font=("Courier", 10, "bold"),
                  relief=tk.FLAT).pack(fill=tk.X, padx=12, pady=3)

        tk.Button(left, text="▶ DFS", command=self._run_dfs,
                  bg="#2563eb", fg="white", font=("Courier", 10, "bold"),
                  relief=tk.FLAT).pack(fill=tk.X, padx=12, pady=3)

        tk.Button(left, text="✕ Clear", command=self._clear,
                  bg="#374151", fg="#d1d5db",
                  font=("Courier", 9), relief=tk.FLAT).pack(fill=tk.X, padx=12, pady=6)

        right = tk.Frame(self.root, bg="#1e1e2e")
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=12, pady=12)

        self.canvas = tk.Canvas(right, bg="#12121f", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.result = tk.Label(right, text="", bg="#1e1e2e",
                               fg="#a78bfa", font=("Courier", 9),
                               justify=tk.LEFT, wraplength=580)
        self.result.pack(anchor=tk.W, pady=6)

        self.canvas.bind("<ButtonPress-1>", self._press)
        self.canvas.bind("<B1-Motion>", self._drag)
        self.canvas.bind("<ButtonRelease-1>", self._release)

    def _section(self, parent, text):
        tk.Label(parent, text=text, bg="#2a2a3e", fg="#6b7280",
                 font=("Courier", 8, "bold")).pack(anchor=tk.W, padx=12, pady=(8,2))

    def _entry(self, parent, placeholder):
        e = tk.Entry(parent, bg="#1e1e2e", fg="white", insertbackground="white")
        e.pack(fill=tk.X, padx=12, pady=4)
        e.insert(0, placeholder)
        return e

    def _dropdown(self, parent, label):
        tk.Label(parent, text=label, bg="#2a2a3e", fg="#9ca3af",
                 font=("Courier", 8)).pack(anchor=tk.W, padx=16)
        cb = ttk.Combobox(parent, values=[], state="readonly")
        cb.pack(fill=tk.X, padx=12, pady=4)
        return cb

    def _refresh(self):
        vals = self.nodes[:]
        self.edge_a["values"] = vals
        self.edge_b["values"] = vals
        self.start_cb["values"] = vals
        self.goal_cb["values"] = vals

    def _add_node(self):
        n = self.node_entry.get().strip()
        if not n:
            return
        if n in self.nodes:
            return
        self.nodes.append(n)
        self.graph[n] = []
        self._refresh()
        self._layout()
        self._draw()

    def _add_edge(self):
        a = self.edge_a.get()
        b = self.edge_b.get()
        if not a or not b or a == b:
            return
        if b not in self.graph[a]:
            self.graph[a].append(b)
        if a not in self.graph[b]:
            self.graph[b].append(a)
        self._draw()

    def _layout(self):
        n = len(self.nodes)
        cx, cy, r = 350, 250, 160
        for i, node in enumerate(self.nodes):
            angle = 2 * math.pi * i / max(n,1)
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            self.pos[node] = (x, y)

    def _draw(self):
        self.canvas.delete("all")
        for u in self.graph:
            x1, y1 = self.pos.get(u, (0,0))
            for v in self.graph[u]:
                x2, y2 = self.pos.get(v, (0,0))
                self.canvas.create_line(x1, y1, x2, y2, fill="#374151", width=2)
        for n in self.nodes:
            x, y = self.pos[n]
            self.canvas.create_oval(x-25, y-25, x+25, y+25,
                                    fill="#7c3aed", outline="#a78bfa", width=2)
            self.canvas.create_text(x, y, text=n, fill="white",
                                    font=("Courier", 10, "bold"))

    def _run_bfs(self):
        s = self.start_cb.get()
        g = self.goal_cb.get()
        if not s or not g:
            return
        path, explored = bfs(self.graph, s, g)
        if path:
            self.result.config(text=f"BFS Path: {' → '.join(path)}\nNodes: {explored}", fg="#22c55e")
        else:
            self.result.config(text="No path found", fg="#ef4444")

    def _run_dfs(self):
        s = self.start_cb.get()
        g = self.goal_cb.get()
        if not s or not g:
            return
        path, explored = dfs(self.graph, s, g)
        if path:
            self.result.config(text=f"DFS Path: {' → '.join(path)}\nNodes: {explored}", fg="#3b82f6")
        else:
            self.result.config(text="No path found", fg="#ef4444")

    def _press(self, e):
        for n in self.nodes:
            x, y = self.pos[n]
            if abs(e.x-x) < 25 and abs(e.y-y) < 25:
                self.dragging = n

    def _drag(self, e):
        if self.dragging:
            self.pos[self.dragging] = (e.x, e.y)
            self._draw()

    def _release(self, e):
        self.dragging = None

    def _clear(self):
        self.nodes.clear()
        self.graph.clear()
        self.pos.clear()
        self.result.config(text="")
        self._refresh()
        self._draw()

root = tk.Tk()
app = NavigationApp(root)
root.mainloop()