
export VLLM_WORKER_MULTIPROC_METHOD=spawn
export HF_DATASETS_CACHE="CACHE_DIR"

# export NCCL_ASYNC_ERROR_HANDLING=1
# export NCCL_DEBUG=WARN
# export NCCL_IB_DISABLE=1        # single node
# export NCCL_P2P_LEVEL=NVL       # prefer NVLink on H100 boxes
# # optional if supported:
# export NCCL_NVLS_ENABLE=1
set -ex
OUTPUT_DIR=result_v3
MODEL=Qwen2.5-Coder-3B-Instruct
MODEL_PATH=MOEDL_PATH
TASK_TYPE=mbpp_pro_1shot # or mbpp_pro
mkdir -p ${OUTPUT_DIR}/${MODEL}/${TASK_TYPE}/outputs/

python -m eval.inference \
  --model_name_or_path $MODEL_PATH \
  --save_path ${OUTPUT_DIR}/${MODEL}/${TASK_TYPE}/outputs/results.jsonl \
  --dataset $TASK_TYPE \
  --is_use_vllm true \
  --use_flash_attention false \
  --do_sample false \
  --temperature 0.0 \
  --top_p 1.0 \
  --max_new_tokens 4096 \
  --n_problems_per_batch 10 \
  --n_samples_per_problem 1 \
  --n_batches 1 