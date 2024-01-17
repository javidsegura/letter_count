def func(x):
      clean_x = x.split()
      results = set()
      for i in clean_x:
            z = clean_x.count(i)
            results.add(f"{i}:{z}")
      return results

print(func('When the ancient Greeks adopted the alphabet, they had no use for a letter to represent the glottal stop—the consonant sound that the letter denoted in Phoenician and other Semitic languages, and that was the first phoneme of the Phoenician pronunciation of the letter—so they used their version of the sign to represent the vowel /a/, and called it by the similar name of alpha. In the earliest Greek inscriptions after the Greek Dark Ages, dating to the eighth century BC, the letter rests upon its side, but in the Greek alphabet of later times it generally resembles the modern capital letter, although many local varieties can be distinguished by the shortening of one leg, or by the angle at which the cross line is set. The Etruscans brought the Greek alphabet to their civilization in the Italian Peninsula and left the letter unchanged. The Romans later adopted the Etruscan alphabet to write the Latin language, and the resulting letter was preserved in the Latin alphabet that would come to be used to write many languages, including English.'))
