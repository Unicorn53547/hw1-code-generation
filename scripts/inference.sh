set -ex
OUTPUT_DIR=result_v3
MODEL=Qwen2.5-Coder-3B-Instruct
DATASET=mbpp_pro
TASK_TYPE=mbpp_pro_1shot

python -m santize \
    --model_name $MODEL \
    --source_path ${OUTPUT_DIR}/${MODEL}/${TASK_TYPE}/outputs/ \
    
python -m harness \
    --model_name $MODEL \
    --task $TASK_TYPE \
    --dataset_path dataset/mbpp_pro_subset_10.json \
    --source_path ${OUTPUT_DIR}/${MODEL}/${TASK_TYPE}/outputs/ \
    --save_path ${OUTPUT_DIR}/${MODEL}/${TASK_TYPE} \
    --run_code
