#!/usr/bin/bash

conda activate txpipe_clp
SLURM_NTASKS=1
mpirun -n ${SLURM_NTASKS} cosmosis --mpi sampler_file.ini
