from Code.Enemy import Enemy
from Code.Entity import Entity


# Verifica as colisões
class EntityMediator:
    @staticmethod
    def __verify_colision_window(ent: Entity):  # método privado usando o __
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
            pass



    @staticmethod
    def verify_colision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_colision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)



