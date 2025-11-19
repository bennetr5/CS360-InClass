from dataclasses import dataclass, field

@dataclass
class Profile:
    username: str
    email: str
    courses: list[str] = field(default_factory=list)

    def update_email(self, new_email: str) -> None:
        self.email = new_email

    def add_course(self, course_name: str) -> None:
        self.courses = list({*self.courses, course_name})

    def remove_course(self, course_name: str) -> None:
        if course_name in self.courses:
            self.courses.remove(course_name)

    def has_course(self, course_name: str) -> bool:
        return course_name in self.courses
    