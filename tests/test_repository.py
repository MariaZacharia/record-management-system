import pytest
from src.repository import RecordRepository
from src.exceptions import DuplicateRecordError, RecordNotFoundError


@pytest.fixture
def repo():
    return RecordRepository()


@pytest.fixture
def client_record():
    return {"type": "client", "id": 1, "name": "Alice", "city": "London"}


def test_add_and_search(repo, client_record):
    repo.add(client_record)
    results = repo.search(type="client", id=1)
    assert len(results) == 1
    assert results[0]["name"] == "Alice"


def test_add_duplicate_raises(repo, client_record):
    repo.add(client_record)
    with pytest.raises(DuplicateRecordError):
        repo.add(client_record)


def test_delete_record(repo, client_record):
    repo.add(client_record)
    repo.delete(1, "client")
    assert repo.search(type="client", id=1) == []


def test_delete_nonexistent_raises(repo):
    with pytest.raises(RecordNotFoundError):
        repo.delete(999, "client")


def test_update_record(repo, client_record):
    repo.add(client_record)
    repo.update(1, "client", {"city": "Manchester"})
    assert repo.search(id=1)[0]["city"] == "Manchester"


def test_update_nonexistent_raises(repo):
    with pytest.raises(RecordNotFoundError):
        repo.update(999, "client", {"name": "Bob"})


def test_search_by_arbitrary_field(repo):
    repo.add({"type": "client", "id": 1, "city": "London"})
    repo.add({"type": "client", "id": 2, "city": "Rome"})
    assert len(repo.search(city="London")) == 1


def test_get_all(repo, client_record):
    repo.add(client_record)
    all_records = repo.get_all()
    assert len(all_records) == 1
