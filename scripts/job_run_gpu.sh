#!/bin/bash

# You must specify a valid email address!
#SBATCH --mail-user=timo.kofmehl@students.unibe.ch

# Mail on NONE, BEGIN, END, FAIL, REQUEUE, ALL
#SBATCH --mail-type=BEGIN,FAIL,END

# Job name
#SBATCH --job-name="KnearestNeighbors"

# Runtime and memory
#SBATCH --time=00:60:00
#SBATCH --mem-per-cpu=32G

# Partition
#SBATCH --partition=bdw
#SBATCH --cpus-per-task=10
#SBATCH --gres=gpu:gtx1080ti:1

#### Your shell commands below this line ####

# module load CUDA/10.1.243
# module load cuDNN/7.6.0.64-gcccuda-2019a


#### Start training,testing, evaluation ####
srun python3 MIA_Lab_Roesch_Kofmehl/bin/main.py