import argparse
import math
from dataclasses import dataclass

import pygame


@dataclass
class Vec3:
    x: float
    y: float
    z: float


class Cube3DAnimation:
    def __init__(self, width: int = 1000, height: int = 700) -> None:
        self.width = width
        self.height = height
        self.center_x = width // 2
        self.center_y = height // 2

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("3D Animation Sample - Rotating Cube")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Helvetica", 22, bold=True)

        self.background_color = (10, 14, 30)
        self.edge_color = (96, 165, 250)
        self.vertex_color = (248, 250, 252)
        self.text_color = (203, 213, 225)

        self.vertices = [
            Vec3(-1, -1, -1),
            Vec3(1, -1, -1),
            Vec3(1, 1, -1),
            Vec3(-1, 1, -1),
            Vec3(-1, -1, 1),
            Vec3(1, -1, 1),
            Vec3(1, 1, 1),
            Vec3(-1, 1, 1),
        ]

        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7),
        ]

        self.scale = 170
        self.camera_distance = 4.2
        self.rotation_speed = 1.0

        self.angle_x = 0.0
        self.angle_y = 0.0
        self.angle_z = 0.0

    def rotate_x(self, point: Vec3, angle: float) -> Vec3:
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        return Vec3(
            point.x,
            point.y * cos_a - point.z * sin_a,
            point.y * sin_a + point.z * cos_a,
        )

    def rotate_y(self, point: Vec3, angle: float) -> Vec3:
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        return Vec3(
            point.x * cos_a + point.z * sin_a,
            point.y,
            -point.x * sin_a + point.z * cos_a,
        )

    def rotate_z(self, point: Vec3, angle: float) -> Vec3:
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        return Vec3(
            point.x * cos_a - point.y * sin_a,
            point.x * sin_a + point.y * cos_a,
            point.z,
        )

    def project(self, point: Vec3) -> tuple[int, int]:
        perspective = self.camera_distance / (self.camera_distance - point.z)
        x_2d = int(point.x * perspective * self.scale + self.center_x)
        y_2d = int(point.y * perspective * self.scale + self.center_y)
        return x_2d, y_2d

    def draw_hud(self) -> None:
        lines = [
            "3D Animation Sample: Rotating Cube",
            "Controls: LEFT/RIGHT adjust speed, SPACE pause/resume, ESC quit",
            f"Rotation speed: {self.rotation_speed:.2f}x",
        ]

        for index, text in enumerate(lines):
            surface = self.font.render(text, True, self.text_color)
            self.screen.blit(surface, (20, 20 + index * 28))

    def run(self, max_seconds: float | None = None) -> None:
        running = True
        paused = False
        elapsed = 0.0

        while running:
            dt = self.clock.tick(60) / 1000.0
            elapsed += dt

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_SPACE:
                        paused = not paused
                    elif event.key == pygame.K_LEFT:
                        self.rotation_speed = max(0.1, self.rotation_speed - 0.1)
                    elif event.key == pygame.K_RIGHT:
                        self.rotation_speed = min(5.0, self.rotation_speed + 0.1)

            if max_seconds is not None and elapsed >= max_seconds:
                running = False

            if not paused:
                self.angle_x += 0.9 * dt * self.rotation_speed
                self.angle_y += 1.2 * dt * self.rotation_speed
                self.angle_z += 0.6 * dt * self.rotation_speed

            transformed = []
            for vertex in self.vertices:
                rotated = self.rotate_x(vertex, self.angle_x)
                rotated = self.rotate_y(rotated, self.angle_y)
                rotated = self.rotate_z(rotated, self.angle_z)
                transformed.append(rotated)

            projected = [self.project(point) for point in transformed]

            self.screen.fill(self.background_color)

            for start_index, end_index in self.edges:
                pygame.draw.line(
                    self.screen,
                    self.edge_color,
                    projected[start_index],
                    projected[end_index],
                    width=3,
                )

            for point in projected:
                pygame.draw.circle(self.screen, self.vertex_color, point, 6)

            self.draw_hud()
            pygame.display.flip()

        pygame.quit()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sample 3D cube animation using pygame")
    parser.add_argument(
        "--seconds",
        type=float,
        default=None,
        help="Auto-close after N seconds (useful for quick test runs)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    Cube3DAnimation().run(max_seconds=args.seconds)
