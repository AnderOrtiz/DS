class ImageNode:
    def __init__(self, file):
        self.file = file
        self.next = None
        self.previous = None

class InfiniteCarousel:
    def __init__(self):
        self.head = None
        self.current = None

    def add_image(self, file):
        new_node = ImageNode(file)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.previous = new_node
            self.current = new_node
        else:
            tail = self.head.previous
            tail.next = new_node
            new_node.previous = tail
            new_node.next = self.head
            self.head.previous = new_node

    def view_current(self):
        if self.current:
            print(f"Mostrando en pantalla: [{self.current.file}]")

    def forward(self):
        if self.current:
            print(">> Siguiente imagen...")
            self.current = self.current.next
            self.view_current()

    def backward(self):
        if self.current:
            print("<< Imagen anterior...")
            self.current = self.current.previous
            self.view_current()


gallery = InfiniteCarousel()
gallery.add_image("infomercial.jpg")
gallery.add_image("diagrama.png")
gallery.add_image("pet.jpeg")
gallery.add_image("captura_pantalla.png")

print("--- Estado Inicial ---")
gallery.view_current()

print("\n--- Avanzando ---")
gallery.forward()
gallery.forward()
gallery.forward()
gallery.forward()

print("\n--- Retrocediendo ---")
gallery.backward()