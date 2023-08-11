from datetime import datetime
from flask import abort, make_response

def get_timestamp () :
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
    "Fairy": {
        "fname": "Tooth",
        "lname": "Fairy",
        "timestamp": get_timestamp(),
    },
    "Ruprecht": {
        "fname": "Knecht",
        "lname": "Ruprecht",
        "timestamp": get_timestamp(),
    },
    "Bunny": {
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": get_timestamp(),
    }
}

def read_all () :
    return list(PEOPLE.values())

def add_person (person) :
    lname = person.get("lname")
    fname = person.get("fname")
    if lname and lname not in PEOPLE:
        PEOPLE[lname] = {
            "lname":lname,
            "fname":fname,
            "timestamp": get_timestamp()
        }
        return PEOPLE[lname], 201
    else:
        abort(406,f"Person with last name {lname} already exists")

def get_a_person(lname) :
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(404,f"Person with last name {lname} not found")

def update_a_person(lname,person):
    if lname in PEOPLE:
        PEOPLE[lname]['fname'] = person.get('fname',PEOPLE[lname]['fname'])
        PEOPLE[lname]['timestamp'] = get_timestamp()
        return PEOPLE[lname]
    else:
        # pass
        abort(404,f"Person with last name {lname} not found")

def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(f"Deleted Successfully",204)
    else:
        abort(404,f"No person with last name {lname} was found")