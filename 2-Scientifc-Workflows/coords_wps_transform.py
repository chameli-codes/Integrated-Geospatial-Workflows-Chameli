# ---------------------
# Coordinate Transformation function using WPS specification
# ---------------------
from osgeo import ogr
from osgeo import osr

def title():
    return "Coordinate Transform" # title of the function

def abstract():
    return "A function that tranform coordinates of a vector geometry from one spatial reference system to another." # short description of the function

def inputs():
    return [
        ['feature', 'Input feature','The feature in the source reference system.','application/json', True],
        ['sourcesrid', 'Source SRID', 'The Spatial Reference System Identifier for the input data e.g 4326.', 'integer', True],
        ['targetsrid', 'Target SRID', 'The Spatial Reference System Identifier for the output data e.g 3857.', 'integer', True]
    ]

def outputs():
    return [['result', 'transformed feature','The feature in the target reference system','application/json']]

def execute(parameters):
    feature = parameters.get('feature')
    sourcesrid = parameters.get('sourcesrid')
    targetsrid = parameters.get('targetsrid')
    if (feature is not None) and (sourcesrid is not None) and (targetsrid is not None):
        feature = feature['value']
        sourcesrid = sourcesrid['value']
        targetsrid = targetsrid['value']

    source = osr.SpatialReference()
    source.ImportFromProj4("+proj=longlat +datum=WGS84 +no_defs")
    target = osr.SpatialReference()
    target.ImportFromProj4("+proj=merc +a=6378137 +b=6378137 +lat_ts=0 +lon_0=0 +x_0=0 +y_0=0 +k=1 +units=m +nadgrids=@null +wktext +no_defs")

    coordtransform = osr.CoordinateTransformation(source, target)
    inputfeature = ogr.CreateGeometryFromJson(feature)
    inputfeature.Transform(coordtransform)
    print("Content-type: application/json")
    print()
    print(inputfeature.ExportToJson())