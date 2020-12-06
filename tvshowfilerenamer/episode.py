from pathlib import Path
import re
# import pytvmaze

class Episode:
    def __init__(self, filepath, tvshow_name=None, season_number=None, episode_number=None, episode_title=None):
        self.filepath = filepath        
        self.tvshow_name = self.get_tvshow_name() if tvshow_name == None else tvshow_name 
        self.season_number = self.get_season_number() if season_number == None else season_number
        self.episode_number = self.get_episode_number() if episode_number == None else episode_number
        self.episode_title = self.get_episode_title() if episode_title == None else episode_title
        
    def get_tvshow_name(self):
        tvshow_name = self.filepath.parent.parent.name
        return tvshow_name

    def get_season_number(self):
        season_number = int((self.filepath.parent.name).replace('Season ', ''))
        return season_number

    def get_episode_number(self):
        '''
        Extracts the episode number from the file name.
        Common types of file formatting:
            SddEdd
            Episode dd
            {Season Name} - dd
        '''
        # TODO: figure out what to do when no patterns match
        # TODO: add new patterns and figure out how to match multiple patterns
        pattern = r'[Ss](\d+)[Ee](?P<episode_number>\d+)'
        # pattern = r'Episode (\d+)'
        match = re.search(pattern, self.filepath.name)
        if match:
            episode_number = int(match.group('episode_number'))
        else:
            episode_number = None
        return episode_number

    def get_episode_title(self):
        # TODO: Access the TV Maze API to get episode information
        return None

    def get_file_extension(self):
        return self.filepath.suffix

    def __str__(self):
        name = f'{self.tvshow_name} - S{self.season_number:02}E{self.episode_number:02}'
        if self.episode_title:
            name = f'{name} - {self.episode_title}'
        name = f'{name}{self.get_file_extension()}'
        return name