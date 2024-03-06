# Basically high level modules should not be depended on low level modules directly but through
# an interface or abstract class

from abc import ABC, abstractmethod

class Logger(ABC):

    @abstractmethod
    def log(self, message: str):
        pass

class ConsoleLogger(Logger):

    def log(self, message: str):
        print("log to console", message)

class FileLogger(Logger):

    def log(self, message: str):
        with open("log.txt", "a") as f:
            f.write("log to file "+ message + "\n")

class OrderProcessor:

    def __init__(self, logger: Logger) -> None:
        self.logger = logger
    
    def process_order(self, food):
        # order processing
        self.logger.log(f"order processed: {food}")
    
console_logger = ConsoleLogger()
file_logger = FileLogger()

order1 = OrderProcessor(console_logger)

order2 = OrderProcessor(file_logger)

order1.process_order("burger")

order2.process_order("ham")



# example from bing AI if the above code did not follow DIP
class ConsoleLogger:
    def log(self, message: str):
        print(f"Log to console: {message}")

class FileLogger:
    def log(self, message: str):
        with open("log.txt", "a") as file:
            file.write(f"Log to file: {message}\n")

class OrderProcessor:
    def __init__(self, logger: ConsoleLogger):
        self.logger = logger

    def process_order(self, order):
        # Process the order
        self.logger.log(f"Order processed: {order}")

console_logger = ConsoleLogger()

order_processor = OrderProcessor(console_logger)
order_processor.process_order("Order 1")

# to log order to file, i'd have to create another class for order processing or rewrite the 
# OrderProcessor class

import this