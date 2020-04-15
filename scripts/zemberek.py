import re
import nltk
from nltk.tokenize import regexp_tokenize
import os
from os.path import join
from typing import List
from jpype import JClass, JString, getDefaultJVMPath, startJVM, java
import jpype
from complaint.models import Complaint

def run(comp, tit):
    

    ZEMBEREK_PATH: str = join('C:\\Users\\melih\\Desktop\\DjangoProjects\\automation\\zemberek','zemberek-full.jar')
        

    if not jpype.isJVMStarted():
        startJVM(getDefaultJVMPath(),'-ea',f'-Djava.class.path={ZEMBEREK_PATH}',convertStrings=False)

    TurkishMorphology: JClass = JClass('zemberek.morphology.TurkishMorphology')
    WordAnalysis: JClass = JClass('zemberek.morphology.analysis.WordAnalysis')
    morpho: TurkishMorphology = TurkishMorphology.createWithDefaults()


    
    sikayet_oneri = comp
    kelimeler = sikayet_oneri
    analysis: java.util.ArrayList = (morpho.analyzeAndDisambiguate(kelimeler).bestAnalysis())
    pos: List[str] = []
        
    for i, analysis in enumerate(analysis, start=1):
        f'\nAnalysis {i}: {analysis}',
        f'\nPrimary POS {i}: {analysis.getPos()}'
        f'\nPrimary POS (Short Form) {i}: {analysis.getPos().shortForm}'       
        pos.append(f'{str(analysis.getLemmas()[0])}')
        
    def deleteSymbol(allWords):
        corpus = []
        for i in range(len(allWords)):
            review = re.sub(r'\W', ' ', str(allWords[i]))
            review = re.sub(r'\s\w\s', ' ', review)
            review = re.sub(r'^\w\s', ' ', review)
            review = re.sub(r'\s+', ' ', review)
            review = review.strip()
            if len(review):
                corpus.append(review)
            
        return corpus

    allWords = deleteSymbol(pos)

    """
    def wordtokenize(sikayet_oneri):
        text=nltk.word_tokenize(sikayet_oneri)
        
        return text
    """

    def twograms():
        twograms_list = []
        bigram_fd = nltk.FreqDist(nltk.ngrams(allWords,2))
        mc=bigram_fd.most_common()

        for i in mc:
            temp=regexp_tokenize(str(i),'[\w]+')
            twograms_list.append(temp)
        
        return twograms_list    

    def threegrams():
        threegrams_list = []
        bigram_fd = nltk.FreqDist(nltk.ngrams(allWords,3))
        mc=bigram_fd.most_common()

        for i in mc:
            threegrams_list.append(i)

        return threegrams_list
    
    
    fileName = tit.replace(" ","_")

    with open(fileName+"_twograms.txt", "w") as f:
        two = twograms()
        for w in two:
            f.write(str(w)+"\n")

    with open(fileName+"_threegrams.txt", "w") as f:
        three = threegrams()
        for w in three:
            f.write(str(w)+"\n")

    








