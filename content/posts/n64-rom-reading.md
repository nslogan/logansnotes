Title: Nintendo 64 ROM Reading
Date: 2020-04-20
Category: n64

[WaveDrom](https://github.com/wavedrom/wavedrom)

<script type="WaveDrom">
{signal: [
  {name: 'ALE_L', wave: '0.1.0.........',
                  node: '..a.c.........' },
  {name: 'ALE_H', wave: '1..0.........1',
                  node: '...b.....ij..h' },
  {name: 'RD',    wave: '1......0.10.1.',
                  node: '.......d.ef.g.' }
],
 edge: [
 	'c<-|->d 1.04 us',
    'd<->e 300 ns',
    'e-i','j-f','i<->j 64 ns',
    'g<-|->h 64 ns'
 ] 
}
</script>

![Alt](https://svg.wavedrom.com/github/nslogan/logansnotes/master/content/posts/waves/n64-rom-single-read.json5)

<script>
	WaveDrom.ProcessAll();
</script>

---

Soon...[^1]

[^1]: A cool reference

Demonstrating use of [footnotes extension](https://python-markdown.github.io/extensions/footnotes/)

### References

Footnotes are place at the end if the `PLACE_MARKER` text isn't found.

///Footnotes Go Here///
