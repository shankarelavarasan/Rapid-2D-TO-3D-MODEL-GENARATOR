import ezdxf
import os

def parse_dxf(filepath):
    """
    Parses a DXF file and extracts geometric entities and dimensions.
    """
    print(f"Current working directory: {os.getcwd()}")
    print(f"Files in CWD: {os.listdir('.')}")
    if not os.path.exists(filepath):
        print(f"File not found at {filepath}")
        return None, None

    try:
        doc = ezdxf.readfile(filepath)
    except IOError:
        print(f"Not a DXF file or a generic I/O error.")
        return None, None
    except ezdxf.DXFStructureError:
        print(f"Invalid or corrupted DXF file.")
        return None, None

    msp = doc.modelspace()

    lines = []
    dimensions = []

    for entity in msp:
        if entity.dxftype() == 'LINE':
            start = entity.dxf.start
            end = entity.dxf.end
            lines.append(((start.x, start.y), (end.x, end.y)))
        elif entity.dxftype() == 'DIMENSION':
            # Extracting dimension info can be complex.
            # This is a simplified approach.
            dim_text = entity.dxf.text
            # The actual measured value is often stored in the dimension's geometry block.
            # For this simple case, we'll just get the explicit text if available.
            if dim_text == '<>':
                # If text is '<>', it means the measurement is displayed.
                # ezdxf can calculate this, but it's not trivial.
                # We'll try to get it from the block.
                try:
                    # Render the dimension to get the measurement
                    measurement = entity.get_measurement()
                    dimensions.append(measurement)
                except Exception as e:
                    print(f"Could not get measurement from dimension: {e}")
            else:
                dimensions.append(dim_text)


    return lines, dimensions

if __name__ == "__main__":
    lines, dimensions = parse_dxf("sample.dxf")
    if lines is not None:
        print("Lines found:")
        for line in lines:
            print(line)
    if dimensions is not None:
        print("\nDimensions found:")
        for dim in dimensions:
            print(dim)
