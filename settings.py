from sequence import Sequence
import pygame

seq4 = Sequence(name="Sequence 4", playlist=["./samples/jingle2.wav",
                                             "./samples/jingle2.wav",
                                             "./samples/jingle2.wav",
                                             "./samples/jingle2.wav",
                                             "./samples/jingle2.wav"],
                                             next_sequence=None)
seq3 = Sequence(name="Sequence 3", playlist=["./samples/jingle2.wav",
                                             "./samples/badswap.wav",
                                             "./samples/jingle2.wav",
                                             "./samples/badswap.wav"],
                                             next_sequence=seq4)
seq2 = Sequence(name="Sequence 2", playlist=["./samples/badswap.wav",
                                             "./samples/badswap.wav",
                                             "./samples/match0.wav",
                                             "./samples/badswap.wav"],
                                             next_sequence=seq3)
seq1 = Sequence(name="Sequence 1", playlist=["./samples/jingle_intro.wav",
                                             "./samples/match0.wav",
                                             "./samples/jingle2.wav",
                                             "./samples/match1.wav",
                                             "./samples/jingle3.wav"],
                                             next_sequence=seq2)

sequences = {
    # touche clavier : sample
    pygame.K_1 : seq1,
    pygame.K_2 : seq2,
    pygame.K_3 : seq3,
    pygame.K_4 : seq4,
}
