from flask_app.config.mysqlconnection import connectToMySQL
import random

class Attacks:
    def __init__(self, mana = 100, stamina = 100):
        self.mana = mana
        self.stamina = stamina
        self.hp_bar = 100
    def attack(self, opponent):
        damage = 10
        print(f"{Sheet.name} Attacked {opponent.Sheet.name} and delt {damage} damage!!!")
        opponent.hp_bar += damage

        chance = random.randint(0 , 9)
        if chance == 0:
            print(f"Critical Hit! {Sheet.name} Attacked {opponent.Sheet.name} and delt {damage} more damage!!!!")
            opponent.hp_bar += 5

class Image:
    def __int__(self,data):
        self.id = data["id"]
        self.img_name = data["img_name"]
        self.img_data = data["img_data"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

class Sheet:
    def __init__(self, data):
        self.id = data["id"]
        self.character_dis = data["character_dis"]
        self.height = data["height"]
        self.weight = data["weight"]
        self.name = data["name"]
        self.race = data["race"]
        self.job = data["job"]
        self.gender = data["gender"]
        self.character_bio = data["character_bio"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["users_id"]
        self.strength = data["strength"]
        self.constatution = data["constatution"]
        self.wisdom = data["wisdom"]
        self.dexterity = data["dexterity"]
        self.intelegence = data["intelegence"]
        self.charisma = data["charisma"]
        self.img_data = data["img_data"]
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO charinfo.character (character_dis, name, race, gender, job, character_bio , created_at, updated_at, users_id, strength, constatution, dexterity, wisdom, intelegence, charisma, img_data) VALUES ( %(character_dis)s, %(name)s , %(race)s, %(gender)s , %(job)s, %(character_bio)s , NOW() , NOW(), %(users_id)s, %(strength)s, %(constatution)s, %(dexterity)s, %(wisdom)s, %(intelegence)s, %(charisma)s, %(img_data)s);"
        return connectToMySQL('charinfo').query_db( query, data )

    @classmethod
    def edit(cls, data):
        query = "UPDATE charinfo.character SET character_dis = %(character_dis)s, name = %(name)s, race = %(race)s, gender = %(gender)s, job = %(job)s, character_bio = %(character_bio)s, strength = %(strength)s, constatution = %(constatution)s, dexterity = %(dexterity)s, wisdom = %(wisdom)s, intelegence = %(intelegence)s, charisma = %(charisma)s, img_data = %(img_data)s  WHERE id = %(id)s;"
        character_id = connectToMySQL("charinfo").query_db(query,data)
        return character_id

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM charinfo.character WHERE id = %(id)s"
        exsponge = connectToMySQL("charinfo").query_db(query,data)

        return exsponge

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM charinfo.character JOIN charinfo.users ON charinfo.character.users_id = charinfo.users.id WHERE charinfo.character.id = %(id)s;"
        results = connectToMySQL("charinfo").query_db(query,data)
        one_instance = cls(results[0])
        return one_instance

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM charinfo.character;"
        results = connectToMySQL("charinfo").query_db(query)

        character = []
        for result in results:
            one_instance = cls(result)
            character.append(one_instance)
        return character


