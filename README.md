# Fast ABFE

Investigating rapid ABFE calculations with [A3FE](https://github.com/michellab/a3fe).

## To Run Example

- Install [A3FE and dependencies](https://github.com/michellab/a3fe)
- Clone this repo with `git clone https://github.com/michellab/fast_abfe.git`
- Edit the slurm script at `master_input/run_somd.sh` to run with your slurm installation (change the partition etc)
- Enter desired directory, e.g. `cd cyclod`
- Run `python ../master_input/run_all_a3fe.py` (currently set to run 0.1 ns / window simulations)

## To Analyse

See `analysis.py` in the `scripts` directory for examples of analyses you could perform.

## To Run New Sets of Simulations

Assuming the system is part of https://github.com/openforcefield/protein-ligand-benchmark:

- Pull the [benchmark_repo](https://github.com/openforcefield/protein-ligand-benchmark) into this directory
- See `scripts/setup_pl_benchmark_inp.py` for an automated setup procedure. Run this.
- Attempt to run the full set as above with `run_all_a3fe.py`
- You are likely to run into issues parameterising the protein. If this is the case, see the tip [here](https://a3fe.readthedocs.io/en/latest/guides.html#preparing-input-for-a3fe) for help.

