import argparse
from src.parser import parse_dxf
from src.generator import create_3d_model

def main():
    """
    The main function for the command-line interface.
    """
    parser = argparse.ArgumentParser(
        description="Generate a 3D model from a 2D DXF file."
    )
    parser.add_argument(
        "input_dxf",
        help="Path to the input DXF file."
    )
    parser.add_argument(
        "output_file",
        help="Path to save the output file (e.g., model.stl or model.step)."
    )
    parser.add_argument(
        "--amount",
        type=float,
        default=10.0,
        help="The amount to extrude the shape (default: 10.0)."
    )

    args = parser.parse_args()

    print(f"Parsing DXF file: {args.input_dxf}...")
    lines, dimensions = parse_dxf(args.input_dxf)

    if lines is None:
        print("Could not parse DXF file. Aborting.")
        return

    print(f"Found {len(lines)} lines and {len(dimensions)} dimensions.")

    # For now, we still use the command-line amount.
    # In the next step, we will use the parsed dimensions.
    extrusion_amount = args.amount

    print(f"Generating 3D model...")
    print(f"Extrusion amount: {extrusion_amount}")
    print(f"Output file: {args.output_file}")

    try:
        create_3d_model(
            lines=lines,
            amount=extrusion_amount,
            output_path=args.output_file
        )
    except Exception as e:
        print(f"An error occurred during model generation: {e}")

if __name__ == "__main__":
    main()
