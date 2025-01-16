# Voice Typing System: Preserving Raw Speech 

A minimalist approach for capturing every nuance of spoken language. Filler words, stutters, and accents stay intact. No fancy punctuation. No TTS loop. No external normalisation.

---

## Concept Overview
- **Raw Transcription**: Record speech exactly as it is uttered.  
- **Phonetic Mapping**: Align audio with phonetic units.  
- **Minimal Language Model**: Fine-tune a small transformer (GPT-2 or T5) on a tiny, carefully curated dataset.

---

## Key Features
1. **Direct Transcription**  
   - Keeps every “um,” “uh,” and repetition.  
   - Avoids system-enforced punctuation or grammar.
2. **User-Specific Adaptation**  
   - Focuses on personal recordings.  
   - Learns quirks and local accent over time.
3. **Manual Correction**  
   - The user reviews transcripts.  
   - Corrections guide further refinements.

---

## Implementation Plan

1. **Phonetic Model**
   - Use Montreal Forced Aligner or CMU Sphinx.  
   - Disable or remove default text cleaning.  
   - Produce phone-level segments.

2. **Minimal Fine-Tuning**
   - Gather a small collection (~1,000–5,000 examples) of your own recorded speech.  
   - Align each phone sequence with the exact textual variant (including stammers).  
   - Fine-tune GPT-2 or T5 on these mappings.  

3. **Real-Time Pipeline**
   - Feed raw audio into the phonetic model.  
   - Pass the resulting phone sequence to the fine-tuned model.  
   - Output text that mirrors your speech patterns.  

4. **Ongoing Correction**
   - Collect user edits as training data.  
   - Occasionally re-fine-tune to maintain accuracy.

---

## Timeline

| Week | Task                                                 |
|-----:|:-----------------------------------------------------|
| 1–2  | Install and test phonetic software on small samples. |
| 3–4  | Record user speech (curated examples).               |
| 5–6  | Fine-tune GPT-2 or T5; evaluate word/phone error rate. |
| 7–8  | Integrate real-time transcription; incorporate corrections. |
| 9+   | Refine model, gather fresh data, iterate.            |

---

## Tools and Resources

- **Forced Alignment**  
  - [Montreal Forced Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner)  
  - [CMU Sphinx](https://cmusphinx.github.io/)  
- **Language Model Fine-Tuning**  
  - [Hugging Face Transformers](https://github.com/huggingface/transformers)  
  - Pre-trained GPT-2 or T5  
- **Audio Recording**  
  - Any basic tool (e.g. Audacity or Python’s `pyaudio`)  

---

## Next Steps
1. **Start Small**  
   - Try 50–100 lines to confirm everything works.  
2. **Refine**  
   - Gradually expand the dataset.  
   - Turn off normalisers in alignment tools.  
3. **Evaluate**  
   - Track word/phone error rates.  
   - Identify repeated mistakes (e.g., homophones).  

---

## Further Reading
- Sacks, H., Schegloff, E.A., & Jefferson, G. (1974). *A simplest systematics for the organization of turn-taking for conversation.*  
- Clark, H. H., & Fox Tree, J. E. (2002). “Using uh and um in spontaneous speech.” *Cognition*, 84(1), 73–111.  
- [Praat](http://www.fon.hum.uva.nl/praat/)  
- [ELAN](https://archive.mpi.nl/tla/elan)  
```
