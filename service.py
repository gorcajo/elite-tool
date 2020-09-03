from typing import List

from injector import inject

from repository import DataBase


class RepairmentsService():

    @inject
    def __init__(self, db: DataBase):
        self.db = db


    def create_new_repairment(self, repairment: dict) -> dict:
        id = self.db.insert(repairment)
        print(id)
        repairment["id"] = id
        return repairment


    def get_repairments(self, filters: List) -> List[dict]:
        all_repairments = self.db.find_all()

        if len(filters) > 0:
            repairments = []

            for key in filters.keys():
                value = filters[key]

                for repairment in all_repairments:
                    if str(repairment[key]).strip().lower() == value.strip().lower():
                        repairments.append(repairment)

            return repairments
        
        else:
            return all_repairments


    def get_repairment(self, id: int) -> dict:
        repairment = self.db.find_by_id(id)

        if repairment is not None:
            return repairment
        else:
            return None


    def modify_repairment(self, id: int, repairment: dict):
        self.db.update(id, repairment)


    def delete_repairment(self, id: int):
        self.db.delete(id)
