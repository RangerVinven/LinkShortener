from fastapi.testclient import TestClient
from ..main import api

client = TestClient(api)

# The user added in the create_user tests
newUser = {
    "FirstName": "Arthur",
    "LastName": "Pendragon",
    "Email": "arthur@pendragon.co.uk",
    "Password": "KingArthur"
}

# The new details used for test_update_user
updatedUserDetails = {
    "FirstName": "Updated",
    "LastName": "User",
    "Email": "fdasfdas@fdasfdsa.fdasfdas",
    "Password": "fdafdsa"
}


# Session token asigned to the Elliot user that's inserted when the database is build built
sessionToken = "f2ca1bb6c7e907d06dafe4687e579fce76b37e4e93b7605022da52e6ccc26fd2"


def test_read_users():
    response = client.get("/users")
    assert response.status_code == 200


def test_create_user():
    newUser = {
        "FirstName": "Arthur",
        "LastName": "Pendragon",
        "Email": "arthur@pendragon.co.uk",
        "Password": "KingArthur"
    }

    response = client.post("/users", json=newUser)
    assert response.status_code == 200


# Should return 403 since this user was created in the test_create_user() test
def test_create_user_duplicate_email():
    response = client.post("/users", json=newUser)
    
    assert response.status_code == 403 # User was already created in test_create_user
    assert response.json() == {"detail": "Account with that email already exists"}


def test_update_user():
    updatedUserDetails = {
        "FirstName": "Updated",
        "LastName": "User",
        "Email": "fdasfdas@fdasfdsa.fdasfdas",
        "Password": "fdafdsa"
    }

    response = client.put("/users", json=updatedUserDetails)

    assert response.status_code == 200



def test_update_user_duplicate_email():
    updatedUserDetails = {
        "FirstName": "Updated",
        "LastName": "User",
        "Email": "mr_robot@proton.me",
        "Password": "fdafdsa"
    }

    response = client.put("/users", json=updatedUserDetails, headers={"SessionToken": sessionToken})

    assert response.status_code == 200