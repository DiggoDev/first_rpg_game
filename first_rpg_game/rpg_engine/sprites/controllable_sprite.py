class ControllableSprite:
    def init_controllable_sprite(self):
        self.move_directions = {
            'left': False,
            'right': False,
            'up': False,
            'down': False,
        }
        self.direction_prio_x = ''
        self.direction_prio_y = ''

    def movement_left(self, move: bool):
        if move is True:
            if self.move_directions['right'] is True:
                self.direction_prio_x = 'left'
            self.move_directions['left'] = True
        else:
            self.move_directions['left'] = False

    def movement_right(self, move: bool):
        if move is True:
            if self.move_directions['left'] is True:
                self.direction_prio_x = 'right'
            self.move_directions['right'] = True
        else:
            self.move_directions['right'] = False

    def movement_up(self, move: bool):
        if move is True:
            if self.move_directions['down'] is True:
                self.direction_prio_y = 'up'
            self.move_directions['up'] = True
        else:
            self.move_directions['up'] = False

    def movement_down(self, move: bool):
        if move is True:
            if self.move_directions['up'] is True:
                self.direction_prio_y = 'down'
            self.move_directions['down'] = True
        else:
            self.move_directions['down'] = False
