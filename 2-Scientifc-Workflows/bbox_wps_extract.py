from osgeo import ogr

def title():
    return "Bounding Box Extraction"

def abstract():
    return "Extracts the bounding box (envelope) of a given vector geometry and returns it as a GeoJSON Polygon."

def inputs():
    return [
        ['geometry', 'Input Geometry', 'Vector geometry for which the bounding box will be calculated.', 'application/json', True]
    ]

def outputs():
    return [
        ['bbox', 'Bounding Box', 'The bounding box of the input geometry as a GeoJSON Polygon.', 'application/json']
    ]

def execute(parameters):
    geometry_param = parameters.get('geometry')

    if geometry_param is not None:
        geom_json = geometry_param['value']
        geom = ogr.CreateGeometryFromJson(geom_json)

        if geom is None:
            print("Content-type: text/plain")
            print()
            print("Invalid GeoJSON input.")
            return

        # Get Envelope: (minX, maxX, minY, maxY)
        envelope = geom.GetEnvelope()
        minX, maxX, minY, maxY = envelope[0], envelope[1], envelope[2], envelope[3]

        # Create Polygon from Envelope
        ring = ogr.Geometry(ogr.wkbLinearRing)
        ring.AddPoint(minX, minY)
        ring.AddPoint(maxX, minY)
        ring.AddPoint(maxX, maxY)
        ring.AddPoint(minX, maxY)
        ring.AddPoint(minX, minY)  # Close the ring

        bbox_polygon = ogr.Geometry(ogr.wkbPolygon)
        bbox_polygon.AddGeometry(ring)

        # Output as GeoJSON
        print("Content-type: application/json")
        print()
        print(bbox_polygon.ExportToJson())
    else:
        print("Content-type: text/plain")
        print()
        print("Missing required 'geometry' input.")
