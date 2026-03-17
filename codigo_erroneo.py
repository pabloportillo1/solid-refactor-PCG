import json

class User:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role


class ReportSystem:

    def __init__(self, users):
        self.users = users

    def generate_report(self, format_type):
        report_data = ""

        # Lógica de negocio + formato mezclado
        for user in self.users:
            report_data += f"{user.name} - {user.email} - {user.role}\n"

        # Manejo de múltiples formatos (OCP violado)
        if format_type == "txt":
            return report_data

        elif format_type == "json":
            data = []
            for user in self.users:
                data.append({
                    "name": user.name,
                    "email": user.email,
                    "role": user.role
                })
            return json.dumps(data)

        elif format_type == "html":
            html = "<html><body><ul>"
            for user in self.users:
                html += f"<li>{user.name} ({user.email}) - {user.role}</li>"
            html += "</ul></body></html>"
            return html

        else:
            raise Exception("Formato no soportado")

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