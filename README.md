## The GANterbury Tales

This repo contains the code and results of my entry for [NaNoGenMo 2019](https://github.com/NaNoGenMo/2019). Hopefully some of these resources may be useful to others - if you have any questions, feel free to reach out.

### Setup

The contents in the “files” folder are all you need to get going, but if you want to do a similar project on a different corpus, I’ve included a `clean.py` script that eliminates a number of common formats for footnotes or editor’s notes in Project Gutenberg. Simply run `python clean.py (path_to_your_file.txt)` to output a cleaned version. Right now, it just contains a number of variables representing different common patterns, so you may want to edit and pick and choose to your needs - don’t accidentally delete text that’s meant to be in  your corpus!

Once your corpus is ready, I’ve modified the sample code from [minimaxir’s gpt-2-simple package](https://github.com/minimaxir/gpt-2-simple) so you can plug and play it.

Simply run `python retrain.py -m=(your preferred model, right now options are “124M” and “355M) -f=”path_to_your_file” -s=(optional number of steps you want to retrain for)`. Alternately, if you don’t have access to a GPU/don’t want to wait to train, I’ve kindly used up all my git large file storage to include a 1000 step training in the checkpoints folder. This one has some anachronisms (it seems to make a lot of winky faces, for example), but still does a halfway decent job.

Once you’ve retrained your model, you can generate a 50,000ish word text using `python novel_gen.py -d=“file_to_write_to" -c=“checkpoint_location" -t=“model temperature"`. This script pulls a sentence from the original text as a seed, then generates a few paragraphs from GPT-2, gets a character count from the generated text, moves to that point in the original, and uses the nearest sentence as a seed for the next generation until it hits 50,000 words

**TODOS**
- [] turn all `clean.py` vars into command line options
- [x] script to actually generate novel - need to mess with seeding, temp and length to see best mix of structure/randomness
