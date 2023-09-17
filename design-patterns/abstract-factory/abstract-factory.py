from __future__ import annotations

from abc import ABC, abstractmethod


class GUIFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WinFactory(GUIFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()


class MacFactory(GUIFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


class Button(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def clicked(self) -> str:
        pass


"""
Concrete Products are created by corresponding Concrete Factories.
"""


class MacButton(Button):
    def clicked(self) -> str:
        return "You clicked on a Mac button!"


class WinButton(Button):
    def clicked(self) -> str:
        return "You clicked on a Windows button!"


class Checkbox(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """

    @abstractmethod
    def clicked(self) -> None:
        """
        Product B is able to do its own thing...
        """
        pass

    @abstractmethod
    def collaborate_with_button(self, collaborator: Button) -> None:
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass


class MacCheckbox(Checkbox):
    def clicked(self) -> str:
        return "You clicked on a Mac checkbox!"

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

    def collaborate_with_button(self, collaborator: Button) -> str:
        result = collaborator.clicked()
        return f"Mac checkbox: {result}"


class WinCheckbox(Checkbox):
    def clicked(self) -> str:
        return "You clicked on a Windows checkbox!"

    def collaborate_with_button(self, collaborator: Button):
        """
        The variant, Product B2, is only able to work correctly with the
        variant, Product A2. Nevertheless, it accepts any instance of
        AbstractProductA as an argument.
        """
        result = collaborator.clicked()
        return f"Windows checkbox: {result}"


def client_code(factory: GUIFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    button: Button = factory.create_button()
    checkbox: Checkbox = factory.create_checkbox()

    print(f"{button.clicked()}")
    print(f"{checkbox.clicked()}")
    print(f"{checkbox.collaborate_with_button(button)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type (WinFactory):")
    client_code(WinFactory())

    print("\n")

    print(
        "Client: Testing the same client code with the second factory type (MacFactory):"
    )
    client_code(MacFactory())
