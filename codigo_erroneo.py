import json

class User:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role
            
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

class ReportSystem:

    def __init__(self, users):
        self.users = users


    def save_to_file(self, filename, content):
        # Manejo directo de archivo (acoplamiento fuerte)
        with open(filename, 'w') as f:
            f.write(content)

    def send_email(self, content):
        # Simulación de envío de correo (responsabilidad extra)
        print(f"Sending email with content:\n{content}")

    def filter_admins(self):
        # Otra responsabilidad más
        return [user for user in self.users if user.role == "admin"]

    def print_report(self, content):
        print("----- REPORT -----")
        print(content)
        print("------------------")