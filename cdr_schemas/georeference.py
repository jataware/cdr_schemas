from typing import List, Union, Optional

from pydantic import BaseModel, Field
from enum import Enum


class PointType(str, Enum):
    Point = "Point"


class Geom_Point(BaseModel):
    """
    Geometry Point:
    Point geometry in world coordinates (longitude, latitude).
    """
    coordinates:List[Optional[Union[float, int]]]
    type: PointType  = PointType.Point


class Pixel_Point(BaseModel):
    """
    Pixel point. 
    Point geometry in pixel coordinates (columns from left, row from bottom).
    """
    coordinates:List[Union[float, int]]
    type: PointType  = PointType.Point


class GroundControlPoint(BaseModel):
    """Ground control point model for mapping and georeferencing purposes.
    
    Attributes:
        map_geom (Geom_Point): Point geometry in world coordinates (longitude, latitude).
        px_geom (Pixel_Point): Point geometry in pixel coordinates (columns from left, row from bottom).
        confidence (Optional[float]): Confidence associated with this extraction.
        model (str): Name of the model used.
        model_version (str): Version of the model.
        crs (Optional[str]): Coordinate reference system.
    """
    map_geom: Geom_Point = Field(..., description="Point geometry, world coordinates, [longitude, latitude]")
    px_geom: Pixel_Point = Field(..., description="Point geometry, pixel coordinates, [columns from left, row from bottom]")
    confidence: Optional[float] = Field(..., description="Confidence associated with this extraction")
    model: str
    model_version: str
    crs: Optional[str]
    

class GeoreferenceResults(BaseModel):
    """Georeference Results.
    
    Attributes:
        map_id: Identifier for the map.
        crs: Projection EPSG code used for projection. ie EPSG:32612
        likely_CRSs: List of potential Coordinate Reference System specifically Projection Coordinate System for the map. ie ["EPSG:32612", "EPSG:32613"]
        gcps:  gcps used in the projected raster output
        unused_gcps: gcps that were not used in the projected raster output
        system: Name of the system used.
        system_version: Version of the system.
    """
    map_id: str
    crs: Optional[str] 
    likely_CRSs: Optional[List[str]]   
    gcps: Optional[List[GroundControlPoint]]
    unused_gcps: Optional[List[GroundControlPoint]]
    system: str  
    system_version: str 
    
