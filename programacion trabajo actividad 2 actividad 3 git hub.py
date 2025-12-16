   
# Programacion tarea
def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def __str__(self):
        return f"ID: {self.student_id} - Name: {self.name} - Age: {self.age}"


class StudentRegistry:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        
        for s in self.students:
            if s.student_id == student.student_id:
                print("El estudiante ya está registrado.")
                return
        self.students.append(student)
        print("Estudiante agregado exitosamente.")

    def remove_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                print("🗑️ Estudiante eliminado.")
                return
        print("Estudiante no encontrado.")

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                print("✔️ Estudiante encontrado:")
                print(s)
                return
        print(" Estudiante no encontrado.")

    def list_students(self):
        if not self.students:
            print(" No hay estudiantes registrados.")
            return
        print("\n Lista de estudiantes:")
        for s in self.students:
            print(s)


def main():
    registry = StudentRegistry()

    while True:
        print("\nStudent Registry")
        print("1. Add student")
        print("2. Remove student")
        print("3. Find student")
        print("4. List students")
        print("5. Exit")

        option = input("Seleccione una opción: ")

        if option == "1":
            student_id = input("Ingrese ID del estudiante: ")
            name = input("Ingrese nombre: ")
            age = input("Ingrese edad: ")
            student = Student(student_id, name, age)
            registry.add_student(student)

        elif option == "2":
            student_id = input("Ingrese ID del estudiante a eliminar: ")
            registry.remove_student(student_id)

        elif option == "3":
            student_id = input("Ingrese ID del estudiante a buscar: ")
            registry.find_student(student_id)

        elif option == "4":
            registry.list_students()

        elif option == "5":
            print("Saliendo del sistema...")
            break

        else:
            print(" Opción inválida. Intente nuevamente.")



if __name__ == "__main__":
    main()
