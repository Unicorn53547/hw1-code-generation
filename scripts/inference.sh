set -ex
OUTPUT_DIR=result_new
MODEL=Llama-3.2-3B-Instruct
DATASET=mbpp_pro
TASK_TYPE=mbpp_pro_cot

python -m santize \
    --model_name $MODEL \
    --source_path ${OUTPUT_DIR}/${MODEL}/${TASK_TYPE}/outputs/ \
    
python -m harness \
    --model_name $MODEL \
    --task $TASK_TYPE \
    --dataset_path dataset/mbpp_new.json \
    --source_path ${OUTPUT_DIR}/${MODEL}/${TASK_TYPE}/outputs/ \
    --save_path ${OUTPUT_DIR}/${MODEL}/${TASK_TYPE} \
    --run_code
