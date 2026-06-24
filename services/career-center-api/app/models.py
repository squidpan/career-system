from typing import Dict, List, Optional

from pydantic import BaseModel


class RecentApplication(BaseModel):
    application_id: str
    company: str
    role: str
    status: str
    last_update: Optional[str] = None
    role_code: Optional[str] = None


class DashboardSummary(BaseModel):
    application_count: int
    counts_by_status: Dict[str, int]
    counts_by_role_code: Dict[str, int]
    recent_applications: List[RecentApplication]


class DashboardStatusCounts(BaseModel):
    counts_by_status: Dict[str, int]


class DashboardRoleCounts(BaseModel):
    counts_by_role_code: Dict[str, int]


class DashboardRecentApplications(BaseModel):
    recent_applications: List[RecentApplication]
