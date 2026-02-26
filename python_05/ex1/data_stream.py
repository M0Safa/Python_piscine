from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


def ft_split(string: str) -> tuple[str, str]:
    is_value = False
    value = ""
    type = ""
    for char in string:
        if char == ':':
            is_value = True
        else:
            if is_value:
                value += char
            else:
                type += char
    return type, value


def ft_len(data: List[Any]) -> int:
    count = 0
    for item in data:
        count += 1
    return count


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
        }


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        valid_data = self.filter_data(data_batch)
        count = 0
        avg = 0
        for data in valid_data:
            count += 1
            type, value = ft_split(data)
            if type == "temp":
                avg = float(value)
        return (
            f"Sensor analysis: {count} readings processed"
            f", avg temp: {avg}°C"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            return [d for d in data_batch if "alert" in d]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Environmental Data"
        return stats


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        valid_data = self.filter_data(data_batch)
        count = 0
        net_flow = 0
        for item in valid_data:
            action, value = ft_split(item)
            value = int(value)
            if action == "buy":
                net_flow -= value
            else:
                net_flow += value
            count += 1
        sign = ""
        if net_flow > 0:
            sign += '+'
        return (
            f"Transaction analysis: {count} operations, "
            f"net flow: {sign}{net_flow}"
        )

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "large":
            return [
                d for d in data_batch
                if int(ft_split(d)[1]) >= 100
            ]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Financial Data"
        return stats


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        valid_data = self.filter_data(data_batch)
        count = 0
        error_count = 0
        for event in valid_data:
            count += 1
            if event == "error":
                error_count += 1
        return (
            f"Event analysis: {count} "
            f"events, {error_count} error detected"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "System Events"
        return stats


class StreamProcessor:
    def __init__(self):
        self.sensor = 0
        self.transaction = 0
        self.event = 0
        self.critical = 0
        self.large = 0

    def process(
        self,
        stream: DataStream,
        data: List[Any],
        criteria: Optional[str] = None
    ) -> str:
        try:
            filtered = stream.filter_data(data, criteria)
            if isinstance(stream, SensorStream):
                self.sensor += ft_len(data)
                self.critical += ft_len(stream.filter_data(data, "critical"))
            elif isinstance(stream, TransactionStream):
                self.transaction += ft_len(data)
                self.large += ft_len(stream.filter_data(data, "large"))
            else:
                self.event += ft_len(data)
            return stream.process_batch(filtered)
        except Exception as e:
            return f"Stream error: {e}"

    def display(
        self,
        stream: DataStream,
    ) -> None:
        stats = stream.get_stats()
        print(f"Stream ID: {stats['stream_id']}, Type: {stats['type']}")

    def display_info(self, num_batch: int, filtering: bool) -> None:
        print(f"Batch {num_batch} Results:")
        print(f"- Sensor data: {self.sensor} readings processed")
        print(f"- Transaction data: {self.transaction} operations processed")
        print(f"- Event data: {self.event} events processed")
        if filtering:
            print("\nStream filtering active: High-priority data only")
            print(f"Filtered results: {self.critical} critical sensor alerts,",
                  f"{self.large} large transaction")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    sensor = SensorStream("SENSOR_001")
    transaction = TransactionStream("TRANS_001")
    event = EventStream("EVENT_001")
    processor = StreamProcessor()
    data = [
        ["temp:22.5", "humidity:65", "alert:1013"],
        ["buy:100", "sell:150", "buy:25"],
        ["login", "error", "logout"]
    ]
    print("\nInitializing Sensor Stream...")
    processor.display(sensor)
    print(f"Processing sensor batch: {data[0]}")
    print(processor.process(
        sensor,
        data[0]
    ))
    print("\nInitializing Transaction Stream...")
    processor.display(transaction)
    print(f"Processing transaction batch: {data[1]}")
    print(processor.process(
        transaction,
        data[1]
    ))
    print("\nInitializing Event Stream...")
    processor.display(event)
    print(f"Processing event batch: {data[2]}")
    print(processor.process(
        event,
        data[2]
    ))
    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    processor.display_info(1, True)
    print("\nAll streams processed successfully. Nexus throughput optimal.")


main()
