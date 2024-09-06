"""Setup input for a given target from the protein-ligand benchmark repo."""

from pathlib import Path
from subprocess import run

DATA_PATH = Path("../protein-ligand-benchmark/data")
OUTPUT_DIR = Path(".")


def read_sdf(sdf_path: Path) -> dict[str, list[str]]:
    """Read the sdf file and return a dict of molecule names and corresponding sdf block."""
    with open(sdf_path, "r") as f:
        lines = f.readlines()
    sdfs = {}
    lig_name = lines[0].strip()
    current_block = []
    for i, line in enumerate(lines):
        if line.strip() == "$$$$":
            sdfs[lig_name] = current_block
            if i + 1 < len(lines):
                lig_name = lines[i + 1].strip()
            current_block = []
        else:
            current_block.append(line)

        # Check if we have charged ligands
        if "> <i_epik_Tot_Q>" in line:
            charge = float(lines[i + 1])
            if charge != 0:
                print(f"Charged ligand {lig_name} with charge {charge}")

    # Renname all of the ligands LIG by changing the first line of the sdf
    for lig_name, sdf_block in sdfs.items():
        sdf_block[0] = "LIG\n"

    return sdfs


def make_inp_dir(lig_name: str, sdf_block: list[str]) -> None:
    """Make a directory for each ligand and write the sdf block to a file."""
    inp_dir = OUTPUT_DIR / lig_name / "input"
    inp_dir.mkdir(exist_ok=True, parents=True)

    # Write the sdf block to a file
    with open(inp_dir / f"ligand.sdf", "w") as f:
        f.writelines(sdf_block)

    # Copy the protein over
    run(
        [
            "cp",
            TARGET_PATH / "01_protein" / "crd" / "protein.pdb",
            inp_dir / "protein.pdb",
        ]
    )

    # Soft link required control files
    run(["ln", "-s", "../../../master_input/run_somd.sh", inp_dir])
    run(["ln", "-s", "../../../master_input/template_config.cfg", inp_dir])


def main():
    # Parse TARGET as an argument
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--target", help="The target to process")
    args = parser.parse_args()
    global TARGET
    TARGET = args.target
    global TARGET_PATH
    TARGET_PATH = DATA_PATH / TARGET

    # Read the sdf file
    sdf_path = TARGET_PATH / "02_ligands" / "ligands.sdf"
    sdfs = read_sdf(sdf_path)

    # Make the input directories
    for lig_name, sdf_block in sdfs.items():
        make_inp_dir(lig_name, sdf_block)


if __name__ == "__main__":
    main()
