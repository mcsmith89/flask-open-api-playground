from datetime import datetime

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