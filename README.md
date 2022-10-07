# party-parrot-replit

A repl.it project for a terminal-based party parrot.

## What's here

* main.py — A Python program that connects to http://parrot.live/, gets each frame of animation, and displays them in a terminal.  It's a little slow because it uses a network connection to get the frames.
* frames-ansi
  * run.sh — A shell script which reads the ANSI animation frame files and displays them in a terminal.  It's also a little slow, because the frames are large and contain many ANSI color sequences.
* frames-txt
  * run.sh — A shell script which reads the text animation frame files and displays them in a terminal.  This is a little faster because it uses the simple text frames (the same ones the network-based Python program uses) and adds a single color for the whole frame.
  
