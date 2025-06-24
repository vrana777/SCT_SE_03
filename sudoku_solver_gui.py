import tkinter as tk
from tkinter import messagebox

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("🧩 Sudoku Solver")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.root, width=2, font=("Helvetica", 18), justify="center")
                entry.grid(row=row, column=col, padx=2, pady=2)
                self.cells[row][col] = entry

    def create_buttons(self):
        solve_btn = tk.Button(self.root, text="Solve", command=self.solve_puzzle, bg="#4CAF50", fg="white", width=10)
        solve_btn.grid(row=9, column=0, columnspan=4, pady=10)

        clear_btn = tk.Button(self.root, text="Clear", command=self.clear_grid, bg="#f44336", fg="white", width=10)
        clear_btn.grid(row=9, column=5, columnspan=4, pady=10)

    def read_grid(self):
        board = []
        for row in range(9):
            current_row = []
            for col in range(9):
                val = self.cells[row][col].get()
                if val == "":
                    current_row.append(0)
                else:
                    try:
                        num = int(val)
                        if 1 <= num <= 9:
                            current_row.append(num)
                        else:
                            raise ValueError
                    except ValueError:
                        messagebox.showerror("Invalid Input", f"Invalid number at ({row+1}, {col+1})")
                        return None
            board.append(current_row)
        return board

    def fill_grid(self, board):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                if board[row][col] != 0:
                    self.cells[row][col].insert(0, str(board[row][col]))

    def is_valid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        start_row = row - row % 3
        start_col = col - col % 3

        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False

        return True

    def solve(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    def solve_puzzle(self):
        board = self.read_grid()
        if board and self.solve(board):
            self.fill_grid(board)
            messagebox.showinfo("Success", "Sudoku solved successfully!")
        elif board:
            messagebox.showerror("Unsolvable", "This Sudoku puzzle cannot be solved.")

    def clear_grid(self):
        for row in self.cells:
            for cell in row:
                cell.delete(0, tk.END)

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolver(root)
    root.mainloop()
