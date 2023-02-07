import random
import pygame
pygame.init()

class Spike:
    def __init__(self, screen_hight, spike_total=10, spike_max=9, spike_min=1, lenth_lvl=4, adding_lvl=0.25) -> None:
        self.spike_total = spike_total
        self.spike_max = spike_max
        self.spike_min = spike_min
        self.nbr_spike = self.spike_min
        self.spike_height = (screen_hight - 100) // self.spike_total
        self.lenth_lvl = lenth_lvl
        self.adding_lvl = adding_lvl
        self.__lvl_up = 0
        self.__lvl = self.spike_min
        self.right = [None]*self.spike_total
        self.left = [None]*self.spike_total
    
    def __repr__(self) -> str:
        return f"{self.left}\n{self.right}\n"

    def reset_spike(self):
        self.right = [None]*self.spike_total
        self.left = [None]*self.spike_total

    def level_update(self):
        self.__lvl_up += 1
        if self.__lvl_up >= self.lenth_lvl:
            self.lenth_lvl += self.adding_lvl
            self.__lvl_up = 0
            self.__lvl += 1
            if self.__lvl > self.spike_max:
                self.__lvl = self.spike_max
        self.nbr_spike = int(self.__lvl)

    def generation_spike(self):
        for i in range(self.nbr_spike):
            pos1 = random.randint(1, self.spike_total-i)
            pos2 = random.randint(1, self.spike_total-i)
            for j in range(self.spike_total):
                if self.right[j] is None:
                    pos1 -= 1
                if pos1 == 0:
                    self.right[j] = 1
                    pos1 = -1
                if self.left[j] is None:
                    pos2 -= 1
                if pos2 == 0:
                    self.left[j] = 1
                    pos2 = -1
                if pos1 < 0 and pos2 < 0:
                    break

    def update(self):
        self.reset_spike()
        self.generation_spike()
        self.level_update()
    
    def affichage(self, screen, screen_size):
        for i in range(self.spike_total):
            if self.left[i]:
                pygame.draw.polygon(screen, (200,200,200), [(0, 50 + i * self.spike_height), (self.spike_height * 0.66, 50 + i * self.spike_height + (self.spike_height * 0.5)), (0, self.spike_height + 50 + i * self.spike_height)])
            if self.right[i]:
                pygame.draw.polygon(screen, (200,200,200), [(screen_size[0], 50 + i * self.spike_height), (screen_size[0] - (self.spike_height * 0.66), 50 + i * self.spike_height + (self.spike_height * 0.5)), (screen_size[0], self.spike_height + 50 + i * self.spike_height)])
