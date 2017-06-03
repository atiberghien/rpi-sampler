from sequence import Sequence
import pygame


seq4 = Sequence(name="Sequence 4", playlist=["./samples/1G3foin.wav",
                                             "./samples/2G3champi.wav",
                                             "./samples/3G3pre.wav",
                                             "./samples/4G3lac.wav",
                                             "./samples/5G3refuge.wav",
                                             "./samples/6G3etoile.wav",
                                             "./samples/7G3gel.wav",
                                             "./samples/8G3neige.wav",
                                             "./samples/9G3musique.wav",
                                             "./samples/10G3paroles.wav"],
                                             next_sequence=None)


seq3 = Sequence(name="Sequence 3", playlist=["./samples/1G4poursuivre.wav",
                                             "./samples/2G4plaisir.wav",
                                             "./samples/3G4aventure.wav",
                                             "./samples/4G4donner.wav",
                                             "./samples/5G4imaginer.wav",
                                             "./samples/6G4accepter.wav",
                                             "./samples/7G4espoir.wav",
                                             "./samples/8G4decouvrir.wav",
                                             "./samples/9G4horizon.wav",
                                             "./samples/10G4etre.wav"],
                                             next_sequence=seq4)


seq2 = Sequence(name="Sequence 2", playlist=["./samples/1G2quijesuis.wav",
                                            "./samples/2G2sommesnous.wav",
                                            "./samples/3G2disons.wav",
                                            "./samples/4G2venons.wav",
                                            "./samples/5G2cherchons.wav",
                                            "./samples/6G2etrela.wav",
                                            "./samples/7G2chatel.wav",
                                            "./samples/8G2meteo.wav",
                                            "./samples/9G2rues.wav",
                                            "./samples/10G2montaiguille.wav"],
                                             next_sequence=seq3)


seq1 = Sequence(name="Sequence 1", playlist=["./samples/1G1partage.wav",
                                             "./samples/2G1sourire.wav",
                                             "./samples/3G1rencontre.wav",
                                             "./samples/4G1courir.wav",
                                             "./samples/5G1rever.wav",
                                             "./samples/6G1croire.wav",
                                             "./samples/7G1desir.wav",
                                             "./samples/8G1creer.wav",
                                             "./samples/9G1paysage.wav",
                                             "./samples/10G1vivre.wav"],
                                             next_sequence=seq2)


sequences = {
    # touche clavier : sample
    pygame.K_1 : seq1,
    pygame.K_2 : seq2,
    pygame.K_3 : seq3,
    pygame.K_4 : seq4,
}
