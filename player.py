import pygame
pygame.init()
class Player:

    def __init__(self, spike, position: list[float]=[400, 400] , velocity: list[float]=[450,0], acceleration: list[float]=[0,3000], rebound_coeff: list[float]=[1,0], color: tuple[int]=(255,255,100)) -> None:
        self.spike = spike
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.rebound_coeff = rebound_coeff
        self.radius = (self.spike.spike_height * 0.6) * 0.5
        self.color = color
    
    def affichage(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)
    
    def update(self, dt: int, screen_size) -> None:
        dt /= 1000
        self.velocity[0] += self.acceleration[0] * dt
        self.velocity[1] += self.acceleration[1] * dt
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt
        colide_spike = self.collision_detecion(screen_size)
        self.correction_pos(screen_size)
        return colide_spike

    def check_spike(self):
        player_pos = (int(round((self.position[1] + (self.radius*0.7) - (100 - self.radius*0.7)) / self.spike.spike_height)), int(round((self.position[1] - (self.radius*0.7) - (100 - self.radius*0.7)) / self.spike.spike_height)))
        print("player pos", player_pos)
        if player_pos[0] not in range(self.spike.spike_total) or player_pos[1] not in range(self.spike.spike_total):
            return False, False
        return (bool(self.spike.left[player_pos[0]]) or bool(self.spike.left[player_pos[1]])), (bool(self.spike.right[player_pos[0]]) or bool(self.spike.right[player_pos[1]]))

    def collision_detection_x(self, size) -> tuple[bool]:
        return self.position[0] - self.radius <= 0, self.position[0] + self.radius >= size
    
    def collision_detection_y(self, size) -> tuple[bool]:
        return self.position[1] - self.radius <= 0, self.position[1] + self.radius >= size
    
    def collision_detecion(self, screen_size) -> None:
        collide_x, collide_y = self.collision_detection_x(screen_size[0]), self.collision_detection_y(screen_size[1])
        if collide_x[0] or collide_x[1]:
            self.velocity[0] *= - self.rebound_coeff[0]
            collide_spike = self.check_spike()
            self.spike.update()
            return (collide_x[0] and collide_spike[0]) or (collide_x[1] and collide_spike[1])
        if collide_y[0] or collide_y[1]:
            self.velocity[1] *= - self.rebound_coeff[1]
            return True
    
    def correction_pos(self, screen_size) -> None:
        if self.position[0] - self.radius < 0: self.position[0] = 2 * self.radius - self.position[0]
        elif self.position[0] + self.radius > screen_size[0]: self.position[0] = screen_size[0] - self.radius - ((self.position[0] + self.radius) - screen_size[0])
        if self.position[1] - self.radius < 0: self.position[1] = 2 * self.radius - self.position[1]
        elif self.position[1] + self.radius > screen_size[1]: self.position[1] = screen_size[1] - self.radius - ((self.position[1] + self.radius) - screen_size[1])
    
    def jump(self):
        if self.velocity[1] > - 500:
            self.velocity[1] = - 800
        else:
            self.velocity[1] -= 300
