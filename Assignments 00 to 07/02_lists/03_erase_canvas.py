# Problem Statement
# Implement an 'eraser' on a canvas.

# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.


import tkinter as tk

CELL_SIZE = 40
ROWS = 10
COLS = 10
ERASER_SIZE = 60

class EraserCanvasApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="white")
        self.canvas.pack()

        self.cells = {}  # Store cell rectangles by ID
        self.draw_grid()

        # Create the eraser
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="gray")

        # Bind mouse drag to eraser movement
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def draw_grid(self):
        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")
                self.cells[rect] = (x1, y1, x2, y2)

    def move_eraser(self, event):
        # Move the eraser to where the mouse is
        x1 = event.x - ERASER_SIZE / 2
        y1 = event.y - ERASER_SIZE / 2
        x2 = x1 + ERASER_SIZE
        y2 = y1 + ERASER_SIZE
        self.canvas.coords(self.eraser, x1, y1, x2, y2)

        # Check intersection with cells
        for rect_id, (cx1, cy1, cx2, cy2) in self.cells.items():
            # Check overlap
            if not (x2 < cx1 or x1 > cx2 or y2 < cy1 or y1 > cy2):
                self.canvas.itemconfig(rect_id, fill="white")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Eraser Canvas")
    app = EraserCanvasApp(root)
    root.mainloop()
