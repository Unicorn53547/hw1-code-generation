#!/usr/bin/env python3
import json
import random
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Randomly pick 20 questions from a JSON file.")
    parser.add_argument("--input", type=Path, required=True, help="Path to input JSON file")
    parser.add_argument("--output", type=Path, required=True, help="Path to output JSON file")
    parser.add_argument("--num", type=int, default=20, help="Number of questions to sample (default: 20)")
    args = parser.parse_args()

    # Load input JSON
    with args.input.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Input JSON must be a list of question objects.")

    # Randomly sample
    n = min(args.num, len(data))
    sampled = random.sample(data, n)

    # Save output JSON
    with args.output.open("w", encoding="utf-8") as f:
        json.dump(sampled, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved {n} randomly selected questions to {args.output}")

if __name__ == "__main__":
    main()
