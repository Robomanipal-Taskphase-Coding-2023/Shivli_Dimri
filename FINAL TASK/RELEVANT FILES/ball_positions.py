#!/usr/bin/env python3




import xml.etree.ElementTree as ET

def parse_urdf(urdf_file):
    ball_positions = []
    
    tree = ET.parse(urdf_file)
    root = tree.getroot()
    
    # Iterate through all links in the URDF
    for link in root.findall('.//link'):
        # Check if the link has a visual element (assuming balls are represented visually)
        visual = link.find('visual')
        if visual is not None:
            geometry = visual.find('geometry')
            if geometry is not None:
                # Assuming balls are represented by spheres
                sphere = geometry.find('sphere')
                if sphere is not None:
                    # Extract position of the ball
                    origin = visual.find('origin')
                    if origin is not None:
                        xyz = origin.attrib.get('xyz')
                        if xyz is not None:
                            position = [float(coord) for coord in xyz.split()]
                            ball_positions.append(position)
    
    return ball_positions

# Change the filename to your URDF file
urdf_file = 'areaurdf_noarea1.urdf'
ball_positions = parse_urdf(urdf_file)
print("Ball positions:", ball_positions)
