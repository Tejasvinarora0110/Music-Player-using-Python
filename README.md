__PYGAME MIXER__

This module contains classes for loading Sound objects and controlling playback. The mixer module is optional and depends on SDL_mixer. Your program should test that pygame.mixerpygame module for loading and playing sounds is available and initialized before using it.
The mixer module has a limited number of channels for playback of sounds. Usually programs tell pygame to start playing audio and it selects an available channel automatically. The default is 8 simultaneous channels, but complex programs can get more precise control over the number of channels and their use.
All sound playback is mixed in background threads. When you begin to play a Sound object, it will return immediately while the sound continues to play. A single Sound object can also be actively played back multiple times.
The mixer also has a special streaming channel. This is for music playback and is accessed through the pygame.mixer.musicpygame  module for controlling streamed audio module.
The mixer module must be initialized like other pygame modules, but it has some extra conditions. The pygame.mixer.init() function takes several optional arguments to control the playback rate and sample size.

__TKINTER__

The tkinter package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit. Both Tk and tkinter are available on most Unix platforms, as well as on Windows systems. (Tk itself is not part of Python; it is maintained at ActiveState.)

For more info about these modules go to:

	__Tkinter__- https://tkdocs.com/shipman/

	__Mixer__ - https://www.pygame.org/docs/ref/mixer.html




        
