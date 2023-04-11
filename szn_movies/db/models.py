from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, JSON

BaseModel = declarative_base()

class Movies(BaseModel):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    shortName = Column(String, default="")
    iconUri = Column(String, default="")
    manifestUri = Column(String, default="")
    source = Column(String, default="")
    focus = Column(Boolean, default=False)
    disabled = Column(Boolean, default=False)
    extraText = Column(JSON, default=[])
    certificateUri = Column(String, nullable=True)
    description = Column(String, nullable=True)
    isFeatured = Column(Boolean, default=False)
    drm = Column(JSON, default=[])
    features = Column(JSON, default=[])
    licenseServers = Column(JSON, default={})
    licenseRequestHeaders = Column(JSON, default={})
    requestFilter = Column(String, nullable=True)
    responseFilter = Column(String, nullable=True)
    clearKeys = Column(JSON, default={})
    extraConfig = Column(JSON, nullable=True)
    adTagUri = Column(String, nullable=True)
    imaVideoId = Column(String, nullable=True)
    imaAssetKey = Column(String, nullable=True)
    imaContentSrcId = Column(Integer, nullable=True)
    mimeType = Column(String, nullable=True)
    mediaPlaylistFullMimeType = Column(String, nullable=True)
    storedProgress = Column(Integer, default=0)
    storedContent = Column(JSON, nullable=True)
