class Chit:
    def __init__(self, subject, number):
        self.subject = subject
        self.number = number

    def __str__(self):
        return f"{self.subject} {self.number}"

    def __repr__(self):
        return f"{self.subject} {self.number}"

    @classmethod
    def from_json(cls, data):
        return cls(**data)


class PaperChit(Chit):
    def __init__(self, subject, number, size, hiding_place):
        super().__init__(subject, number)
        self.size = size
        self.hiding_place = hiding_place

    def __str__(self):
        return f"{super().__str__()} {self.size} {self.hiding_place}"


class ElectronicChit(Chit):
    def __init__(self, subject, number, media_name):
        super().__init__(subject, number)
        self.media_name = media_name

    def __str__(self):
        return f"{super().__str__()} {self.media_name}"


class Student:
    def __init__(self, name, group, chips=None):
        self.name = name
        self.group = group
        self.chips = chips if not chips is None else []

    def __str__(self):
        s = f"{self.name} {self.group}\n"
        for chip in self.chips:
            s += f"\t{chip}\n"
        return s
    @classmethod
    def from_json(cls, data):
        return cls(**data)