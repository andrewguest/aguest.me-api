from typing import Optional

from beanie import Document


class Projects(Document):
    name: str
    description: str
    frontend_lang: Optional[str] = None
    frontend_framework: Optional[str] = None
    backend_lang: Optional[str] = None
    backend_framework: Optional[str] = None
    database: Optional[str] = None
    url: str
    github_repos: Optional[list[str]] = None
    priority: int = 0

    class Settings:
        name = "projects"
