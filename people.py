from datetime import datetime
from flask import abort, make_response

def get_timestamp () :
    """
    Returns current time when the function called in the specified format
    %Y year, %m month, %d date, %H hours, %M minutes, %S second
    """
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
    """
    Route function
    Reads all the values from the dictionary of the peoples and return them
    in form of list
    """
    return list(PEOPLE.values())

def add_person (person) :
    """
    Route function
    Adds the person data in PEOPLE data in list
    Returns the creating person data
    """
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
    """
    Route Function
    Get the person from PEOPLE list from last name param
    and Returns it
    """
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(404,f"Person with last name {lname} not found")

def update_a_person(lname,person):
    """
    Route Function
    Updates the data of a person from unique key last name and 
    Returns the update data of the person
    """
    if lname in PEOPLE:
        PEOPLE[lname]['fname'] = person.get('fname',PEOPLE[lname]['fname'])
        PEOPLE[lname]['timestamp'] = get_timestamp()
        return PEOPLE[lname]
    else:
        # pass
        abort(404,f"Person with last name {lname} not found")

def delete(lname):
    """
    Route Function
    Deletes the data of person from PEOPLE list and 
    Returns "Deleted Successfully"
    """
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(f"Deleted Successfully",204)
    else:
        abort(404,f"No person with last name {lname} was found")