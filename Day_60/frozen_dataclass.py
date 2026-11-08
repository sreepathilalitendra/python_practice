# Day 60: Frozen Dataclass

from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    name: str
    price: float


product1 = Product("Keyboard", 1500.0)

print(product1)

# This would raise FrozenInstanceError:
# product1.price = 2000.0