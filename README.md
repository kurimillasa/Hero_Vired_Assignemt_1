# Password Manager API (Hero_Vired_Assignemt_1)

This project is a small Flask API for storing usernames and passwords in memory.
Users can add a username and password with a POST request.
They can retrieve a saved password later by providing the username.
The app also includes simple voting and health-check routes for demonstration.

## Installation and Setup Steps
1. Install Python 3.8 or newer.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment:
   ```text
   python -m venv venv
   venv\Scripts\activate
   ```
4. Install the required package:
   ```text
   pip install -r requirements.txt
   ```
5. Start the Flask application:
   ```text
   python app.py
   ```

6. The API will be available at `http://127.0.0.1:5000`.

Data is stored only in memory, so all saved passwords are lost when the app stops.

## API Endpoint Reference

| Endpoint               | Method | What it does                                              | Example response                                        |
| ---------------------- | ------ | --------------------------------------------------------- | ------------------------------------------------------- |
| `/`                    | GET    | Returns a welcome message.                                | `Welcome to the Home Page!`                             |
| `/health`              | GET    | Confirms that the application is running.                 | `Application is running`                                |
| `/add`                 | POST   | Saves a username and password from a JSON request body.   | `{"message":"User Santhosh added successfully"}`           |
| `/get/<username>`      | GET    | Returns the saved password for a username.                | `{"password":"password1","username":"Santhosh"}`              |
| `/get/<username>`      | GET    | Returns an error when the username does not exist.        | `{"error":"User unknown not found"}` with status `404`  |
| `/vote/<name>`         | GET    | Adds one vote for the specified name.                     | `Vote received for Santhosh! Total votes: 1`                |
| `/session_vote/<name>` | GET    | Adds one vote for the specified name in the user session. | `Session vote received for Santhosh! Your session votes: 1` |
| `/results`             | GET    | Returns all in-memory vote totals.                        | `{"Santhosh":1}`                                            |

### Adding a password

Send a POST request to `/add` with a JSON body:

```json
{
  "username": "Santhosh",
  "password": "password1"
}
```

Successful response: `201 Created`

```json
{
  "message": "User Santhosh added successfully"
}
```

### Retrieving a password

Send a GET request to `/get/Santhosh`.

Successful response: `200 OK`

```json
{
  "username": "Santhosh",
  "password": "password-1"
}
```

An unknown username returns `404 Not Found`.

The `/session_vote/<name>` route uses Flask sessions and requires a Flask
`SECRET_KEY` to be configured before it can persist session data.

## Git Workflow

Development work is done on the `dev` branch. Completed changes are reviewed and
then merged into the `main` branch. The basic workflow is:

```text
main  <--- merge completed work from dev
					^
					|
				dev  <--- create and test changes here
```

Typical commands:
```text
git checkout dev
git add .
git commit -m "Final working code - with add and get methods"
git push origin dev
```

After review, merge the `dev` branch into `main`.

## Version History

| Version   | Changes                                                                                                                      |
| --------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Version 1 | Added the Flask application, health-check route, voting routes, and in-memory vote storage.                                  |
| Version 2 | Added the in-memory password manager with `POST /add`, `GET /get/<username>`, JSON validation, and not-found error handling. |

## Screenshots 

Welcome Page:

<img width="457" height="202" alt="image" src="https://github.com/user-attachments/assets/42e720fd-54d1-4d88-af01-aa102670b284" />

App Health:

<img width="557" height="400" alt="image" src="https://github.com/user-attachments/assets/65925705-283a-498d-9894-f757bd45ad85" />

Votes received:

<img width="651" height="286" alt="image" src="https://github.com/user-attachments/assets/65977368-8e0e-4876-bcd1-21253831175a" />

Votes Count Added:

<img width="557" height="311" alt="image" src="https://github.com/user-attachments/assets/2b49c1f9-14b7-400b-a4b0-0ceb51f6bac5" />

Vote Results:

<img width="537" height="315" alt="image" src="https://github.com/user-attachments/assets/01e59fa6-2650-49bd-ba5a-30af380fe605" />

/add to add user Santhosh and RamyaSree:

<img width="358" height="254" alt="image" src="https://github.com/user-attachments/assets/72268aca-aea7-4d45-a33b-6593b8c6dc42" />

<img width="855" height="612" alt="image" src="https://github.com/user-attachments/assets/eabfaf40-0ec4-45b7-9973-42a96a34cf77" />

/get/<username> to retrieve user details along with the password:

<img width="358" height="254" alt="image" src="https://github.com/user-attachments/assets/b8c96aba-b617-4a85-808d-e853e5229e81" />

Git Commit - Final version:

<img width="715" height="555" alt="image" src="https://github.com/user-attachments/assets/1e4fd6ba-cfb8-4def-bb6e-2923fc442f07" />



