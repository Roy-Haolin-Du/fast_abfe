""""Run A3FE calculations for all ligands."""

import os

import a3fe as a3


def get_cfg(fast: bool = True) -> a3.SystemPreparationConfig:
    cfg = a3.SystemPreparationConfig()
    cfg.forcefields["ligand"] = "gaff2"
    lambda_values = {
        a3.LegType.BOUND: {
            a3.StageType.RESTRAIN: [0.0, 1.0],
            a3.StageType.DISCHARGE: [0.0, 0.291, 0.54, 0.776, 1.0],
            a3.StageType.VANISH: [
                0.0,
                0.026,
                0.054,
                0.083,
                0.111,
                0.14,
                0.173,
                0.208,
                0.247,
                0.286,
                0.329,
                0.373,
                0.417,
                0.467,
                0.514,
                0.564,
                0.623,
                0.696,
                0.833,
                1.0,
            ],
        },
        a3.LegType.FREE: {
            a3.StageType.DISCHARGE: [0.0, 0.222, 0.447, 0.713, 1.0],
            a3.StageType.VANISH: [
                0.0,
                0.026,
                0.055,
                0.09,
                0.126,
                0.164,
                0.202,
                0.239,
                0.276,
                0.314,
                0.354,
                0.396,
                0.437,
                0.478,
                0.518,
                0.559,
                0.606,
                0.668,
                0.762,
                1.0,
            ],
        },
    }
    cfg.lambda_values = lambda_values
    cfg.slurm = True
    if fast:  # Drop the equilibration times
        cfg.runtime_npt_unrestrained = 50
        cfg.runtime_npt = 50
        cfg.ensemble_equilibration_time = 100

    return cfg


def main() -> None:
    calc_paths = [d for d in os.listdir() if "lig" in d]
    calc_set = a3.CalcSet(calc_paths=calc_paths)

    # Set the calcuations up with a "fast" config
    cfg = get_cfg(fast=True)
    calc_set.setup(bound_leg_sysprep_config=cfg, free_leg_sysprep_config=cfg)

    # Run the calculations
    calc_set.run(adaptive=False, runtime=0.1, run_stages_parallel=True)


if __name__ == "__main__":
    main()
