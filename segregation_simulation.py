import random as r
import graphics as g
import time as t

class SegregationSimulation:
    def __init__(self, similar: float, ratio: float, empty: float, size: int, delay: float):
        self.similar = similar
        self.size = size
        self.delay = delay
        self.grid = self.create_grid(ratio, empty)
        self.win = self.make_win()

    def create_grid(self, ratio: float, empty: float):
        empty_count = int(empty * (self.size ** 2))
        fill_count = (self.size ** 2) - empty_count
        red_count = int(fill_count * ratio)
        blue_count = fill_count - red_count

        agents = ['e'] * empty_count + ['r'] * red_count + ['b'] * blue_count
        r.shuffle(agents)
        return [agents[i * self.size:(i + 1) * self.size] for i in range(self.size)]

    def is_satisfied(self, row: int, col: int) -> bool:
        agent = self.grid[row][col]
        neighbors = [(row + r_offset, col + c_offset) 
                     for r_offset in (-1, 0, 1) for c_offset in (-1, 0, 1)
                     if (r_offset, c_offset) != (0, 0) and 0 <= row + r_offset < self.size and 0 <= col + c_offset < self.size]
        
        sim_count = sum(1 for n_row, n_col in neighbors if self.grid[n_row][n_col] == agent)
        total_neighbors = sum(1 for n_row, n_col in neighbors if self.grid[n_row][n_col] != 'e')

        return total_neighbors == 0 or sim_count / total_neighbors >= self.similar

    def update_grid(self):
        empty_slots = [(row, col) for row in range(self.size) for col in range(self.size) if self.grid[row][col] == 'e']
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] != 'e' and not self.is_satisfied(row, col):
                    if empty_slots:
                        empty_slot = r.choice(empty_slots)
                        self.grid[empty_slot[0]][empty_slot[1]] = self.grid[row][col]
                        self.grid[row][col] = 'e'
                        empty_slots.remove(empty_slot)

    def draw_grid(self, iteration: int):
        for row in range(self.size):
            for col in range(self.size):
                color = {"r": "red", "b": "blue", "e": "white"}[self.grid[row][col]]
                rect = g.Rectangle(g.Point(col, row), g.Point(col + 1, row + 1))
                rect.setFill(color)
                rect.draw(self.win)

        g.Text(g.Point(self.size / 2, self.size + 0.5), f"Round {iteration}").draw(self.win)
        g.update()

    def make_win(self):
        win = g.GraphWin("Segregation Simulation", 400, 400, autoflush=False)
        win.setCoords(-1, -1, self.size, self.size)
        return win

    def run(self):
        iteration = 1
        while True:
            t.sleep(self.delay)
            self.update_grid()
            self.clear_window()
            self.draw_grid(iteration)
            iteration += 1

            if self.get_per_satisfied() == 1:
                break

        self.win.getMouse()  # Wait for mouse click
        self.win.close()

    def clear_window(self):
        for item in self.win.items[:]:
            item.undraw()

    def get_per_satisfied(self):
        total_agents = self.size ** 2 - sum(row.count('e') for row in self.grid)
        satisfied_agents = sum(1 for row in range(self.size) for col in range(self.size)
                               if self.grid[row][col] != 'e' and self.is_satisfied(row, col))
        return satisfied_agents / total_agents if total_agents > 0 else 0

if __name__ == "__main__":
    sim = SegregationSimulation(similar=0.7, ratio=0.3, empty=0.4, size=20, delay=0.1)
    sim.run()