from flask_app.config.mysqlconnection import connectToMySQL

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
        self.users_id = data["users_id"]
        self.strength = data["strength"]
        self.constatution = data["constatution"]
        self.wisdom = data["wisdom"]
        self.dexterity = data["dexterity"]
        self.intelegence = data["intelegence"]
        self.charisma = data["charisma"]
        self.img_data = data["img_data"]
    
    @classmethod
    def save(cls, data ):
        # query = "INSERT INTO charinfo.character (character_dis, height, weight, name, race, job, gender, character_bio , created_at, updated_at, users_id, strength, constatution, dexterity, wisdom, intelegence, charisma, img_data) VALUES ( %(character_dis)s, %(height)s, %(weight)s, %(name)s , %(race)s, %(job)s,%(gender)s , %(character_bio)s , NOW() , NOW(), %(users_id)s, %(strength)s, %(constatution)s, %(dexterity)s, %(wisdom)s, %(intelegence)s, %(charisma)s, %(img_data)s);"
        query = "INSERT INTO charinfo.character (character_dis, height, weight, name, race, job, gender, character_bio , created_at, updated_at, users_id, strength, constatution, dexterity, wisdom, intelegence, charisma, img_data) VALUES ( %(character_dis)s, %(height)s, %(weight)s, %(name)s , %(race)s, %(job)s,%(gender)s , %(character_bio)s , NOW() , NOW(), %(users_id)s, %(strength)s, %(constatution)s, %(dexterity)s, %(wisdom)s, %(intelegence)s, %(charisma)s, %(img_data)s);"
        new_id = connectToMySQL('charinfo').query_db( query, data )
        return new_id

    @classmethod
    def edit(cls, data):
        query = "UPDATE character SET character_dis = %(character_dis)s,height = %(height)s, weight = %(weight)s, name = %(name)s, race = %(race)s, gender = %(gender)s, job = %(job)s, character_bio = %(character_bio)s, strength = %(strength)s, constatution = %(constatution)s, dexterity = %(dexterity)s, wisdom = %(wisdom)s, intelegence = %(intelegence)s, charisma = %(charisma)s, img_data = %(img_data)s,users_id = %(users_id)s WHERE id = %(id)s;"
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
        query = "SELECT * FROM charinfo.character JOIN users ON character.users_id WHERE users_id = users.id;"
        results = connectToMySQL("charinfo").query_db(query)

        # character = []
        for result in results:
            one_instance = cls(result)
            # character.append(one_instance)
        return results


