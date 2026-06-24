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


class ApplicationSummary(BaseModel):
    application_id: str
    company: str
    role: str
    status: str
    last_update: Optional[str] = None
    role_code: Optional[str] = None


class ApplicationDetail(BaseModel):
    application_id: str
    company: str
    role: str
    role_id: Optional[str] = None
    role_code: Optional[str] = None
    role_family: Optional[str] = None
    status: str
    date_applied: Optional[str] = None
    last_update: Optional[str] = None
    source: Optional[str] = None
    location: Optional[str] = None
    employment_type: Optional[str] = None
    normalized_jd_file: Optional[str] = None
    raw_jd_file: Optional[str] = None
    final_resume_file: Optional[str] = None
    application_package_path: Optional[str] = None
    notes: Optional[str] = None


class JobDescriptionItem(BaseModel):
    jd_type: str
    file_path: Optional[str] = None
    content_text: Optional[str] = None


class ApplicationJobDescriptions(BaseModel):
    application_id: str
    job_descriptions: List[JobDescriptionItem]


class ApplicationArtifactItem(BaseModel):
    artifact_type: str
    file_path: Optional[str] = None
    content_text: Optional[str] = None


class ApplicationArtifacts(BaseModel):
    application_id: str
    artifacts: List[ApplicationArtifactItem]
