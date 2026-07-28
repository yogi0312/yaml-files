#!/usr/bin/env python3
"""
OOMKill Test Script
This script demonstrates Out-Of-Memory (OOM) kill by allocating memory in 10 MB chunks.
Useful for testing Kubernetes OOM kill behavior with resource limits.

Usage:
    python3 oomkill_test.py

The script will:
1. Allocate 10 MB chunks of memory using bytearray
2. Print memory allocation progress
3. Continue until the system runs out of memory and kills the process
"""

import time
import sys

def allocate_memory_chunks(chunk_size_mb=10):
    """
    Allocate memory in chunks using bytearray to trigger OOM kill.
    
    Args:
        chunk_size_mb (int): Size of each memory chunk in MB (default: 10 MB)
    """
    chunk_size_bytes = chunk_size_mb * 1024 * 1024  # Convert MB to bytes
    allocated_chunks = []
    iteration = 0
    
    print(f"Starting OOMKill test - allocating {chunk_size_mb} MB chunks...")
    print("Press Ctrl+C to stop gracefully\n")
    
    try:
        while True:
            iteration += 1
            total_allocated_mb = (iteration * chunk_size_mb)
            
            try:
                # Allocate a chunk of memory
                chunk = bytearray(chunk_size_bytes)
                allocated_chunks.append(chunk)
                
                # Print progress
                print(f"Iteration {iteration}: Allocated {total_allocated_mb} MB total memory")
                
                # Add a small delay to make progress visible
                time.sleep(0.1)
                
            except MemoryError:
                print(f"\n[ERROR] MemoryError at iteration {iteration}: Could not allocate more memory")
                print(f"Total memory allocated before error: {total_allocated_mb} MB")
                break
    
    except KeyboardInterrupt:
        print(f"\n\n[INFO] Gracefully stopped at iteration {iteration}")
        print(f"Total memory allocated: {total_allocated_mb} MB")
        return

if __name__ == "__main__":
    # You can modify chunk size as command line argument
    chunk_mb = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    
    print("=" * 60)
    print("OOMKill Test - Memory Allocation Script")
    print("=" * 60)
    print(f"Chunk size: {chunk_mb} MB")
    print("=" * 60 + "\n")
    
    allocate_memory_chunks(chunk_size_mb=chunk_mb)
    
    print("\n[INFO] Memory allocation test completed or terminated by system OOMKill")
