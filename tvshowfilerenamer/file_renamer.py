from pathlib import Path
from episode import Episode
import argparse

video_file_extensions = ('mkv', 'avi', 'mp4', 'mov', 'wmv', 'flv', 'webm')

def get_episodes(directory_path, verbose=False):
    files = []
    episodes = []

    # Get list of video files in directory
    for type in video_file_extensions:
        files.extend(Path(directory_path).glob(f'**/*.{type}'))
    # Create Episode objects
    for file in files:
        if verbose:
            print(file)
        episode = Episode(file)
        episodes.append(episode)
    return episodes

def rename_files(episodes, verbose=False):
    for episode in episodes:
        folder = episode.filepath.parent
        new_filepath = Path(f'{folder}/{episode}')
        if verbose:
            print(new_filepath)
        episode.filepath.rename(new_filepath)

def dir_path(path):
    if Path(path).is_dir():
        return path
    else:
        raise argparse.ArgumentTypeError(f'readable_dir:{path} is not a valid path')

def parse_arguments():
    parser = argparse.ArgumentParser( 
        description='Renames TV show files from a given directory')
    parser.add_argument('directory', 
        type=dir_path, 
        help='a folder containing the TV show video files')
    parser.add_argument('-v-', '--verbose',
        action='store_true', 
        help='increase output verbosity')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    # Get list of episodes in the given directory
    episodes = get_episodes(args.directory, verbose=args.verbose)
    # Rename files
    rename_files(episodes, verbose=args.verbose)
    
if __name__ == '__main__':
    main()
