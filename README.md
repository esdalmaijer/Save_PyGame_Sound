Save PyGame Sound as wave file
==============================

**TL;DR: Could not find easy way to make sound files out of
NumPy arrays, so here are example scripts.**

Sometimes I use PyGame's [Surface class](http://pygame.org/docs/ref/surface.html) and [image module](http://pygame.org/docs/ref/image.html) to
create and save images. This works brilliantly if you need to
quickly implement a simple algorithm that consists of highly
repetitive steps (e.g. creating fields of random dots, making
backgrounds transparant, cropping images, etc.).

So when I needed to create sounds out of NumPy arrays today,
I automatically turned to PyGame. Without thinking, I started
writing my script. I created my NumPy Arrays, converted them
to PyGame Sounds, end then went on to save them.

But, wait, what? There's no function to do that!? A quick
Google search learned that [more](http://stackoverflow.com/questions/17292444/pygame-mixer-save-audio-to-disk) [people](http://stackoverflow.com/questions/2141315/pygame-saving-audio-files) have asked similar
things, but haven't found a working answer yet. This makes
sense: PyGame was not quite designed to do these things.

A bit more Googling brought up the [`wave`](https://docs.python.org/2/library/wave.html), a native Python
module to read and write WAV files. Brilliant stuff! It took
a bit of fiddling around, but was really easy.

In this repository, I provide some working examples. If you
want to use them, please do feel free. They provide a good
start if you want to do more fancy stuff.