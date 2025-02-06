import dataclasses


@dataclasses.dataclass
class Product:
    id: str
    name: str
    quantity: str


smartphone = Product(
    id="43",
    name="Smartphone",
    quantity="1")

notebook = Product(
    id="31",
    name="14.1-inch Laptop",
    quantity="1")