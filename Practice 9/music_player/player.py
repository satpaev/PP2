import os
import pygame


class MusicPlayer:
    def __init__(self, music_folder):
        self.music_folder = music_folder
        self.playlist = self.load_playlist()
        self.current_index = 0

        self.is_playing = False
        self.is_paused = False

        # Time tracking for accurate pause/resume display.
        self.elapsed_before_pause_ms = 0
        self.play_start_tick_ms = 0

    def load_playlist(self):
        formats = (".mp3", ".wav")
        files = []

        for file_name in os.listdir(self.music_folder):
            if file_name.lower().endswith(formats):
                full_path = os.path.join(self.music_folder, file_name)
                files.append(full_path)

        files.sort()
        return files

    def get_current_track_name(self):
        if not self.playlist:
            return "No tracks found"
        return os.path.basename(self.playlist[self.current_index])

    def load_current_track(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])

    def reset_time_tracking(self):
        self.elapsed_before_pause_ms = 0
        self.play_start_tick_ms = 0

    def play(self):
        if not self.playlist:
            return

        try:
            if self.is_paused:
                pygame.mixer.music.unpause()
                self.play_start_tick_ms = pygame.time.get_ticks()
                self.is_playing = True
                self.is_paused = False
            elif not self.is_playing:
                self.load_current_track()
                pygame.mixer.music.play()
                self.reset_time_tracking()
                self.play_start_tick_ms = pygame.time.get_ticks()
                self.is_playing = True
                self.is_paused = False
        except pygame.error as e:
            print(f"Error playing track: {e}")
            self.is_playing = False
            self.is_paused = False
            self.reset_time_tracking()

    def stop(self):
        # Pause at the exact current point.
        if self.is_playing:
            now = pygame.time.get_ticks()
            self.elapsed_before_pause_ms += now - self.play_start_tick_ms
            pygame.mixer.music.pause()
            self.is_playing = False
            self.is_paused = True

    def full_stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False
        self.reset_time_tracking()

    def next_track(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.full_stop()
            self.play()

    def previous_track(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.full_stop()
            self.play()

    def get_position_seconds(self):
        if self.is_playing:
            now = pygame.time.get_ticks()
            current_ms = self.elapsed_before_pause_ms + (now - self.play_start_tick_ms)
            return max(0, current_ms // 1000)

        if self.is_paused:
            return max(0, self.elapsed_before_pause_ms // 1000)

        return 0
