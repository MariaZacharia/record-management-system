import os
import jsonlines


def load_records(filepath: str) -> list[dict]:
    """Load records from a JSONL file. Returns an empty list if the file does not exist."""
    if not os.path.exists(filepath):
        return []
    with jsonlines.open(filepath, mode="r") as reader:
        return list(reader)


def save_records(records: list[dict], filepath: str) -> None:
    """Persist records to a JSONL file, overwriting any existing content."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with jsonlines.open(filepath, mode="w") as writer:
        writer.write_all(records)
