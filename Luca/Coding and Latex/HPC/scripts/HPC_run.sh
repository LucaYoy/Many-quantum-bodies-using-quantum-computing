#!/bin/bash
#SBATCH --partition=defq
#SBATCH --array=0,1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=10g
#SBATCH --time=120:00:00
#below use Linux commands, which will run on compute node

echo "Running on `hostname`"
cd ${SLURM_SUBMIT_DIR}
module purge
module load anaconda-uon/3

source ~/.bashrc
conda activate year4projenv

TASK=${SLURM_ARRAY_TASK_ID}
for i in {1..10}
do 
	python -u main.py $TASK
done
echo "Finished job now"