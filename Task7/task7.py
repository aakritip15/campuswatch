from enum import Enum
from dataclasses import dataclass, asdict
from datetime import datetime
import json

class SeverityLevel(Enum):
    """Severity level of an alert"""
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

class ThreatType(Enum):
    """Types of security threats that can be detected"""
    UNAUTHORIZED_ACCESS = "unauthorized_access"
    WEAPON_DETECTED = "weapon_detected"
    SUSPICIOUS_BEHAVIOR = "suspicious_behavior"
    UNATTENDED_PACKAGE = "unattended_package"
    PERSON_DOWN = "person_down"
    LOITERING = "loitering"
    CROWD_GATHERING = "crowd_gathering"
    VANDALISM = "vandalism"
    THEFT = "theft"
    TRESPASSING = "trespassing"
 
class LocationRisk(Enum):
    """Risk level of a location (affects severity)"""
    CRITICAL = "critical"           # Server rooms, labs, admin buildings
    HIGH = "high"                   # Main entrances, parking lots
    MEDIUM = "medium"               # Classrooms, libraries, cafeterias
    LOW = "low"                     # Open courtyards, recreational areas


@dataclass
class AlertContext:
    """Context information for alert severity calculation"""
    threat_type: ThreatType
    location_risk: LocationRisk
    confidence_score: float  # 0.0 to 1.0
    person_count: int
    duration_seconds: int
    camera_id: str
    location_name: str


def calculate_severity(context: AlertContext) -> SeverityLevel:
    """
    Assigns a severity level based on threat type, confidence score and location risk
    """
    severity = SeverityLevel.LOW  # Default

    # Setting severity based on threat type
    if context.threat_type in [ThreatType.WEAPON_DETECTED, ThreatType.PERSON_DOWN]:
        severity = SeverityLevel.CRITICAL
    elif context.threat_type in [ThreatType.UNAUTHORIZED_ACCESS, ThreatType.THEFT, ThreatType.TRESPASSING]:
        severity = SeverityLevel.HIGH
    elif context.threat_type in [ThreatType.SUSPICIOUS_BEHAVIOR, ThreatType.UNATTENDED_PACKAGE, ThreatType.VANDALISM]:
        severity = SeverityLevel.MEDIUM
    else:
        severity = SeverityLevel.LOW

    # Adjusting for location risk
    if context.location_risk == LocationRisk.CRITICAL and severity != SeverityLevel.LOW:
        severity = SeverityLevel.CRITICAL
    elif context.location_risk == LocationRisk.HIGH and severity == SeverityLevel.MEDIUM:
        severity = SeverityLevel.HIGH

    # Adjusting for model confidence
    if context.confidence_score < 0.3:
        severity = SeverityLevel.LOW


    return severity


def generate_alert_json(context: AlertContext):
    """Generate a JSON representation of the alert with severity included"""
    severity = calculate_severity(context)

    alert_data = {
        "alert_id": "CW-20250921-1000",
        "timestamp": datetime.now().isoformat(),
        "severity": severity.value,
        "threat_type": context.threat_type.value,
        "location": context.location_name,
        "confidence_score": round(context.confidence_score, 2),
        "camera_id": context.camera_id,
        "person_count": context.person_count,
        "duration_seconds": context.duration_seconds
    }
    return alert_data

if __name__ == "__main__":
    sample_context = AlertContext(
        threat_type=ThreatType.WEAPON_DETECTED,
        location_risk=LocationRisk.CRITICAL,
        confidence_score=0.95,
        person_count=2,
        duration_seconds=30,
        camera_id="CAM-01",
        location_name="Admin Building Entrance"
    )

    alert_json = generate_alert_json(sample_context)

    # Save to file
    with open('generated_alerts.json', 'w') as f:
        json.dump(alert_json, f, indent=2)
    print(json.dumps(alert_json, indent=4))
