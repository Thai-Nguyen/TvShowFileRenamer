# TV Show File Renamer
This package finds and renames video files in a given directory.

## File Naming Convention
The program renames the video file into a standard format that is recognized by home theatre software such as Kodi, XBMC, or Plex.

The TV Show FIle Renamer attempts to extract the following information from a given video file: 
- TV show name
- TV season number
- TV episode number
- TV episode title

 The program specifically renames the file into

    <TV Show Name> - S<Season Number>E<Episode Number> - <Episode Title>

For example, given the following file 
    
    E:\TV Shows\The Umbrella Academy\Season 1\the.umbrella.academy.s01e08.internal.1080p.web.x264-strife.mkv

The file would be renamed to

    E:\TV Shows\The Umbrella Academy\Season 1\The Umbrella Academy - S01E08 - I Heard a Rumor.mkv

## Accepted Video File Extensions
The program only accepts the following video file extensions:
- mkv
- avi
- mp4
- mov
- wmv
- flv
- webm

Any files that do not include the accepted file extensions will be ignored.