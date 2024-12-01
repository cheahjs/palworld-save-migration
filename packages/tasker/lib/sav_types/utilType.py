from dataclasses import dataclass, fields

class Null:
    def __repr__(self):
        return "Null()"