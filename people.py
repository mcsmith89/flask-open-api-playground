from datetime import datetime
from flask import abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

people = {
    "Hellbender": {
        "fname": "James",
        "lname": "Hellbender",
        "timestamp": get_timestamp(),
    },
    "Fuckboi": {
        "fname": "Billy",
        "lname": "Fuckboi",
        "timestamp": get_timestamp(),
    },
    "Dover": {
        "fname": "Ben",
        "lname": "Dover",
        "timestamp": get_timestamp(),
    }

}

def read_all():
    return list(people.values())

def create(person):
    lname = person.get("lname")
    fname = person.get("fname", "")

    if lname not in people:
        people.update({
            lname:{
                "fname":lname,
                "lname":lname,
                "timestamp":get_timestamp()
            }
        })

        return people[lname], 201
    
    else:
        abort(
            406,
            f"Person with last name {lname} already exists",
        )
#Left off on Create a New Person