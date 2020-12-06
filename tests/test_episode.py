from episode import Episode
import unittest

class TestEpisode(unittest.TestCase):
    def create_episode(self):
        pass

    def create_episode_given_wrong_file(self):
        pass

    def test_get_tvshow_name(self):
        from pathlib import Path
        file = Path('E:/TV Shows/The Umbrella Academy/Season 1/the.umbrella.academy.s01e02.internal.1080p.web.x264-strife.mkv')

    def test_get_season_number(self):
        from pathlib import Path
        file = Path('E:/TV Shows/The Umbrella Academy/Season 1/the.umbrella.academy.s01e02.internal.1080p.web.x264-strife.mkv')
        test_episode = Episode(file)
        result = test_episode.get_season_number(file)
        self.assertEqual(result, 1, 'Should be 1')

    def test_get_episode_number_from_video_file(self):
        from pathlib import Path
        file = Path('E:/TV Shows/The Umbrella Academy/Season 1/the.umbrella.academy.s01e02.internal.1080p.web.x264-strife.mkv')
        test_episode = Episode(file)
        result = test_episode.get_episode_number(file) 
        self.assertEqual(result, 2, 'Should be 2')

    def test_get_episode_number_from_wrong_file_format(self):
        from pathlib import Path
        file = Path('E:/TV Shows/The Umbrella Academy/Season 1/[TGx]Downloaded from torrentgalaxy.org.txt')
        test_episode = Episode(file)
        result = test_episode.get_episode_number(file) 
        self.assertEqual(result, None)

    def test_get_episode_title(self):
        pass

    def test_get_file_extension_from_mkv_file(self):
        from pathlib import Path
        file = Path('E:/TV Shows/My Hero Academia/Season 4/My Hero Academia S04E11 Lemillion.mkv')
        test_episode = Episode(file)
        result = test_episode.get_file_extension(file)
        self.assertEqual(result, '.mkv', 'Should return ".mkv"')

if __name__ == '__main__':
    unittest.main()