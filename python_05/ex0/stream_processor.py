from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")

        total = 0
        count = 0
        for num in data:
            total += num
            count += 1
        average = total / count
        return (
            f"Processed {count} numeric values, "
            f"sum={total}, avg={average}"
        )

    def validate(self, data: Any) -> bool:
        if isinstance(data, list) and data:
            for value in data:
                if not isinstance(value, (int, float)):
                    return False
            return True
        return False


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")
        char_count = 0
        word_count = 0
        flag = True
        for char in data:
            char_count += 1
            if char != ' ' and flag:
                word_count += 1
                flag = False
            if char == ' ':
                flag = True
        return (
            f"Processed text: {char_count} characters, "
            f"{word_count} words"
        )

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log data")
        level = ""
        message = ""
        flag = True
        for char in data:
            if char == ':':
                flag = False
            else:
                if flag:
                    level = level + char
                else:
                    message = message + char
        return f"[{level}] {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str) and ":" in data:
            return True
        return False


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    try:
        c = '"'
        data = [1, 2, 3, 4, 5]
        print("Initializing Numeric Processor...")
        numeric = NumericProcessor()
        print("Processing data:", data)
        result = numeric.process(data)
        print("Validation: Numeric data verified")
        print(numeric.format_output(result))
        print("\nInitializing Text Processor...")
        data = "Hello Nexus World"
        text = TextProcessor()
        print(f"Processing data: {c}{data}{c}")
        result = text.process(data)
        print("Validation: Text data verified")
        print(text.format_output(result))
        print("\nInitializing Log Processor...")
        data = "ERROR: Connection timeout"
        log = LogProcessor()
        print(f"Processing data: {c}{data}{c}")
        result = log.process(data)
        print("Validation: Log entry verified")
        print(log.format_output(result))
        print("\n=== Polymorphic Processing Demo ===\n")
        print("Processing multiple data types through same interface...")
        processors = [
            NumericProcessor(),
            TextProcessor(),
            LogProcessor(),
        ]
        data_items = [
            [1, 2, 3],
            "Hello World",
            "INFO: System ready",
        ]
        i = 0
        for processor in processors:
            result = processor.process(data_items[i])
            print(f"Result {i + 1}: {result}")
            i += 1
        print(
            "\nFoundation systems online. "
            "Nexus ready for advanced streams."
        )
    except Exception as error:
        print("Error:", error)


main()
