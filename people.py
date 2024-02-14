from datetime import datetime
from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


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


def read_all():
    return list(PEOPLE.values())


def create(person):
    lname = person.get("lname")
    fname = person.get("fname", "")

    if lname and lname not in PEOPLE:
        PEOPLE[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return PEOPLE[lname], 201
    else:
        abort(401,
              "Person with last name {} already exists".format(lname))


def read_one(lname):
    if lname in PEOPLE:
        return PEOPLE[lname]
    else:
        abort(404, "Person with last name {} not found").format(lname)


def update(lname, person):
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname", PEOPLE[lname]["fname"])
        PEOPLE[lname]["lname"] = person.get("lname", PEOPLE[lname]["lname"])
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(404, "Person with last name {} not found".format(lname))


def delete(lname):
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            "{} successfully deleted".format(lname), 200
        )
    else:
        abort(
            404,
            "Person with last name {} not found".format(lname)
        )
