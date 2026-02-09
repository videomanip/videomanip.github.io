#!/usr/bin/env python3
"""
Script to delete all video files ending with "backup" in the specified folder and its subfolders.
"""

import os
import sys
from pathlib import Path

def delete_backup_videos(root_dir):
    """
    Recursively find and delete all video files with "backup" at the end of their name.
    
    Args:
        root_dir: The root directory to search in
    """
    root_path = Path(root_dir)
    
    if not root_path.exists():
        print(f"Error: Directory '{root_dir}' does not exist.")
        return
    
    if not root_path.is_dir():
        print(f"Error: '{root_dir}' is not a directory.")
        return
    
    # Common video file extensions
    video_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.m4v'}
    
    deleted_files = []
    deleted_count = 0
    
    # Walk through all files in the directory and subdirectories
    for file_path in root_path.rglob('*'):
        if file_path.is_file():
            # Get file extension
            file_ext = file_path.suffix.lower()
            
            # Check if it's a video file
            if file_ext in video_extensions:
                # Get filename without extension
                filename_without_ext = file_path.stem
                
                # Check if filename ends with "backup" (case-insensitive)
                if filename_without_ext.lower().endswith('backup'):
                    try:
                        file_path.unlink()  # Delete the file
                        deleted_files.append(str(file_path))
                        deleted_count += 1
                        print(f"Deleted: {file_path}")
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")
    
    print(f"\nTotal files deleted: {deleted_count}")
    return deleted_files

if __name__ == "__main__":
    # Default directory
    target_dir = "/home/hongyi/video2manip.github.io/static/data/manip"
    
    # Allow command-line argument for directory
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    
    print(f"Searching for backup videos in: {target_dir}")
    print("=" * 60)
    
    deleted = delete_backup_videos(target_dir)
    
    if deleted:
        print("\nDeleted files:")
        for f in deleted:
            print(f"  - {f}")

