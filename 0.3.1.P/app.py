from flask import Flask, render_template, Response
import cv2
import mediapipe as mp

app = Flask(__name__)

# Inicialização do Mediapipe e captura de vídeo
video = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils
last_libra = None

# Variáveis para armazenar os pontos das mãos
point_0 = None
point_1 = None
point_2 = None
point_3 = None
point_4 = None
point_5 = None
point_6 = None
point_7 = None
point_8 = None
point_9 = None
point_10 = None
point_11 = None
point_12 = None
point_13 = None
point_14 = None
point_15 = None
point_16 = None
point_17 = None
point_18 = None
point_19 = None
point_20 = None

def detectar_libra(pontos):
    """
    Função para detectar as letras A, B e C com base nos pontos das mãos
    e usando variáveis de movimento.
    """

    if len(pontos) > 20:
        global point_0, point_1, point_2, point_3, point_4
        global point_5, point_6, point_7, point_8, point_9
        global point_10, point_11, point_12, point_13, point_14
        global point_15, point_16, point_17, point_18, point_19, point_20

        # Atualiza as variáveis de movimento com os pontos da mão detectada
    if (  #  Letra A
                pontos[8][1] > pontos[5][1] and
                pontos[12][1] > pontos[9][1] and
                pontos[16][1] > pontos[13][1] and
                pontos[20][1] > pontos[17][1] and
                pontos[4][1] < pontos[5][1] and

                pontos[4][0] > pontos[6][0]
            ):
                return "A"


    if (  #  Letra B
                pontos[8][1] < pontos[7][1] and
                pontos[12][1] < pontos[11][1] and
                pontos[16][1] < pontos[15][1] and
                pontos[20][1] < pontos[19][1] and
                pontos[4][0] < pontos[1][0] and
                pontos[4][2] < pontos[13][2]
            ):
                return "B"


    if  (  #  Letra C
                pontos[8][2] > pontos[12][2] and
                pontos[12][2] > pontos[16][2] and
                pontos[16][2] > pontos[20][2] and
                pontos[4][0] > pontos[3][0] and
                pontos[4][2] > pontos[20][2] and
                pontos[4][1] > pontos[8][1] and
                pontos[17][2] < pontos[5][2] and
                pontos[17][2] < pontos[13][2] and
                pontos[17][2] < pontos[9][2] and
                pontos[17][2] < pontos[4][2] and
                pontos[4][1] > pontos[8][1] and
                pontos[4][1] > pontos[16][1] and
                pontos[4][1] > pontos[18][1] and
                pontos[4][1] > pontos[19][1] and
                pontos[4][1] > pontos[20][1] and
                pontos[4][1] > pontos[14][1] and
                pontos[4][1] > pontos[15][1] and
                pontos[4][1] > pontos[16][1] and
                pontos[4][1] > pontos[10][1] and
                pontos[4][1] > pontos[11][1] and
                pontos[4][1] > pontos[12][1] and
                pontos[4][1] > pontos[6][1] and
                pontos[4][1] > pontos[7][1] and
                pontos[4][1] > pontos[8][1] and
                pontos[20][1] < pontos[18][1]
            ):
                return "C"


    if (  #  Letra D
                pontos[8][1] < pontos[10][1] and
                pontos[12][1] > pontos[10][1] and
                pontos[16][1] > pontos[14][1] and
                pontos[20][1] > pontos[18][1] and
                pontos[4][1] < pontos[16][1] and
                pontos[4][1] > pontos[10][1] and
                pontos[4][1] < pontos[3][1] and
                pontos[4][1] < pontos[2][1] and
                pontos[4][0] < pontos[3][0] and
                pontos[12][1] < pontos[3][1] and
                pontos[11][1] < pontos[3][1] and
                pontos[11][1] < pontos[9][1]
            ):
                return "D"


    if (  # Letra E
                pontos[8][1] < pontos[5][1] and
                pontos[20][1] > pontos[19][1] and
                pontos[16][1] > pontos[15][1] and
                pontos[12][1] > pontos[11][1] and
                pontos[4][1] > pontos[5][1] and
                pontos[4][2] < pontos[2][2] and
                pontos[4][0] < pontos[3][0] and
                pontos[8][1] > pontos[7][1] and
                pontos[20][1] > pontos[19][1] and
                pontos[16][1] > pontos[15][1] and
                pontos[12][1] > pontos[11][1]
            ):
                return "E"


    if ( # Letra F
                # pontos[4][2] > pontos[0][2] and
                # pontos[4][2] > pontos[1][2] and
                # pontos[4][2] > pontos[2][2] and
                # pontos[4][2] > pontos[3][2] and
                # pontos[4][2] > pontos[7][2] and
                pontos[6][1] > pontos[10][1] and
                pontos[6][1] > pontos[14][1] and
                pontos[6][1] > pontos[19][1] and
                pontos[7][1] > pontos[10][1] and
                pontos[7][1] > pontos[14][1] and
                pontos[7][1] > pontos[19][1] and
                pontos[8][1] > pontos[10][1] and
                pontos[8][1] > pontos[14][1] and
                pontos[8][1] > pontos[19][1] and
                pontos[20][1] > pontos[15][1]
            ):
                return "F"


    if ( # Letra G
                pontos[8][1] < pontos[0][1] and
                pontos[8][1] < pontos[1][1] and
                pontos[8][1] < pontos[2][1] and
                pontos[8][1] < pontos[3][1] and
                pontos[8][1] < pontos[5][1] and
                pontos[8][1] < pontos[6][1] and
                pontos[8][1] < pontos[7][1] and
                pontos[8][1] < pontos[9][1] and
                pontos[8][1] < pontos[10][1] and
                pontos[8][1] < pontos[11][1] and
                pontos[8][1] < pontos[12][1] and
                pontos[8][1] < pontos[13][1] and
                pontos[8][1] < pontos[14][1] and
                pontos[8][1] < pontos[15][1] and
                pontos[8][1] < pontos[16][1] and
                pontos[8][1] < pontos[17][1] and
                pontos[8][1] < pontos[18][1] and
                pontos[8][1] < pontos[19][1] and
                pontos[8][1] < pontos[20][1] and

                pontos[7][1] < pontos[0][1] and
                pontos[7][1] < pontos[1][1] and
                pontos[7][1] < pontos[2][1] and
                pontos[7][1] < pontos[3][1] and
                pontos[7][1] < pontos[5][1] and
                pontos[7][1] < pontos[6][1] and
                pontos[7][1] > pontos[8][1] and
                pontos[7][1] < pontos[9][1] and
                pontos[7][1] < pontos[10][1] and
                pontos[7][1] < pontos[11][1] and
                pontos[7][1] < pontos[12][1] and
                pontos[7][1] < pontos[13][1] and
                pontos[7][1] < pontos[14][1] and
                pontos[7][1] < pontos[15][1] and
                pontos[7][1] < pontos[16][1] and
                pontos[7][1] < pontos[17][1] and
                pontos[7][1] < pontos[18][1] and
                pontos[7][1] < pontos[19][1] and
                pontos[7][1] < pontos[20][1] and

                pontos[6][1] < pontos[0][1] and
                pontos[6][1] < pontos[1][1] and
                pontos[6][1] < pontos[2][1] and
                pontos[6][1] < pontos[3][1] and
                pontos[6][1] < pontos[5][1] and
                pontos[6][1] > pontos[7][1] and
                pontos[6][1] > pontos[8][1] and
                pontos[6][1] < pontos[9][1] and
                pontos[6][1] < pontos[10][1] and
                pontos[6][1] < pontos[11][1] and
                pontos[6][1] < pontos[12][1] and
                pontos[6][1] < pontos[13][1] and
                pontos[6][1] < pontos[14][1] and
                pontos[6][1] < pontos[15][1] and
                pontos[6][1] < pontos[16][1] and
                pontos[6][1] < pontos[17][1] and
                pontos[6][1] < pontos[18][1] and
                pontos[6][1] < pontos[19][1] and
                pontos[6][1] < pontos[20][1] and

                pontos[4][1] < pontos[1][1] and
                pontos[4][1] < pontos[2][1] and
                pontos[4][1] < pontos[3][1] and
                pontos[4][1] < pontos[5][1] and
                pontos[4][1] > pontos[6][1] and
                pontos[4][1] > pontos[7][1] and
                pontos[4][1] > pontos[8][1] and
                pontos[4][1] < pontos[9][1] and
                pontos[4][1] < pontos[10][1] and
                pontos[4][1] < pontos[11][1] and
                pontos[4][1] < pontos[12][1] and
                pontos[4][1] < pontos[13][1] and
                pontos[4][1] < pontos[14][1] and
                pontos[4][1] < pontos[15][1] and
                pontos[4][1] < pontos[16][1] and
                pontos[4][1] < pontos[17][1] and
                pontos[4][1] < pontos[18][1] and
                pontos[4][1] < pontos[19][1] and
                pontos[4][1] < pontos[20][1] and
                pontos[4][2] < pontos[6][2] and
                pontos[4][0] > pontos[6][0] and

                pontos[20][1] > pontos[17][1] and
                pontos[20][1] > pontos[13][1] and
                pontos[20][1] > pontos[9][1] and
                pontos[20][1] > pontos[5][1] and
                pontos[16][1] > pontos[17][1] and
                pontos[16][1] > pontos[13][1] and
                pontos[16][1] > pontos[9][1] and
                pontos[16][1] > pontos[5][1] and
                pontos[12][1] > pontos[17][1] and
                pontos[12][1] > pontos[13][1] and
                pontos[12][1] > pontos[9][1] and
                pontos[12][1] > pontos[5][1] and
                pontos[19][1] > pontos[17][1] and
                pontos[19][1] > pontos[13][1] and
                pontos[19][1] > pontos[9][1] and
                pontos[19][1] > pontos[5][1] and
                pontos[15][1] > pontos[17][1] and
                pontos[15][1] > pontos[13][1] and
                pontos[15][1] > pontos[9][1] and
                pontos[15][1] > pontos[5][1] and
                pontos[11][1] > pontos[17][1] and
                pontos[11][1] > pontos[13][1] and
                pontos[11][1] > pontos[9][1] and
                pontos[11][1] > pontos[5][1] and

                pontos[11][1] > pontos[14][1] and
                pontos[12][1] > pontos[14][1] and
                pontos[11][0] < pontos[4][0]

            ):
                return "G"


    if (  # Letra I

                # Todos os pontos abaixo, com exceção de 14, 10, 6, 20, 4
                pontos[20][1] < pontos[0][1] and
                pontos[20][1] < pontos[1][1] and
                pontos[20][1] < pontos[2][1] and
                pontos[20][1] < pontos[3][1] and
                pontos[20][1] < pontos[5][1] and
                pontos[20][1] < pontos[7][1] and
                pontos[20][1] < pontos[8][1] and
                pontos[20][1] < pontos[9][1] and
                pontos[20][1] < pontos[11][1] and
                pontos[20][1] < pontos[12][1] and
                pontos[20][1] < pontos[13][1] and
                pontos[20][1] < pontos[15][1] and
                pontos[20][1] < pontos[16][1] and
                pontos[20][1] < pontos[17][1] and
                pontos[20][1] < pontos[18][1] and
                pontos[20][1] < pontos[19][1] and

                # Todos os pontos abaixo, com exceção de 14, 10, 6, 20, 19, 4
                pontos[19][1] < pontos[0][1] and
                pontos[19][1] < pontos[1][1] and
                pontos[19][1] < pontos[2][1] and
                pontos[19][1] < pontos[3][1] and
                pontos[19][1] < pontos[5][1] and
                pontos[19][1] < pontos[7][1] and
                pontos[19][1] < pontos[8][1] and
                pontos[19][1] < pontos[9][1] and
                pontos[19][1] < pontos[11][1] and
                pontos[19][1] < pontos[12][1] and
                pontos[19][1] < pontos[13][1] and
                pontos[19][1] < pontos[15][1] and
                pontos[19][1] < pontos[16][1] and
                pontos[19][1] < pontos[17][1] and
                pontos[19][1] < pontos[18][1] and

                # Todos os pontos abaixo, com exceção de 14, 10, 6, 20, 19, 18, 4
                pontos[18][1] < pontos[0][1] and
                pontos[18][1] < pontos[1][1] and
                pontos[18][1] < pontos[2][1] and
                pontos[18][1] < pontos[3][1] and
                pontos[18][1] < pontos[5][1] and
                pontos[18][1] < pontos[7][1] and
                pontos[18][1] < pontos[8][1] and
                pontos[18][1] < pontos[9][1] and
                pontos[18][1] < pontos[11][1] and
                pontos[18][1] < pontos[12][1] and
                pontos[18][1] < pontos[13][1] and
                pontos[18][1] < pontos[15][1] and
                pontos[18][1] < pontos[16][1] and
                pontos[18][1] < pontos[17][1] and

                pontos[4][0] < pontos[3][0]
            ):
                return "I"

    if (  # Letra H
                point_8 != None and
                point_12 != None
            ):
                X_move_8 = pontos[8][0] - point_8[0]
                X_move_12 = pontos[12][0] - point_12[0]
                if (
                    X_move_8 > 5 and
                    X_move_12 > 5 and
                    pontos[8][1] < pontos[7][1] and
                    pontos[12][1] < pontos[11][1]
                ):
                    # Redefinição dos pontos das mãos (para a detecção de movimento)
                    point_0 = None
                    point_1 = None
                    point_2 = None
                    point_3 = None
                    point_4 = None
                    point_5 = None
                    point_6 = None
                    point_7 = None
                    point_8 = None
                    point_9 = None
                    point_10 = None
                    point_11 = None
                    point_12 = None
                    point_13 = None
                    point_14 = None
                    point_15 = None
                    point_16 = None
                    point_17 = None
                    point_18 = None
                    point_19 = None
                    point_20 = None
                    if last_libra != "H":
                        last_libra = "H"
                        return "H"
                    else:
                        return "H"



    if ( # Letra J
                point_8 != None and
                point_12 != None and
                point_0 != None
            ):
                X_move_8 = pontos[8][0] - point_8[0]
                X_move_12 = pontos[12][0] - point_12[0]
                Y_move_8 = pontos[8][1] - point_8[1]
                Y_move_12 = pontos[12][1] - point_12[1]

                if (
                        X_move_8 > 5 and
                        X_move_12 > 5 and
                        Y_move_8 > 5 and
                        Y_move_12 > 5 and
                        pontos[8][1] > pontos[7][1] and  # Dedo mindinho mais baixo que a base da palma
                        pontos[12][1] > pontos[11][1] and  # Dedo indicador mais baixo que a base da palma
                        pontos[0][1] > pontos[1][1] and  # Palma voltada para baixo
                        pontos[0][1] > pontos[2][1]
                ):
                    # Redefinição dos pontos das mãos (para a detecção de movimento)
                    point_0 = None
                    point_1 = None
                    point_2 = None
                    point_3 = None
                    point_4 = None
                    point_5 = None
                    point_6 = None
                    point_7 = None
                    point_8 = None
                    point_9 = None
                    point_10 = None
                    point_11 = None
                    point_12 = None
                    point_13 = None
                    point_14 = None
                    point_15 = None
                    point_16 = None
                    point_17 = None
                    point_18 = None
                    point_19 = None
                    point_20 = None
                    if last_libra != "J":
                        last_libra = "J"
                        return "J"
                    else:
                        return "J"


    if (  # Letra K
                    point_8 != None and
                    point_12 != None
            ):
                X_move_8 = pontos[8][0] - point_8[0]
                X_move_12 = pontos[12][0] - point_12[0]
                if (
                        X_move_8 < -5 and
                        X_move_12 < -5 and
                        pontos[8][1] < pontos[7][1] and
                        pontos[12][1] < pontos[11][1]
                ):
                    # Redefinição dos pontos das mãos (para a detecção de movimento)
                    point_0 = None
                    point_1 = None
                    point_2 = None
                    point_3 = None
                    point_4 = None
                    point_5 = None
                    point_6 = None
                    point_7 = None
                    point_8 = None
                    point_9 = None
                    point_10 = None
                    point_11 = None
                    point_12 = None
                    point_13 = None
                    point_14 = None
                    point_15 = None
                    point_16 = None
                    point_17 = None
                    point_18 = None
                    point_19 = None
                    point_20 = None
                    if last_libra != "K":
                        last_libra = "K"
                        return "K"
                    else:
                        return "K"


    if ( # Letra L
                pontos[8][1] < pontos[0][1] and
                pontos[8][1] < pontos[1][1] and
                pontos[8][1] < pontos[2][1] and
                pontos[8][1] < pontos[3][1] and
                pontos[8][1] < pontos[4][1] and
                pontos[8][1] < pontos[5][1] and
                pontos[8][1] < pontos[6][1] and
                pontos[8][1] < pontos[7][1] and
                pontos[8][1] < pontos[9][1] and
                pontos[8][1] < pontos[10][1] and
                pontos[8][1] < pontos[11][1] and
                pontos[8][1] < pontos[12][1] and
                pontos[8][1] < pontos[13][1] and
                pontos[8][1] < pontos[14][1] and
                pontos[8][1] < pontos[15][1] and
                pontos[8][1] < pontos[16][1] and
                pontos[8][1] < pontos[17][1] and
                pontos[8][1] < pontos[18][1] and
                pontos[8][1] < pontos[19][1] and
                pontos[8][1] < pontos[20][1] and

                pontos[7][1] < pontos[0][1] and
                pontos[7][1] < pontos[1][1] and
                pontos[7][1] < pontos[2][1] and
                pontos[7][1] < pontos[3][1] and
                pontos[7][1] < pontos[4][1] and
                pontos[7][1] < pontos[5][1] and
                pontos[7][1] < pontos[6][1] and
                pontos[7][1] > pontos[8][1] and
                pontos[7][1] < pontos[9][1] and
                pontos[7][1] < pontos[10][1] and
                pontos[7][1] < pontos[11][1] and
                pontos[7][1] < pontos[12][1] and
                pontos[7][1] < pontos[13][1] and
                pontos[7][1] < pontos[14][1] and
                pontos[7][1] < pontos[15][1] and
                pontos[7][1] < pontos[16][1] and
                pontos[7][1] < pontos[17][1] and
                pontos[7][1] < pontos[18][1] and
                pontos[7][1] < pontos[19][1] and
                pontos[7][1] < pontos[20][1] and

                pontos[6][1] < pontos[0][1] and
                pontos[6][1] < pontos[1][1] and
                pontos[6][1] < pontos[2][1] and
                pontos[6][1] < pontos[3][1] and
                pontos[6][1] < pontos[4][1] and
                pontos[6][1] < pontos[5][1] and
                pontos[6][1] > pontos[7][1] and
                pontos[6][1] > pontos[8][1] and
                pontos[6][1] < pontos[9][1] and
                pontos[6][1] < pontos[10][1] and
                pontos[6][1] < pontos[11][1] and
                pontos[6][1] < pontos[12][1] and
                pontos[6][1] < pontos[13][1] and
                pontos[6][1] < pontos[14][1] and
                pontos[6][1] < pontos[15][1] and
                pontos[6][1] < pontos[16][1] and
                pontos[6][1] < pontos[17][1] and
                pontos[6][1] < pontos[18][1] and
                pontos[6][1] < pontos[19][1] and
                pontos[6][1] < pontos[20][1] and

                pontos[4][0] > pontos[0][0] and
                pontos[4][0] > pontos[1][0] and
                pontos[4][0] > pontos[2][0] and
                pontos[4][0] > pontos[3][0] and
                pontos[4][0] > pontos[5][0] and
                pontos[4][0] > pontos[7][0] and
                pontos[4][0] > pontos[8][0] and
                pontos[4][0] > pontos[9][0] and
                pontos[4][0] > pontos[10][0] and
                pontos[4][0] > pontos[11][0] and
                pontos[4][0] > pontos[12][0] and
                pontos[4][0] > pontos[13][0] and
                pontos[4][0] > pontos[14][0] and
                pontos[4][0] > pontos[15][0] and
                pontos[4][0] > pontos[16][0] and
                pontos[4][0] > pontos[17][0] and
                pontos[4][0] > pontos[18][0] and
                pontos[4][0] > pontos[19][0] and
                pontos[4][0] > pontos[20][0] and

                pontos[3][0] > pontos[0][0] and
                pontos[3][0] > pontos[1][0] and
                pontos[3][0] > pontos[2][0] and
                pontos[3][0] > pontos[5][0] and
                pontos[3][0] > pontos[9][0] and
                pontos[3][0] > pontos[10][0] and
                pontos[3][0] > pontos[11][0] and
                pontos[3][0] > pontos[12][0] and
                pontos[3][0] > pontos[13][0] and
                pontos[3][0] > pontos[14][0] and
                pontos[3][0] > pontos[15][0] and
                pontos[3][0] > pontos[16][0] and
                pontos[3][0] > pontos[17][0] and
                pontos[3][0] > pontos[18][0] and
                pontos[3][0] > pontos[19][0] and
                pontos[3][0] > pontos[20][0]


            ):
                return "L"


    if ( # Letra M
                pontos[8][1] > pontos[0][1] and
                pontos[8][1] > pontos[1][1] and
                pontos[8][1] > pontos[2][1] and
                pontos[8][1] > pontos[3][1] and
                pontos[8][1] > pontos[4][1] and
                pontos[8][1] > pontos[5][1] and
                pontos[8][1] > pontos[6][1] and
                pontos[8][1] > pontos[7][1] and
                pontos[8][1] > pontos[9][1] and
                pontos[8][1] > pontos[10][1] and
                pontos[8][1] > pontos[11][1] and
                pontos[8][1] > pontos[13][1] and
                pontos[8][1] > pontos[14][1] and
                pontos[8][1] > pontos[15][1] and
                pontos[8][1] > pontos[17][1] and
                pontos[8][1] > pontos[18][1] and
                pontos[8][1] > pontos[19][1] and
                pontos[8][1] > pontos[20][1] and

                pontos[12][1] > pontos[0][1] and
                pontos[12][1] > pontos[1][1] and
                pontos[12][1] > pontos[2][1] and
                pontos[12][1] > pontos[3][1] and
                pontos[12][1] > pontos[4][1] and
                pontos[12][1] > pontos[5][1] and
                pontos[12][1] > pontos[6][1] and
                pontos[12][1] > pontos[7][1] and
                pontos[12][1] > pontos[9][1] and
                pontos[12][1] > pontos[10][1] and
                pontos[12][1] > pontos[11][1] and
                pontos[12][1] > pontos[13][1] and
                pontos[12][1] > pontos[14][1] and
                pontos[12][1] > pontos[15][1] and
                pontos[12][1] > pontos[17][1] and
                pontos[12][1] > pontos[18][1] and
                pontos[12][1] > pontos[19][1] and
                pontos[12][1] > pontos[20][1] and

                pontos[16][1] > pontos[0][1] and
                pontos[16][1] > pontos[1][1] and
                pontos[16][1] > pontos[2][1] and
                pontos[16][1] > pontos[3][1] and
                pontos[16][1] > pontos[4][1] and
                pontos[16][1] > pontos[5][1] and
                pontos[16][1] > pontos[6][1] and
                pontos[16][1] > pontos[7][1] and
                pontos[16][1] > pontos[9][1] and
                pontos[16][1] > pontos[10][1] and
                pontos[16][1] > pontos[11][1] and
                pontos[16][1] > pontos[13][1] and
                pontos[16][1] > pontos[14][1] and
                pontos[16][1] > pontos[15][1] and
                pontos[16][1] > pontos[17][1] and
                pontos[16][1] > pontos[18][1] and
                pontos[16][1] > pontos[19][1] and
                pontos[16][1] > pontos[20][1] and

                pontos[0][1] < pontos[1][1] and
                pontos[0][1] < pontos[2][1] and
                pontos[0][1] < pontos[3][1] and
                pontos[0][1] < pontos[4][1] and
                pontos[0][1] < pontos[5][1] and
                pontos[0][1] < pontos[6][1] and
                pontos[0][1] < pontos[7][1] and
                pontos[0][1] < pontos[8][1] and
                pontos[0][1] < pontos[9][1] and
                pontos[0][1] < pontos[10][1] and
                pontos[0][1] < pontos[11][1] and
                pontos[0][1] < pontos[12][1] and
                pontos[0][1] < pontos[13][1] and
                pontos[0][1] < pontos[14][1] and
                pontos[0][1] < pontos[15][1] and
                pontos[0][1] < pontos[16][1] and
                pontos[0][1] < pontos[17][1] and
                pontos[0][1] < pontos[18][1] and
                pontos[0][1] < pontos[19][1] and
                pontos[0][1] < pontos[20][1]

            ):
                return "M"


    if ( # Letra N
                pontos[8][1] > pontos[0][1] and
                pontos[8][1] > pontos[1][1] and
                pontos[8][1] > pontos[2][1] and
                pontos[8][1] > pontos[3][1] and
                pontos[8][1] > pontos[4][1] and
                pontos[8][1] > pontos[5][1] and
                pontos[8][1] > pontos[6][1] and
                pontos[8][1] > pontos[7][1] and
                pontos[8][1] > pontos[9][1] and
                pontos[8][1] > pontos[10][1] and
                pontos[8][1] > pontos[11][1] and
                pontos[8][1] > pontos[13][1] and
                pontos[8][1] > pontos[14][1] and
                pontos[8][1] > pontos[15][1] and
                pontos[8][1] > pontos[17][1] and
                pontos[8][1] > pontos[18][1] and
                pontos[8][1] > pontos[19][1] and
                pontos[8][1] > pontos[20][1] and

                pontos[12][1] > pontos[0][1] and
                pontos[12][1] > pontos[1][1] and
                pontos[12][1] > pontos[2][1] and
                pontos[12][1] > pontos[3][1] and
                pontos[12][1] > pontos[4][1] and
                pontos[12][1] > pontos[5][1] and
                pontos[12][1] > pontos[6][1] and
                pontos[12][1] > pontos[7][1] and
                pontos[12][1] > pontos[9][1] and
                pontos[12][1] > pontos[10][1] and
                pontos[12][1] > pontos[11][1] and
                pontos[12][1] > pontos[13][1] and
                pontos[12][1] > pontos[14][1] and
                pontos[12][1] > pontos[15][1] and
                pontos[12][1] > pontos[17][1] and
                pontos[12][1] > pontos[18][1] and
                pontos[12][1] > pontos[19][1] and
                pontos[12][1] > pontos[20][1] and

                pontos[16][1] < pontos[12][1] and
                pontos[16][1] < pontos[11][1] and
                pontos[16][1] < pontos[8][1] and
                pontos[16][1] < pontos[7][1] and

                pontos[0][1] < pontos[1][1] and
                pontos[0][1] < pontos[2][1] and
                pontos[0][1] < pontos[3][1] and
                pontos[0][1] < pontos[4][1] and
                pontos[0][1] < pontos[5][1] and
                pontos[0][1] < pontos[6][1] and
                pontos[0][1] < pontos[7][1] and
                pontos[0][1] < pontos[8][1] and
                pontos[0][1] < pontos[9][1] and
                pontos[0][1] < pontos[10][1] and
                pontos[0][1] < pontos[11][1] and
                pontos[0][1] < pontos[12][1] and
                pontos[0][1] < pontos[13][1] and
                pontos[0][1] < pontos[14][1] and
                pontos[0][1] < pontos[15][1] and
                pontos[0][1] < pontos[16][1] and
                pontos[0][1] < pontos[17][1] and
                pontos[0][1] < pontos[18][1] and
                pontos[0][1] < pontos[19][1] and
                pontos[0][1] < pontos[20][1]
            ):
                return "N"


    if ( # Letra O
                pontos[8][2] > pontos[12][2] and
                pontos[12][2] > pontos[16][2] and
                pontos[16][2] > pontos[20][2] and
                pontos[17][2] < pontos[5][2] and
                pontos[17][2] < pontos[13][2] and
                pontos[17][2] < pontos[9][2] and
                pontos[4][1] < pontos[12][1] # and # Se a condição a seguir estiver ativa, tirar o comentário do "and"
                # pontos[20][1] < pontos[13][1] # Condição com possível problema. Em caso de erros em outras mãos, colocar sob comentário.
            ):
                return "O"


    if ( # Letra P
                pontos[8][1] < pontos[0][1] and
                pontos[8][1] < pontos[1][1] and
                pontos[8][1] < pontos[2][1] and
                pontos[8][1] < pontos[3][1] and
                pontos[8][1] < pontos[4][1] and
                pontos[8][1] < pontos[5][1] and
                pontos[8][1] < pontos[6][1] and
                pontos[8][1] < pontos[7][1] and
                pontos[8][1] < pontos[9][1] and
                pontos[8][1] < pontos[10][1] and
                pontos[8][1] < pontos[11][1] and
                pontos[8][1] < pontos[12][1] and
                pontos[8][1] < pontos[13][1] and
                pontos[8][1] < pontos[14][1] and
                pontos[8][1] < pontos[15][1] and
                pontos[8][1] < pontos[16][1] and
                pontos[8][1] < pontos[17][1] and
                pontos[8][1] < pontos[18][1] and
                pontos[8][1] < pontos[19][1] and
                pontos[8][1] < pontos[20][1] and

                pontos[7][1] < pontos[0][1] and
                pontos[7][1] < pontos[1][1] and
                pontos[7][1] < pontos[2][1] and
                pontos[7][1] < pontos[3][1] and
                pontos[7][1] < pontos[4][1] and
                pontos[7][1] < pontos[5][1] and
                pontos[7][1] < pontos[6][1] and
                pontos[7][1] < pontos[9][1] and
                pontos[7][1] < pontos[10][1] and
                pontos[7][1] < pontos[11][1] and
                pontos[7][1] < pontos[12][1] and
                pontos[7][1] < pontos[13][1] and
                pontos[7][1] < pontos[14][1] and
                pontos[7][1] < pontos[15][1] and
                pontos[7][1] < pontos[16][1] and
                pontos[7][1] < pontos[17][1] and
                pontos[7][1] < pontos[18][1] and
                pontos[7][1] < pontos[19][1] and
                pontos[7][1] < pontos[20][1] and

                pontos[4][1] < pontos[11][1] and
                pontos[4][1] < pontos[12][1] and

                pontos[12][0] > pontos[0][0] and
                pontos[12][0] > pontos[1][0] and
                pontos[12][0] > pontos[2][0] and
                pontos[12][0] > pontos[3][0] and
                pontos[12][0] > pontos[4][0] and
                pontos[12][0] > pontos[5][0] and
                pontos[12][0] > pontos[6][0] and
                pontos[12][0] > pontos[7][0] and
                pontos[12][0] > pontos[9][0] and
                pontos[12][0] > pontos[10][0] and
                pontos[12][0] > pontos[11][0] and
                pontos[12][0] > pontos[13][0] and
                pontos[12][0] > pontos[14][0] and
                pontos[12][0] > pontos[15][0] and
                pontos[12][0] > pontos[16][0] and
                pontos[12][0] > pontos[17][0] and
                pontos[12][0] > pontos[18][0] and
                pontos[12][0] > pontos[19][0] and
                pontos[12][0] > pontos[20][0] and
                pontos[12][1] < pontos[15][1] and

                pontos[11][0] > pontos[0][0] and
                pontos[11][0] > pontos[1][0] and
                pontos[11][0] > pontos[2][0] and
                pontos[11][0] > pontos[3][0] and
                pontos[11][0] > pontos[4][0] and
                pontos[11][0] > pontos[5][0] and
                pontos[11][0] > pontos[6][0] and
                pontos[11][0] > pontos[7][0] and
                pontos[11][0] > pontos[9][0] and
                pontos[11][0] > pontos[10][0] and
                pontos[11][0] > pontos[13][0] and
                pontos[11][0] > pontos[14][0] and
                pontos[11][0] > pontos[15][0] and
                pontos[11][0] > pontos[16][0] and
                pontos[11][0] > pontos[17][0] and
                pontos[11][0] > pontos[18][0] and
                pontos[11][0] > pontos[19][0] and
                pontos[11][0] > pontos[20][0]
            ):
                return "P"


    if ( # Letra Q
                pontos[0][1] < pontos[1][1] and
                pontos[0][1] < pontos[2][1] and
                pontos[0][1] < pontos[3][1] and
                pontos[0][1] < pontos[4][1] and
                pontos[0][1] < pontos[5][1] and
                pontos[0][1] < pontos[6][1] and
                pontos[0][1] < pontos[7][1] and
                pontos[0][1] < pontos[8][1] and
                pontos[0][1] < pontos[9][1] and
                pontos[0][1] < pontos[10][1] and
                pontos[0][1] < pontos[11][1] and
                pontos[0][1] < pontos[12][1] and
                pontos[0][1] < pontos[13][1] and
                pontos[0][1] < pontos[14][1] and
                pontos[0][1] < pontos[15][1] and
                pontos[0][1] < pontos[16][1] and
                pontos[0][1] < pontos[17][1] and
                pontos[0][1] < pontos[18][1] and
                pontos[0][1] < pontos[19][1] and
                pontos[0][1] < pontos[20][1] and

                pontos[8][1] > pontos[0][1] and
                pontos[8][1] > pontos[1][1] and
                pontos[8][1] > pontos[2][1] and
                pontos[8][1] > pontos[3][1] and
                pontos[8][1] > pontos[4][1] and
                pontos[8][1] > pontos[5][1] and
                pontos[8][1] > pontos[6][1] and
                pontos[8][1] > pontos[7][1] and
                pontos[8][1] > pontos[9][1] and
                pontos[8][1] > pontos[10][1] and
                pontos[8][1] > pontos[11][1] and
                pontos[8][1] > pontos[12][1] and
                pontos[8][1] > pontos[13][1] and
                pontos[8][1] > pontos[14][1] and
                pontos[8][1] > pontos[15][1] and
                pontos[8][1] > pontos[16][1] and
                pontos[8][1] > pontos[17][1] and
                pontos[8][1] > pontos[18][1] and
                pontos[8][1] > pontos[19][1] and
                pontos[8][1] > pontos[20][1] and

                # Se possível, adicionar mais condições ao ponto 4 (seja no eixo X, Y ou Z)
                pontos[4][1] > pontos[3][1]


            ):
                return "Q"


    if ( # Letra R
                pontos[8][0] < pontos[12][0] and
                pontos[6][0] > pontos[10][0] and
                pontos[20][1] > pontos[17][1] and
                pontos[16][1] > pontos[15][1]
            ):
                return "R"


    if ( # Letra S
                pontos[8][1] > pontos[5][1] and
                pontos[12][1] > pontos[9][1] and
                pontos[16][1] > pontos[13][1] and
                pontos[20][1] > pontos[17][1] and
                pontos[4][1] < pontos[5][1] and

                pontos[4][0] < pontos[6][0] and
                pontos[4][0] < pontos[5][0]
             ):
                return "S"



          #  if ( # Letra T
                # pontos[4][2] > pontos[0][2] and
                # pontos[4][2] > pontos[1][2] and
                # pontos[4][2] > pontos[2][2] and
                # pontos[4][2] > pontos[3][2] and
                # pontos[4][2] < pontos[6][2] and
                # pontos[4][2] < pontos[7][2] and
                # pontos[4][2] < pontos[8][2] and
                # pontos[6][1] > pontos[10][1] and
                # pontos[6][1] > pontos[14][1] and
                # pontos[6][1] > pontos[19][1] and
                # pontos[7][1] > pontos[10][1] and
                # pontos[7][1] > pontos[14][1] and
                # pontos[7][1] > pontos[19][1] and
                # pontos[8][1] > pontos[10][1] and
                # pontos[8][1] > pontos[14][1] and
                # pontos[8][1] > pontos[19][1] and
                # pontos[20][1] > pontos[15][1]
            # ):
                # return "T"


    if ( # Letra U
                pontos[20][1] > pontos[17][1] and
                pontos[16][1] > pontos[13][1] and
                pontos[12][1] < pontos[11][1] and
                pontos[8][1] < pontos[7][1] and
                abs(pontos[8][0] - pontos[12][0]) < 25 and
                pontos[4][2] < pontos[8][2]
            ):
                return "U"


    if ( # Letra V
                pontos[20][1] > pontos[17][1] and
                pontos[16][1] > pontos[13][1] and
                pontos[12][1] < pontos[11][1] and
                pontos[8][1] < pontos[7][1] and
                abs(pontos[8][0] - pontos[12][0])  >=  25 and
                pontos[4][2] < pontos[8][2]
            ):
                return "V"


    if ( # Letra W
                pontos[8][1] < pontos[7][1] and
                pontos[12][1] < pontos[11][1] and
                pontos[16][1] < pontos[15][1] and
                pontos[20][1] > pontos[19][1] and
                abs(pontos[12][0] - pontos[8][0]) >= 25 and
                abs(pontos[16][0] - pontos[12][0]) >= 25
            ):
                return "W"


    if ( # Letra X
                pontos[8][1] < pontos[6][1] and
                pontos[20][1] > pontos[17][1] and
                pontos[16][1] > pontos[13][1] and
                pontos[12][1] > pontos[9][1] and
                pontos[12][1] > pontos[5][1] and
                abs(pontos[8][1] - pontos[10][1]) >= 50 and
                abs(pontos[8][1] - pontos[5][1]) >= 50 and
                abs(pontos[8][1] - pontos[4][1]) >= 35
            ):
                return "X"


    if ( # Letra Y
                pontos[8][1] > pontos[7][1] and
                pontos[20][1] < pontos[19][1] and
                pontos[16][1] > pontos[15][1] and
                pontos[12][1] > pontos[11][1] and
                pontos[4][0] > pontos[3][0]
            ):
                return "Y"


    if ( # Letra Z
                pontos[8][2] < pontos[0][2] and
                pontos[8][2] < pontos[1][2] and
                pontos[8][2] < pontos[2][2] and
                pontos[8][2] < pontos[3][2] and
                pontos[8][2] < pontos[4][2] and
                pontos[8][2] < pontos[5][2] and
                pontos[8][2] < pontos[6][2] and
                pontos[8][2] < pontos[7][2] and
                pontos[8][2] < pontos[9][2] and
                pontos[8][2] < pontos[10][2] and
                pontos[8][2] < pontos[12][2] and
                pontos[8][2] < pontos[11][2] and
                pontos[8][2] < pontos[13][2] and
                pontos[8][2] < pontos[14][2] and
                pontos[8][2] < pontos[15][2] and
                pontos[8][2] < pontos[16][2] and
                pontos[8][2] < pontos[18][2] and
                pontos[8][2] < pontos[17][2] and
                pontos[8][2] < pontos[19][2] and
                pontos[8][2] < pontos[20][2] and

                pontos[17][1] < pontos[18][1] and
                pontos[13][1] < pontos[14][1] and
                pontos[9][1] < pontos[10][1]
            ):
                return "Z"

    if ( # Libra Eu te amo (❤️)
            pontos[8][1] < pontos[0][1] and
            pontos[8][1] < pontos[1][1] and
            pontos[8][1] < pontos[2][1] and
            pontos[8][1] < pontos[3][1] and
            pontos[8][1] < pontos[4][1] and
            pontos[8][1] < pontos[5][1] and
            pontos[8][1] < pontos[6][1] and
            pontos[8][1] < pontos[7][1] and
            pontos[8][1] < pontos[9][1] and
            pontos[8][1] < pontos[10][1] and
            pontos[8][1] < pontos[11][1] and
            pontos[8][1] < pontos[12][1] and
            pontos[8][1] < pontos[13][1] and
            pontos[8][1] < pontos[14][1] and
            pontos[8][1] < pontos[15][1] and
            pontos[8][1] < pontos[16][1] and
            pontos[8][1] < pontos[17][1] and

            pontos[7][1] < pontos[0][1] and
            pontos[7][1] < pontos[1][1] and
            pontos[7][1] < pontos[2][1] and
            pontos[7][1] < pontos[3][1] and
            pontos[7][1] < pontos[4][1] and
            pontos[7][1] < pontos[5][1] and
            pontos[7][1] < pontos[6][1] and
            pontos[7][1] > pontos[8][1] and
            pontos[7][1] < pontos[9][1] and
            pontos[7][1] < pontos[10][1] and
            pontos[7][1] < pontos[11][1] and
            pontos[7][1] < pontos[12][1] and
            pontos[7][1] < pontos[13][1] and
            pontos[7][1] < pontos[14][1] and
            pontos[7][1] < pontos[15][1] and
            pontos[7][1] < pontos[16][1] and
            pontos[7][1] < pontos[17][1] and

            pontos[6][1] < pontos[0][1] and
            pontos[6][1] < pontos[1][1] and
            pontos[6][1] < pontos[2][1] and
            pontos[6][1] < pontos[3][1] and
            pontos[6][1] < pontos[4][1] and
            pontos[6][1] < pontos[5][1] and
            pontos[6][1] > pontos[7][1] and
            pontos[6][1] > pontos[8][1] and
            pontos[6][1] < pontos[9][1] and
                pontos[6][1] < pontos[10][1] and
                pontos[6][1] < pontos[11][1] and
                pontos[6][1] < pontos[12][1] and
                pontos[6][1] < pontos[13][1] and
                pontos[6][1] < pontos[14][1] and
                pontos[6][1] < pontos[15][1] and
                pontos[6][1] < pontos[16][1] and
                pontos[6][1] < pontos[17][1] and

                pontos[4][0] > pontos[0][0] and
                pontos[4][0] > pontos[1][0] and
                pontos[4][0] > pontos[2][0] and
                pontos[4][0] > pontos[3][0] and
                pontos[4][0] > pontos[5][0] and
                pontos[4][0] > pontos[7][0] and
                pontos[4][0] > pontos[8][0] and
                pontos[4][0] > pontos[9][0] and
                pontos[4][0] > pontos[10][0] and
                pontos[4][0] > pontos[11][0] and
                pontos[4][0] > pontos[12][0] and
                pontos[4][0] > pontos[13][0] and
                pontos[4][0] > pontos[14][0] and
                pontos[4][0] > pontos[15][0] and
                pontos[4][0] > pontos[16][0] and
                pontos[4][0] > pontos[17][0] and
                pontos[4][0] > pontos[18][0] and
                pontos[4][0] > pontos[19][0] and
                pontos[4][0] > pontos[20][0] and

                pontos[3][0] > pontos[0][0] and
                pontos[3][0] > pontos[1][0] and
                pontos[3][0] > pontos[2][0] and
                pontos[3][0] > pontos[5][0] and
                pontos[3][0] > pontos[9][0] and
                pontos[3][0] > pontos[10][0] and
                pontos[3][0] > pontos[11][0] and
                pontos[3][0] > pontos[12][0] and
                pontos[3][0] > pontos[13][0] and
                pontos[3][0] > pontos[14][0] and
                pontos[3][0] > pontos[15][0] and
                pontos[3][0] > pontos[16][0] and
                pontos[3][0] > pontos[17][0] and
                pontos[3][0] > pontos[18][0] and
                pontos[3][0] > pontos[19][0] and
                pontos[3][0] > pontos[20][0] and

                pontos[20][1] < pontos[19][1] and
                pontos[19][1] < pontos[18][1]

            ):
                return "Eu te amo"


    return None

def gerar_frames():
    global last_libra
    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Conversão de BGR para RGB para processar no Mediapipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        pontos = []

        # Processamento dos pontos das mãos
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for id, cord in enumerate(hand_landmarks.landmark):
                    h, w, _ = frame.shape
                    cx, cy = int(cord.x * w), int(cord.y * h)
                    pontos.append((cx, cy, cord.z))

                # Detecção da letra
                letra = detectar_libra(pontos)
                if letra:
                    last_libra = letra
                    cv2.putText(frame, f"Letra: {letra}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                # Desenha as conexões e pontos das mãos no frame
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Codificação do frame para formato jpeg
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Geração do frame para a resposta HTTP
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html', letra=last_libra)

@app.route('/video_feed')
def video_feed():
    return Response(gerar_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)

