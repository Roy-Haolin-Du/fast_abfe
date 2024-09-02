# Fast ABFE

Investigating rapid ABFE calculations with [A3FE](https://github.com/michellab/a3fe).

## To Run

- Install [A3FE and dependencies](https://github.com/michellab/a3fe)
- Clone this repo with `git clone https://github.com/michellab/fast_abfe.git`
- Edit the slurm script at `master_input/run_somd.sh` to run with your slurm installation (change the partition etc)
- Enter desired directory, e.g. `cd cyclod`
- Run `python ../master_input/run_all_a3fe.py` (currently set to run 0.1 ns / window simulations)
