import pygame as pg
from pytmx.util_pygame import load_pygame

from GameUI import GameUI
from BGObject import BGObject
from Camera import Camera
from Event import Event
from Flag import Flag
from Const import *
from Platform import Platform
from Player import Player
from Goombas import Goombas
from Mushroom import Mushroom
from Flower import Flower
from Koopa import Koopa
from Tube import Tube
from PlatformDebris import PlatformDebris
from CoinDebris import CoinDebris
from Fireball import Fireball
from Text import Text


class Map(object):
    """

    Esta classe contém todos os objetos do mapa: blocos, inimigos e jogador.
    Também guarda a câmera, os eventos e a interface (HUD).

    """

    def __init__(self, world_num):
        self.obj = []
        self.obj_bg = []
        self.tubes = []
        self.debris = []
        self.mobs = []
        self.projectiles = []
        self.text_objects = []
        self.map = 0
        self.flag = None

        self.mapSize = (0, 0)
        self.sky = 0

        self.textures = {}
        self.worldNum = world_num
        self.loadWorld_11()

        self.is_mob_spawned = [False, False]
        self.score_for_killing_mob = 100
        self.score_time = 0

        self.in_event = False
        self.tick = 0
        self.time = 400

        self.oPlayer = Player(x_pos=128, y_pos=351)
        self.oCamera = Camera(self.mapSize[0] * 32, 14)
        self.oEvent = Event()
        self.oGameUI = GameUI()

    def loadWorld_11(self):
        tmx_data = load_pygame("worlds/1-1/W11.tmx")
        self.mapSize = (tmx_data.width, tmx_data.height)

        self.sky = pg.Surface((WINDOW_W, WINDOW_H))
        self.sky.fill((pg.Color('#5c94fc')))

        # Lista 2D
        self.map = [[0] * tmx_data.height for i in range(tmx_data.width)]

        layer_num = 0
        for layer in tmx_data.visible_layers:
            for y in range(tmx_data.height):
                for x in range(tmx_data.width):

                    # Obtendo a superfície (imagem) do pygame
                    image = tmx_data.get_tile_image(x, y, layer_num)

                    # É None quando não há bloco nessa posição
                    if image is not None:
                        tileID = tmx_data.get_tile_gid(x, y, layer_num)

                        if layer.name == 'Foreground':

                            # O ID 22 é um bloco de interrogação, então carregamos todas as imagens dele
                            if tileID == 22:
                                image = (
                                    image,                                      # 1
                                    tmx_data.get_tile_image(0, 15, layer_num),   # 2
                                    tmx_data.get_tile_image(1, 15, layer_num),   # 3
                                    tmx_data.get_tile_image(2, 15, layer_num)    # ativado
                                )

                            # A classe Map tem 1) a lista "map", usada no sistema de colisão porque
                            # permite pegar um bloco pelas coordenadas x e y; 2) "obj", "obj_bg" e listas
                            # parecidas, usadas na renderização para não precisar percorrer todos os
                            # pares (x, y). Aqui o mesmo objeto de plataforma é adicionado em 2 listas.
                            self.map[x][y] = Platform(x * tmx_data.tileheight, y * tmx_data.tilewidth, image, tileID)
                            self.obj.append(self.map[x][y])

                        elif layer.name == 'Background':
                            self.map[x][y] = BGObject(x * tmx_data.tileheight, y * tmx_data.tilewidth, image)
                            self.obj_bg.append(self.map[x][y])
            layer_num += 1

        # Canos
        self.spawn_tube(28, 10)
        self.spawn_tube(37, 9)
        self.spawn_tube(46, 8)
        self.spawn_tube(55, 8)
        self.spawn_tube(163, 10)
        self.spawn_tube(179, 10)

        # Inimigos
        self.mobs.append(Goombas(736, 352, False))
        self.mobs.append(Goombas(1295, 352, True))
        self.mobs.append(Goombas(1632, 352, False))
        self.mobs.append(Goombas(1672, 352, False))
        self.mobs.append(Goombas(5570, 352, False))
        self.mobs.append(Goombas(5620, 352, False))

        self.map[21][8].bonus = 'mushroom'
        self.map[78][8].bonus = 'mushroom'
        self.map[109][4].bonus = 'mushroom'

        self.flag = Flag(6336, 48)

    def reset(self, reset_all):
        self.obj = []
        self.obj_bg = []
        self.tubes = []
        self.debris = []
        self.mobs = []
        self.is_mob_spawned = [False, False]

        self.in_event = False
        self.flag = None
        self.sky = None
        self.map = None

        self.tick = 0
        self.time = 400

        self.mapSize = (0, 0)
        self.textures = {}
        self.loadWorld_11()

        self.get_event().reset()
        self.get_player().reset(reset_all)
        self.get_camera().reset()

    def get_name(self):
        if self.worldNum == '1-1':
            return '1-1'

    def get_player(self):
        return self.oPlayer

    def get_camera(self):
        return self.oCamera

    def get_event(self):
        return self.oEvent

    def get_ui(self):
        return self.oGameUI

    def _get_safe_map_cell(self, x, y):
        if self.map is None or not self.map:
            return 0

        width = len(self.map)
        height = len(self.map[0]) if width > 0 else 0

        if x < 0 or x >= width or y < 0 or y >= height:
            return 0

        return self.map[x][y]

    def get_blocks_for_collision(self, x, y):
        """

        Retorna os blocos ao redor da entidade

        """
        return (
            self._get_safe_map_cell(x, y - 1),
            self._get_safe_map_cell(x, y + 1),
            self._get_safe_map_cell(x, y),
            self._get_safe_map_cell(x - 1, y),
            self._get_safe_map_cell(x + 1, y),
            self._get_safe_map_cell(x + 2, y),
            self._get_safe_map_cell(x + 1, y - 1),
            self._get_safe_map_cell(x + 1, y + 1),
            self._get_safe_map_cell(x, y + 2),
            self._get_safe_map_cell(x + 1, y + 2),
            self._get_safe_map_cell(x - 1, y + 1),
            self._get_safe_map_cell(x + 2, y + 1),
            self._get_safe_map_cell(x, y + 3),
            self._get_safe_map_cell(x + 1, y + 3)
        )

    def get_blocks_below(self, x, y):
        """

        Retorna os 2 blocos abaixo da entidade para verificar o on_ground

        """
        return (
            self._get_safe_map_cell(x, y + 1),
            self._get_safe_map_cell(x + 1, y + 1)
        )

    def get_mobs(self):
        return self.mobs

    def spawn_tube(self, x_coord, y_coord):
        self.tubes.append(Tube(x_coord, y_coord))

        # A colisão do cano é feita criando blocos dentro dele.
        # Eles não são desenhados porque vão só para a lista de colisão.
        for y in range(y_coord, 12): # 12 porque é o nível do chão.
            for x in range(x_coord, x_coord + 2):
                self.map[x][y] = Platform(x * 32, y * 32, image=None, type_id=0)

    def spawn_mushroom(self, x, y):
        self.get_mobs().append(Mushroom(x, y, True))

    def spawn_goombas(self, x, y, move_direction):
        self.get_mobs().append(Goombas(x, y, move_direction))

    def spawn_koopa(self, x, y, move_direction):
        self.get_mobs().append(Koopa(x, y, move_direction))

    def spawn_flower(self, x, y):
        self.mobs.append(Flower(x, y))

    def spawn_debris(self, x, y, type):
        if type == 0:
            self.debris.append(PlatformDebris(x, y))
        elif type == 1:
            self.debris.append(CoinDebris(x, y))

    def spawn_fireball(self, x, y, move_direction):
        self.projectiles.append(Fireball(x, y, move_direction))

    def spawn_score_text(self, x, y, score=None):
        """

        Este texto aparece quando, por exemplo, você mata um inimigo. Ele mostra
        quantos pontos você ganhou.

        """

        # score é None só quando você mata um inimigo. Em uma sequência de abates,
        # os pontos por inimigo aumentam: 100, 200, 400, 800...
        # Por isso não dá para saber de antemão quantos pontos somar.
        if score is None:
            self.text_objects.append(Text(str(self.score_for_killing_mob), 16, (x, y)))

            # A próxima pontuação será maior
            self.score_time = pg.time.get_ticks()
            if self.score_for_killing_mob < 1600:
                self.score_for_killing_mob *= 2

        # Este caso vale para todas as outras situações.
        else:
            self.text_objects.append(Text(str(score), 16, (x, y)))

    def remove_object(self, object):
        self.obj.remove(object)
        self.map[object.rect.x // 32][object.rect.y // 32] = 0

    def remove_whizbang(self, whizbang):
        self.projectiles.remove(whizbang)

    def remove_text(self, text_object):
        self.text_objects.remove(text_object)

    def update_player(self, core):
        self.get_player().update(core)

    def update_entities(self, core):
        for mob in self.mobs:
            mob.update(core)
            if not self.in_event:
                self.entity_collisions(core)

    def update_time(self, core):
        """

        Atualiza o tempo do mapa.

        """

        # O tempo só corre se o mapa não estiver em um evento
        if not self.in_event:
            self.tick += 1
            if self.tick % 40 == 0:
                self.time -= 1
                self.tick = 0
            if self.time == 100 and self.tick == 1:
                core.get_sound().start_fast_music(core)
            elif self.time == 0:
                self.player_death(core)

    def update_score_time(self):
        """

        Quando o jogador mata inimigos em sequência, a pontuação de cada
        um aumenta. Quando ele para de matar inimigos, os pontos
        voltam para 100. Este método atualiza esses pontos.

        """
        if self.score_for_killing_mob != 100:

            # O intervalo é de 750 ms
            if pg.time.get_ticks() > self.score_time + 750:
                self.score_for_killing_mob //= 2

    def entity_collisions(self, core):
        if not core.get_map().get_player().unkillable:
            for mob in self.mobs:
                mob.check_collision_with_player(core)

    def try_spawn_mobs(self, core):
        """

        Estes inimigos aparecem quando o jogador alcança certa coordenada x

        """
        if self.get_player().rect.x > 2080 and not self.is_mob_spawned[0]:
            self.spawn_goombas(2495, 224, False)
            self.spawn_goombas(2560, 96, False)
            self.is_mob_spawned[0] = True

        elif self.get_player().rect.x > 2460 and not self.is_mob_spawned[1]:
            self.spawn_goombas(3200, 352, False)
            self.spawn_goombas(3250, 352, False)
            self.spawn_koopa(3400, 338, False)
            self.spawn_goombas(3700, 352, False)
            self.spawn_goombas(3750, 352, False)
            self.spawn_goombas(4060, 352, False)
            self.spawn_goombas(4110, 352, False)
            self.spawn_goombas(4190, 352, False)
            self.spawn_goombas(4240, 352, False)
            self.is_mob_spawned[1] = True

    def player_death(self, core):
        self.in_event = True
        self.get_player().reset_jump()
        self.get_player().reset_move()
        self.get_player().numOfLives -= 1

        if self.get_player().numOfLives == 0:
            self.game_over = True
            self.get_event().start_kill(core, True)
            
        else:
            pass

    def player_win(self, core):
        self.in_event = True
        self.get_player().reset_jump()
        self.get_player().reset_move()
        self.get_event().start_win(core)

    def update(self, core):

        # Todos os inimigos
        self.update_entities(core)

        if not core.get_map().in_event:

            # Quando o jogador come um cogumelo
            if self.get_player().inLevelUpAnimation:
                self.get_player().change_powerlvl_animation()

            # Ao contrário da animação de crescer, aqui o jogador pode se mover
            elif self.get_player().inLevelDownAnimation:
                self.get_player().change_powerlvl_animation()
                self.update_player(core)

            # Caso comum
            else:
                self.update_player(core)

        else:
            self.get_event().update(core)

        # Debris são 1) pedaços que aparecem quando o jogador quebra um bloco de tijolo
        # 2) moedas que aparecem quando o jogador ativa um bloco de interrogação
        for debris in self.debris:
            debris.update(core)

        # Bolas de fogo do jogador
        for whizbang in self.projectiles:
            whizbang.update(core)

        # Textos que mostram quantos pontos o jogador ganhou
        for text_object in self.text_objects:
            text_object.update(core)

        # A câmera para quando o jogador morre ou toca a bandeira
        if not self.in_event:
            self.get_camera().update(core.get_map().get_player().rect)

        self.try_spawn_mobs(core)

        self.update_time(core)
        self.update_score_time()

    def render_map(self, core):
        """

        Renderiza apenas os blocos. É usado no menu principal.

        """
        core.screen.blit(self.sky, (0, 0))

        for obj_group in (self.obj_bg, self.obj):
            for obj in obj_group:
                obj.render(core)

        for tube in self.tubes:
            tube.render(core)

    def render(self, core):
        """

       Renderiza cada objeto.
       
        """
        core.screen.blit(self.sky, (0, 0))

        for obj in self.obj_bg:
            obj.render(core)

        for mob in self.mobs:
            mob.render(core)

        for obj in self.obj:
            obj.render(core)

        for tube in self.tubes:
            tube.render(core)

        for whizbang in self.projectiles:
            whizbang.render(core)

        for debris in self.debris:
            debris.render(core)

        self.flag.render(core)

        for text_object in self.text_objects:
            text_object.render_in_game(core)

        self.get_player().render(core)

        self.get_ui().render(core)
