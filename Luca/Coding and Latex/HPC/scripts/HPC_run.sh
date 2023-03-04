#!/bin/bash
#SBATCH --partition=defq
#SBATCH --array=1-10
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=10m
#SBATCH --time=00:10:00
#below use Linux commands, which will run on compute node

echo "Running on `hostname`"
cd ${SLURM_SUBMIT_DIR}
module purge
module load anaconda-uon/3

source ~/.bashrc
conda activate year4projenv

TASK=${SLURM_ARRAY_TASK_ID}
python -u main.py $TASK
echo "Finished job now"