import json
from abc import ABC, abstractmethod

class User:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

class Formatter(ABC):

    @abstractmethod
    def format (self, data):
        pass

class TxtFormatter(Formatter):
    def format (self, data):
        result = ""
        for user in data:
            result = f"{user['name']} - {user['email']} - {user['role']}\n"
        return result
    
class HtmlFormatter(Formatter):
    def format(self, data):
        html = "<html><body><ul>"
        for user in data:
            html += f"<li>{user['name']} ({user['email']}) ({user['role']}) </li>"
        html += "</ul></body></html>"

class JsonFormatter(Formatter):
    def format(self, data):
        return json.dumps(data, indent = 2)
            
class GenerateReport:
    def __init__(self, users):
        self.users = users
    
    def generate_data(self):
        return [
            {
                "name": User.name,
                "email": User.email,
                "role": User.role
            }
            for user in self.users
        ]

class FileSaver:
    def save_to_file(self, filename, content):
        with open(filename, 'w') as f:
            f.write(content)

class EmailSender:
    def send_email(self, content):
        # Simulación de envío de correo
        print(f"Sending email with content:\n{content}")


class ReportSystem:

    def __init__(self, users, formatter, file_saver, email_sender):
        self.users = users

    def filter_admins(self):
        # Otra responsabilidad más
        return [user for user in self.users if user.role == "admin"]

    def print_report(self, content):
        print("----- REPORT -----")
        print(content)
        print("------------------")