## The GANterbury Tales

This repo contains the code and results of my entry for [NaNoGenMo 2019](https://github.com/NaNoGenMo/2019). Hopefully some of these resources may be useful to others - if you have any questions, feel free to reach out.

## Sample Output


#### 901 Steps

`A! false god, false god! owen god?
Who is he? who is he? who is he?
He is my lord, and my fader, y-lyke.
For I am him-self ful wo: 'al peyne me
Of my worship;) it wol nat faille me;
And, by my feith, he wol my wrecched heve hem,
That in myn herte wol I dwelle hem-ward:
And, lo, here the wys of him-self, I rede,
That false god of hevene be my worship!
And I shal with you two been as yemen goon.'
That hir goode swowninge for to stonde,
This fals he took agayn, and swoughte herde;—
'I werk noght,' quod he, 'by my feith,
I wol my litel body be so dere,
That I shal been a pye in-feith, as wel
As ye;) the false god, dere god!
A! false god, false god! how may ye smyte?
Mochiteth nat, er thou goost to hevene,'
Seyde this false god, 'ye up stirken in the sky!
What? what is this, and why wryte thee?
What is the cause, and whiche god forsook of thee,
That thou, false god, in his owene dere,
Seyde thou thy fals aweyf as if it were truth?
Mochiteth nat, thise dere god forsook of thee;
Thou seist thou what is the matter, and heeldeth thee!
Much as I shal tellen al the cause why.
`

#### 10000 Steps (using novel generation script)
`Balade that Chaucier made.


This world is now ful tikel, sikerly;
We breken it al to-morn as a shadwe;
And ech of us bicomen otheres brother,
And ech of us spinners, and we xens,
And gerlandes, bothe day and night,
And wayter pater-nails, and earthes
In general, so that ther shal bityde.
And whan that we hadde a certeyn day
Hem Clens were y-voyded, so wormes hede,
And many a mery hir salte teres speke,
Til day bigan to springe was accorde.
And in his herte somwhat he solas,
Til day bigan to springe grete mirours raines
In al thatl we can demen by our wit.
Tho bigan he day by his wonder-teres
The whyte sheep, that Wool in wizard was.)
Tho bigan he day by his sleighte
The whyte hare, and by the holy confort
The man, charles, and eek the halfway prince,
Conforten, and voyded hir together.
Thus started is this lineage;
Men may devyne and devyse al conseil.







And so bifel, that in the toun of Rome,
The statue of the mother of god,
With bowe in honde, as he had seyn,
And arwes in honured harnesses,
And eek hir lemman, and hir posse,
And alle hir rythes and hir fayres,
And how they shul seyn "allas!"
Now changes heer of ensamples many oon,
And many a newe markisesse,
That shapen with-outen any recche or stryf.
Thus quyte Iogenes, olde wronges,
Of ech estaat and rudenesse,
And of lichets, and of avoutryes,
Of regnes, of regnes duetees,
Of honurable wordes, and of charitablenesse,
Of markisesse, and of baudes po,
Of contractes, and of werkinges,
Of preestes, and of procuringes,
Of chirche-reves, and of chirche-pieces,
Of chirche-spe, and of chirche-trees,
Of contractes, and of werkinges,
And eek of other art of instrumentes,
And in what manere, by whiche instruments,
If any persone order, or any wight,
To doon a thing, or elles make another.
It is hard to seken of trouthe and gladnesse;
Boras, brydel, brydel-leves, and cote-armures;
Keminations, and kemes, and cloothes, and torets,
And eek the appendices and the foot-long stele;
The shap, ther- as is the shadwe of deeth;
The eres of mortels, and the eres of eels;
Poudres, and eek the foulnesse of it,
That dreynte cutteth cisouns
After gif, and rots, and furnishins;
toggle, and turnips, and cloothes of lye;
Cots, and dukes, and bateles ful of plate;
Reliks, and chiknes, and saveles,
And eek the guttes caroles, and the rectels,
That drenchen in the roof of the pyrie,
Into the moone, and the dores, and the spares,
And the mannes shoo, it is so lowe;
Noon hyer was the faile, ne noght the lowe.
Beth war, I pray yow hertely; for if she fare,
She shal wel knowe that right as she,
Sin that it is the beste reed,
She shal reherce wel half a gode ende.
And if so be the game wente aright,
She shal seye right sooth, what that herde is.
For wel she seith, right as she that misconceyveth,
She that misconceyveth som freend or two,
And cheats hir-self, she cI crye 'allas! that I was so longe ordained
To long apprenticeship in sinne and in meschance!'
Ther I was bred, taughte me that I be old
To sone rype, and bad my-self for to knete!
Yet hadde I never hard enough, certayn,
To garden in the morweninge,
For to goon to the nexte citee.
I have ther-with to done, I may nat longe tarie,
To garden up-on the grounde,
And maken of our covent firmes three.
And therfore, sire, trusteth right longe in my tonge,
That I shal doon, I wol rewe on Thursday.
And wel I woot, Sathanas, if I have it in my might,
I wol shal make hem good men to venge thee.'

`


### Setup
All python files are in the `scripts` folder.

The contents in the `files` folder are all you need to get going with generating, but if you want to do a similar project on a different corpus, I’ve included a `clean.py` script that eliminates a number of common formats for footnotes or editor’s notes in Project Gutenberg. Simply run `python clean.py (path_to_your_file.txt)` to output a cleaned version. Right now, it just contains a number of variables representing different common patterns, so you may want to edit and pick and choose to your needs - don’t accidentally delete text that’s meant to be in  your corpus!

Once your corpus is ready, I’ve modified the sample code from [minimaxir’s gpt-2-simple package](https://github.com/minimaxir/gpt-2-simple) so you can plug and play it.

Simply run `python retrain.py -m=(your preferred model, right now options are “124M” and “355M) -f=”path_to_your_file” -s=(optional number of steps you want to retrain for)`. Alternately, if you don’t have access to a GPU/don’t want to wait to train, I’ve kindly used up all my git large file storage to include a 1000 step training in the checkpoints folder. This one has some anachronisms (it seems to make a lot of winky faces, for example), but still does a halfway decent job.

Once you’ve retrained your model, you can generate a 50,000ish word text using `python novel_gen.py -d=“file_to_write_to" -c=“checkpoint_location" -t=“model temperature"`. This script pulls a sentence from the original text as a seed, then generates a few paragraphs from GPT-2, gets a character count from the generated text, moves to that point in the original, and uses the nearest sentence as a seed for the next generation until it hits 50,000 words. You can see some sample output at different steps in the `samples` folder, and a few different novels in `texts`.

**TODOS**
- [] turn all `clean.py` vars into command line options
- [x] script to actually generate novel - need to mess with seeding, temp and length to see best mix of structure/randomness
