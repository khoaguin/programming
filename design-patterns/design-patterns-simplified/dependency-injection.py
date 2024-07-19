# Define interfaces
class ILogger:
    def log(self, message: str):
        raise NotImplementedError


class IDeliveryService:
    def deliver(self, order_id: int):
        raise NotImplementedError


class IOrdersRepository:
    def get_order(self, order_id: int):
        raise NotImplementedError


# Define implementations
class Logger(ILogger):
    def log(self, message: str):
        print(f"Log: {message}")


class DeliveryService(IDeliveryService):
    def deliver(self, order_id: int):
        print(f"Delivering order {order_id}")


class OrdersRepository(IOrdersRepository):
    def get_order(self, order_id: int):
        print(f"Getting order {order_id}")
        return {"id": order_id, "product": "Sample Product"}


class OrdersApi:
    def __init__(
        self, 
        orders_repository: IOrdersRepository, 
        delivery_service: IDeliveryService, 
        logger: ILogger
    ):
        self.orders_repository = orders_repository
        self.delivery_service = delivery_service
        self.logger = logger


if __name__ == "__main__":
    # Manual dependency injection setup
    logger = Logger()
    delivery_service = DeliveryService()
    orders_repository = OrdersRepository()

    # Create OrdersApi instance with injected dependencies
    orders_api = OrdersApi(orders_repository, delivery_service, logger)

    # Verify dependencies are injected
    orders_api.logger.log("This is a log message.")  # Log: This is a log message.
    orders_api.delivery_service.deliver(1)  # Delivering order 1
    orders_api.orders_repository.get_order(1)  # Getting order 1