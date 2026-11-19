class ProcessNode:
    def __init__(self, name):
        self.name = name
        self.next = None

class OSScheduler:
    def __init__(self):
        self.head = None

    def add_process(self, name):
        new_process = ProcessNode(name)
        if not self.head:
            self.head = new_process
            new_process.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            
            current.next = new_process
            new_process.next = self.head

    def simulate_execution(self, total_rounds):
        if not self.head:
            print("No hay procesos en el planificador.")
            return

        current = self.head
        completed_rounds = 0

        print(f"--- Iniciando planificador ({total_rounds} vueltas) ---")
        while completed_rounds < total_rounds:
            print(f"Ejecutando: {current.name}")
            current = current.next

            if current == self.head:
                completed_rounds += 1
                print(f"--> Ciclo {completed_rounds} completado\n")


scheduler = OSScheduler()
scheduler.add_process("Terminal")
scheduler.add_process("Gestor de Archivos")
scheduler.add_process("Cliente de Correo")
scheduler.add_process("Antivirus")


scheduler.simulate_execution(3)