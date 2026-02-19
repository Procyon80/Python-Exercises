import math
import random
import importlib
from pathlib import Path
from typing import Any

tk: Any = None
pygame: Any = None
pil_image: Any = None
pil_draw: Any = None

try:
    tk = importlib.import_module("tkinter")
except ModuleNotFoundError:
    pass

try:
    pygame = importlib.import_module("pygame")
except ModuleNotFoundError:
    pass

try:
    pil_image = importlib.import_module("PIL.Image")
    pil_draw = importlib.import_module("PIL.ImageDraw")
except ModuleNotFoundError:
    pass


class OrbitAnimation:
    def __init__(self) -> None:
        self.width = 900
        self.height = 600
        self.center_x = self.width // 2
        self.center_y = self.height // 2

        self.window = tk.Tk()
        self.window.title("Sample Graphic Animation")
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)

        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height, bg="#0b1020", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.time_step = 0.0
        self.stars = self._create_stars(120)

        self.orbits = [80, 145, 220]
        self.speeds = [2.5, 1.5, 0.9]
        self.sizes = [12, 18, 24]
        self.colors = ["#56cfe1", "#ffd166", "#ef476f"]

        self.status_text = self.canvas.create_text(
            20,
            20,
            anchor="nw",
            fill="#cbd5e1",
            font=("Helvetica", 14, "bold"),
            text="Graphic Animation Demo",
        )

    def _create_stars(self, count: int) -> list[tuple[float, float, float, str]]:
        stars: list[tuple[float, float, float, str]] = []
        for _ in range(count):
            x_position = random.uniform(0, self.width)
            y_position = random.uniform(0, self.height)
            radius = random.uniform(0.8, 2.2)
            color = random.choice(["#e2e8f0", "#cbd5e1", "#94a3b8"])
            stars.append((x_position, y_position, radius, color))
        return stars

    def draw_background(self) -> None:
        self.canvas.delete("all")
        for x_position, y_position, radius, color in self.stars:
            self.canvas.create_oval(
                x_position - radius,
                y_position - radius,
                x_position + radius,
                y_position + radius,
                fill=color,
                outline=color,
            )

    def draw_sun(self) -> None:
        glow = 50 + 8 * math.sin(self.time_step)
        self.canvas.create_oval(
            self.center_x - glow,
            self.center_y - glow,
            self.center_x + glow,
            self.center_y + glow,
            fill="#ffb703",
            outline="",
            stipple="gray25",
        )
        self.canvas.create_oval(
            self.center_x - 36,
            self.center_y - 36,
            self.center_x + 36,
            self.center_y + 36,
            fill="#ffdd57",
            outline="#ffd166",
            width=2,
        )

    def draw_orbits(self) -> None:
        for radius in self.orbits:
            self.canvas.create_oval(
                self.center_x - radius,
                self.center_y - radius,
                self.center_x + radius,
                self.center_y + radius,
                outline="#334155",
                width=1,
            )

    def draw_planets(self) -> None:
        for orbit_radius, speed, size, color in zip(self.orbits, self.speeds, self.sizes, self.colors):
            angle = self.time_step * speed
            x_position = self.center_x + orbit_radius * math.cos(angle)
            y_position = self.center_y + orbit_radius * math.sin(angle)

            self.canvas.create_oval(
                x_position - size,
                y_position - size,
                x_position + size,
                y_position + size,
                fill=color,
                outline="#e2e8f0",
                width=1,
            )

            self.canvas.create_line(
                self.center_x,
                self.center_y,
                x_position,
                y_position,
                fill="#1e293b",
                width=1,
                dash=(3, 5),
            )

    def animate(self) -> None:
        self.draw_background()
        self.draw_orbits()
        self.draw_sun()
        self.draw_planets()

        self.canvas.itemconfig(
            self.status_text,
            text=f"Graphic Animation Demo    t={self.time_step:0.2f}",
        )

        self.time_step += 0.035
        self.window.after(16, self.animate)

    def run(self) -> None:
        self.animate()
        self.window.mainloop()


class OrbitAnimationPygame:
    def __init__(self) -> None:
        self.width = 900
        self.height = 600
        self.center_x = self.width // 2
        self.center_y = self.height // 2

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sample Graphic Animation")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Helvetica", 22, bold=True)

        self.time_step = 0.0
        self.stars = self._create_stars(120)
        self.orbits = [80, 145, 220]
        self.speeds = [2.5, 1.5, 0.9]
        self.sizes = [12, 18, 24]
        self.colors = [(86, 207, 225), (255, 209, 102), (239, 71, 111)]

    def _create_stars(self, count: int) -> list[tuple[float, float, float, tuple[int, int, int]]]:
        stars: list[tuple[float, float, float, tuple[int, int, int]]] = []
        star_palette = [(226, 232, 240), (203, 213, 225), (148, 163, 184)]
        for _ in range(count):
            x_position = random.uniform(0, self.width)
            y_position = random.uniform(0, self.height)
            radius = random.uniform(1.0, 2.4)
            stars.append((x_position, y_position, radius, random.choice(star_palette)))
        return stars

    def _draw_background(self) -> None:
        self.screen.fill((11, 16, 32))
        for x_position, y_position, radius, color in self.stars:
            pygame.draw.circle(self.screen, color, (int(x_position), int(y_position)), int(radius))

    def _draw_orbits(self) -> None:
        for radius in self.orbits:
            pygame.draw.circle(self.screen, (51, 65, 85), (self.center_x, self.center_y), radius, width=1)

    def _draw_sun(self) -> None:
        glow = int(50 + 8 * math.sin(self.time_step))
        pygame.draw.circle(self.screen, (255, 183, 3), (self.center_x, self.center_y), glow)
        pygame.draw.circle(self.screen, (255, 221, 87), (self.center_x, self.center_y), 36)

    def _draw_planets(self) -> None:
        for orbit_radius, speed, size, color in zip(self.orbits, self.speeds, self.sizes, self.colors):
            angle = self.time_step * speed
            x_position = self.center_x + orbit_radius * math.cos(angle)
            y_position = self.center_y + orbit_radius * math.sin(angle)

            pygame.draw.line(
                self.screen,
                (30, 41, 59),
                (self.center_x, self.center_y),
                (int(x_position), int(y_position)),
                1,
            )
            pygame.draw.circle(self.screen, color, (int(x_position), int(y_position)), size)
            pygame.draw.circle(self.screen, (226, 232, 240), (int(x_position), int(y_position)), size, width=1)

    def _draw_status(self) -> None:
        label = self.font.render(f"Graphic Animation Demo    t={self.time_step:0.2f}", True, (203, 213, 225))
        self.screen.blit(label, (20, 20))

    def run(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self._draw_background()
            self._draw_orbits()
            self._draw_sun()
            self._draw_planets()
            self._draw_status()

            pygame.display.flip()
            self.time_step += 0.035
            self.clock.tick(60)

        pygame.quit()


class OrbitAnimationGif:
    def __init__(self) -> None:
        self.width = 900
        self.height = 600
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        self.time_step = 0.0
        self.stars = self._create_stars(120)
        self.orbits = [80, 145, 220]
        self.speeds = [2.5, 1.5, 0.9]
        self.sizes = [12, 18, 24]
        self.colors = [(86, 207, 225), (255, 209, 102), (239, 71, 111)]

    def _create_stars(self, count: int) -> list[tuple[float, float, float, tuple[int, int, int]]]:
        stars: list[tuple[float, float, float, tuple[int, int, int]]] = []
        star_palette = [(226, 232, 240), (203, 213, 225), (148, 163, 184)]
        for _ in range(count):
            stars.append(
                (
                    random.uniform(0, self.width),
                    random.uniform(0, self.height),
                    random.uniform(1.0, 2.4),
                    random.choice(star_palette),
                )
            )
        return stars

    def _draw_frame(self) -> Any:
        image = pil_image.new("RGB", (self.width, self.height), (11, 16, 32))
        drawer = pil_draw.Draw(image)

        for x_position, y_position, radius, color in self.stars:
            drawer.ellipse(
                (
                    x_position - radius,
                    y_position - radius,
                    x_position + radius,
                    y_position + radius,
                ),
                fill=color,
            )

        for radius in self.orbits:
            drawer.ellipse(
                (
                    self.center_x - radius,
                    self.center_y - radius,
                    self.center_x + radius,
                    self.center_y + radius,
                ),
                outline=(51, 65, 85),
                width=1,
            )

        glow = int(50 + 8 * math.sin(self.time_step))
        drawer.ellipse(
            (
                self.center_x - glow,
                self.center_y - glow,
                self.center_x + glow,
                self.center_y + glow,
            ),
            fill=(255, 183, 3),
        )
        drawer.ellipse(
            (
                self.center_x - 36,
                self.center_y - 36,
                self.center_x + 36,
                self.center_y + 36,
            ),
            fill=(255, 221, 87),
            outline=(255, 209, 102),
            width=2,
        )

        for orbit_radius, speed, size, color in zip(self.orbits, self.speeds, self.sizes, self.colors):
            angle = self.time_step * speed
            x_position = self.center_x + orbit_radius * math.cos(angle)
            y_position = self.center_y + orbit_radius * math.sin(angle)

            drawer.line(
                (
                    self.center_x,
                    self.center_y,
                    x_position,
                    y_position,
                ),
                fill=(30, 41, 59),
                width=1,
            )
            drawer.ellipse(
                (
                    x_position - size,
                    y_position - size,
                    x_position + size,
                    y_position + size,
                ),
                fill=color,
                outline=(226, 232, 240),
                width=1,
            )

        self.time_step += 0.08
        return image

    def run(self) -> None:
        output_path = Path.cwd() / "orbit_animation.gif"
        frames = [self._draw_frame() for _ in range(120)]
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            loop=0,
            duration=33,
            optimize=False,
        )
        print(f"Generated animated GIF: {output_path}")


def run_animation() -> None:
    if pygame is not None:
        print("Using pygame backend for live animation.")
        OrbitAnimationPygame().run()
        return

    if tk is not None:
        print("Pygame unavailable. Using Tkinter backend.")
        OrbitAnimation().run()
        return

    if pil_image is not None and pil_draw is not None:
        print("Tkinter and pygame are unavailable. Generating GIF with Pillow backend.")
        OrbitAnimationGif().run()
        return

    raise SystemExit(
        "No graphics backend available.\n"
        "Option 1 (quick): pip install pygame\n"
        "Option 2 (Tkinter): install/use a Python build that includes Tk support\n"
        "Option 3 (Pillow): pip install pillow"
    )


if __name__ == "__main__":
    run_animation()
