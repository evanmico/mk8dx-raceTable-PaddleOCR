# Mariokart 8 Deluxe Race Finish Screen Text Extraction with PaddleOCR
This is simply a prototype experiment with PaddleOCR to see how manageable it could be for me to extract text from the end screen of races.
## Why did I want to do this in the first place?
I wanted to do this because in Mariokart clan wars there are often disconnects that screw up the entire score calculation for each player at the end of the 12 race war, requiring a rather lengthy and tedious process of going through all of the races and seeing where the player disconnected and adjusting their end score accordingly based on their placements (scores before they are disconnected are not counted by the game automatically). So, I want to in the future us ethe virtual cam of OBS to be able to monitor one player's screen continuously as they play through these wars (usually at least one member on the team has a setup for streaming/recording) and then they can press a hotkey at the end of each race to screenshot the screen and upload that info to a website that I was working on. Was just looking into how on the server side I could more cost-effectively achieve score extraction.
## Challenges I Came Across
- Found out that traditional OCR software really isn't made for this so it struggles to consistently get the names right
- PaddleOCR only really has a good model that does English and Chinese so some names with Cyrillic characters are messed up
- Seems a bit too intensive for what I want to do at the end
- I found a repo later that does exactly what I want, but MUCH better and MUCH less intensively [right here](https://github.com/hlorenzi/mk8d_ocr)
## What I learned
- How to setup a CUDA environment
- How to do image transforms with OpenCV
- A LOT about the many things to consider regarding image formatting for OCR to be effective couortesy of the brilliant PaddleOCR docs and textbook
## Requirements to run
- System with CUDA (probably)
- and some packages, but haven't added requirements.txt yet sorry
  - PaddleOCR
  - OpenCV2
  - numpy
 