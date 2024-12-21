from random import randint


class Food:
    def __init__(
        self, dimensions: int = 2, x: int = randint(1, 20), y: int = randint(1, 20)
    ):
        self.x = x % 20
        self.y = y % 20
        self.dimensions = dimensions

    def spawn(self):
        pass

    def get_pos(self):
        return (self.x, self.y)

    def __str__(self):
        return f"{self.x}:{self.y}"


class Snake:
    def __init__(self):
        self.direction = "R"
        self.h_pos = [10, 10]
        self.body = [(10, 10)]
        self.score = 0

    def move(self):
        if self.direction == "R":
            self.h_pos[0] += 1
        elif self.direction == "L":
            self.h_pos[0] -= 1
        elif self.direction == "U":
            self.h_pos[1] -= 1
        elif self.direction == "D":
            self.h_pos[1] += 1

        self.body.insert(0, self.h_pos)
        if self.h_pos == apple.get_pos():
            self.score += 1
            apple.spawn()
        else:
            self.body.pop()

    def check_cols(self):
        if self.h_pos in self.body[1:]:
            with open("hs.txt", "r") as file:
                if int(file.read()) > snake.score:
                    with open("hs.txt", "w") as file:
                        file.write(str(snake.score))
            return True
        if (
            self.h_pos[0] > 20
            or self.h_pos[0] < 0
            or self.h_pos[1] > 20
            or self.h_pos[1] < 0
        ):
            with open("hs.txt", "r") as file:
                if int(file.read()) > snake.score:
                    with open("hs.txt", "w") as file:
                        file.write(str(snake.score))
            return True
        else:
            return False


apple = Food()
snake = Snake()
print(apple)
