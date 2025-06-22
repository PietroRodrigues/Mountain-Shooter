


from Class.Entity import Entity


class EntityFactory:

    def get_entity(self, entity_type:str) -> Entity:
        return Entity()