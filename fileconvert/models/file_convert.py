from fileconvert.models import db
from fileconvert import models as m


class FileConvert(db.Model, m.TimestampMixin):
    """
    Contains information of banner_type table
    """
    __tablename__ = 'file_convert'

    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(255), nullable=False)
    path = db.Column(db.TEXT, nullable=True)

    def to_dict(self):
        return {"id": self.id,
                "name": self.name,
                "code": self.code,
                "path": self.description
                }
