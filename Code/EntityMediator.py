from Code.Const import WIN_WIDTH
from Code.Enemy import Enemy
from Code.EnemyShot import EnemyShot
from Code.Entity import Entity
from Code.Player import Player
from Code.PlayerShot import PlayerShot


# Verifica as colisões
class EntityMediator:
    @staticmethod
    def __verify_colision_window(ent: Entity):  # método privado usando o __
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
            if isinstance(ent, EnemyShot):
                if ent.rect.right <= 0:
                    ent.health = 0

    @staticmethod
    def __verify_colision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:  # é o mesmo que colocar valid_interaction == True:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent1.health -= ent2.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @staticmethod
    def verify_colision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_colision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_colision_entity(entity2, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
