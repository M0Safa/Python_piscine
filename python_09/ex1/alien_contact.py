from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class Alien_Contact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count: int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_business_rules(self) -> 'Alien_Contact':
        is_A = self.contact_id[0] == 'A'
        is_C = self.contact_id[1] == 'C'
        if not (is_A and is_C):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        is_telepathic = self.contact_type == ContactType.TELEPATHIC
        if is_telepathic and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
                )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        report = Alien_Contact(
            contact_id="AC_2026_X1",
            timestamp="2026-02-11T20:00:00",
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        print("Valid contact report:")
        print(f"ID: {report.contact_id}")
        print(f"Type: {report.contact_type.value}")
        print(f"Location: {report.location}")
        print(f"Signal: {report.signal_strength}/10")
        print(f"Duration: {report.duration_minutes} minutes")
        print(f"Witnesses: {report.witness_count}")
        print(f"Message: '{report.message_received}'")
    except ValidationError as e:
        print(f"Unexpected Error: {e}")

    print("======================================")
    print("Expected validation error:")
    try:
        Alien_Contact(
            contact_id="AC_BAD_01",
            timestamp=datetime.now(),
            location="Unknown",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=1,
            is_verified=True
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
