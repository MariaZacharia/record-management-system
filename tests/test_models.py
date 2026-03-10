import pytest
from datetime import datetime
from src.models import ClientRecord, AirlineRecord, FlightRecord


def make_client(**kwargs):
    defaults = dict(id=1, name="Alice", address_line_1="1 High St",
                    address_line_2="", address_line_3="", city="London",
                    state="England", zip_code="EC1A 1BB", country="UK",
                    phone_number="07700900000")
    defaults.update(kwargs)
    return ClientRecord(**defaults)


class TestClientRecord:
    def test_type_is_auto_set(self):
        c = make_client()
        assert c.type == "client"

    def test_to_dict_contains_all_keys(self):
        d = make_client().to_dict()
        for key in ("id", "name", "type", "city", "country"):
            assert key in d

    def test_from_dict_round_trip(self):
        original = make_client()
        restored = ClientRecord.from_dict(original.to_dict())
        assert restored.name == original.name
        assert restored.type == "client"

    def test_missing_required_field_raises(self):
        with pytest.raises(TypeError):
            ClientRecord(id=1)


class TestAirlineRecord:
    def test_type_is_auto_set(self):
        a = AirlineRecord(id=10, company_name="BritAir")
        assert a.type == "airline"

    def test_round_trip(self):
        a = AirlineRecord(id=10, company_name="BritAir")
        restored = AirlineRecord.from_dict(a.to_dict())
        assert restored.company_name == "BritAir"


class TestFlightRecord:
    def _make(self):
        return FlightRecord(client_id=1, airline_id=10,
                            date=datetime(2025, 6, 15, 9, 0),
                            start_city="London", end_city="Rome")

    def test_type_is_auto_set(self):
        assert self._make().type == "flight"

    def test_date_serialised_to_string(self):
        d = self._make().to_dict()
        assert isinstance(d["date"], str)

    def test_from_dict_restores_datetime(self):
        f = self._make()
        restored = FlightRecord.from_dict(f.to_dict())
        assert isinstance(restored.date, datetime)
        assert restored.date.year == 2025
