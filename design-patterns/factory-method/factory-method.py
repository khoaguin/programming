from __future__ import annotations

from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass


class Truck(Transport):
    def deliver(self) -> str:
        return "{Deliver by Truck}"


class Ship(Transport):
    def deliver(self) -> str:
        return "{Deliver by Ship}"


class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        """
        This is the factory method
        """
        pass

    def plan_delivery(self) -> str:
        transport = self.create_transport()
        result = f"Logistics: The same logistics' code has just worked with {transport.deliver()}"
        return result


class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()


def client_code(logistics: Logistics) -> None:
    print(
        f"Client is not aware of the code in the logistic's class, but it still works.\n"
        f"{logistics.plan_delivery()}",
        end="",
    )


if __name__ == "__main__":
    print("Client planning to devliver by road")
    client_code(RoadLogistics())
    print("\n")

    print("Client planning to devliver by ship")
    client_code(SeaLogistics())
