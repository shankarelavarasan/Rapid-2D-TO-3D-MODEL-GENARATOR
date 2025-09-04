import cadscript as cad

def create_3d_model(lines, amount, output_path):
    """
    Creates a 3D model by extruding a 2D shape defined by lines.

    :param lines: A list of tuples, where each tuple represents a line with start and end points.
                  e.g., [((x1, y1), (x2, y2)), ...]
    :param amount: The amount to extrude the shape.
    :param output_path: The path to save the output file (e.g., .stl, .step).
    """
    if not lines:
        print("No lines to create a model from.")
        return

    # Convert the list of line segments into a single list of points for the polygon
    points = [line[0] for line in lines]
    # The last point should be the same as the first to close the polygon,
    # but add_polygon might handle this automatically. Let's assume it does for now.

    # Create a sketch and add the polygon
    sketch = cad.make_sketch()
    sketch.add_polygon(points)

    # Extrude the sketch from the XY plane
    body = cad.make_extrude("XY", sketch, amount)

    # Save the model
    if output_path.lower().endswith(".stl"):
        body.export_stl(output_path)
    elif output_path.lower().endswith(".step") or output_path.lower().endswith(".stp"):
        body.export_step(output_path)
    else:
        print(f"Unsupported output file format: {output_path}. Please use .stl or .step")
        return

    print(f"3D model saved to {output_path}")

if __name__ == "__main__":
    # This is an example of how to use the function.

    # Example: a 100x50 rectangle
    sample_lines = [
        ((0, 0), (100, 0)),
        ((100, 0), (100, 50)),
        ((100, 50), (0, 50)),
        ((0, 50), (0, 0))
    ]

    create_3d_model(sample_lines, amount=20, output_path="sample.stl")
