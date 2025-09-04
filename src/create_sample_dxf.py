import ezdxf

def create_sample_dxf(filepath="sample.dxf"):
    """
    Creates a simple DXF file with a rectangle and a dimension.
    """
    doc = ezdxf.new()
    msp = doc.modelspace()

    # Add a rectangle (as four lines)
    msp.add_line((0, 0), (100, 0))
    msp.add_line((100, 0), (100, 50))
    msp.add_line((100, 50), (0, 50))
    msp.add_line((0, 50), (0, 0))

    # Add a horizontal dimension
    dim = msp.add_aligned_dim(p1=(0, 0), p2=(100, 0), distance=10)
    dim.render()

    doc.saveas(filepath)
    print(f"Sample DXF file created at {filepath}")

if __name__ == "__main__":
    create_sample_dxf()
